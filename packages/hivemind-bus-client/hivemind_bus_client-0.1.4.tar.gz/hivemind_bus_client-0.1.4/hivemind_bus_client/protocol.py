from dataclasses import dataclass

import pgpy
from ovos_bus_client import Message as MycroftMessage
from ovos_bus_client import MessageBusClient
from ovos_bus_client.message import Message
from ovos_bus_client.session import Session, SessionManager
from ovos_utils.log import LOG
from poorman_handshake import HandShake, PasswordHandShake
from typing import Optional

from hivemind_bus_client.client import HiveMessageBusClient
from hivemind_bus_client.identity import NodeIdentity
from hivemind_bus_client.message import HiveMessage, HiveMessageType


@dataclass()
class HiveMindSlaveInternalProtocol:
    """ this class handles all interactions between a hivemind listener and a ovos-core messagebus"""
    hm_bus: HiveMessageBusClient
    share_bus: bool = False
    bus: Optional[MessageBusClient] = None
    node_id: str = ""  # this is how ovos-core bus refers to this slave's master

    def register_bus_handlers(self):
        self.bus.on("hive.send.upstream", self.handle_send)
        self.bus.on("message", self.handle_outgoing_mycroft)  # catch all

    # mycroft handlers  - from slave -> master
    def handle_send(self, message: Message):
        """ ovos wants to send a HiveMessage

        a device can be both a master and a slave, upstream messages are handled here

        HiveMindListenerInternalProtocol will handle requests meant to go downstream
        """

        payload = message.data.get("payload")
        msg_type = message.data["msg_type"]

        hmessage = HiveMessage(msg_type, payload=payload)

        if msg_type == HiveMessageType.BROADCAST:
            # only masters can broadcast, ignore silently
            #   if this device is also a master to something,
            #   HiveMindListenerInternalProtocol will handle the request
            pass
        else:
            self.hm_bus.emit(hmessage)

    def handle_outgoing_mycroft(self, message: Message):
        """ forward internal messages to masters"""
        if isinstance(message, str):
            # "message" is a special case in ovos-bus-client that is not deserialized
            message = Message.deserialize(message)

        # this allows the master node to do passive monitoring of bus events
        if self.share_bus:
            msg = HiveMessage(HiveMessageType.SHARED_BUS,
                              payload=message.serialize())
            self.hm_bus.emit(msg)

        # this message is targeted at master
        # eg, a response to some bus event injected by master
        # note: master might completely ignore it
        peers = message.context.get("destination")
        if peers:
            if not isinstance(peers, list):
                peers = [peers]
            if self.node_id in peers:
                msg = HiveMessage(HiveMessageType.BUS,
                                  payload=message.serialize())
                self.hm_bus.emit(msg)


@dataclass()
class HiveMindSlaveProtocol:
    """
    Joins this instance ovos-core bus with master ovos-core bus
    Master becomes able to inject arbitrary bus messages
    """
    hm: HiveMessageBusClient
    identity: Optional[NodeIdentity] = None
    handshake: Optional[HandShake] = None
    pswd_handshake: Optional[PasswordHandShake] = None
    internal_protocol: HiveMindSlaveInternalProtocol = None
    mpubkey: str = ""  # asc public PGP key from master
    shared_bus: bool = False
    binarize: bool = False
    site_id: str = "unknown"

    def bind(self, bus: Optional[MessageBusClient] = None):
        if self.identity is None:
            self.identity = self.hm.identity or NodeIdentity()
        self.handshake = HandShake(self.identity.private_key)
        self.pswd_handshake = PasswordHandShake(self.identity.password) if self.identity.password else None

        if bus is None:
            bus = MessageBusClient()
            bus.run_in_thread()
            bus.connected_event.wait()
        LOG.info("Initializing HiveMindSlaveInternalProtocol")
        self.internal_protocol = HiveMindSlaveInternalProtocol(bus=bus, hm_bus=self.hm)
        self.internal_protocol.register_bus_handlers()
        LOG.info("registering protocol handlers")
        self.hm.on(HiveMessageType.HELLO, self.handle_hello)
        self.hm.on(HiveMessageType.BROADCAST, self.handle_broadcast)
        self.hm.on(HiveMessageType.PROPAGATE, self.handle_propagate)
        self.hm.on(HiveMessageType.INTERCOM, self.handle_intercom)
        self.hm.on(HiveMessageType.ESCALATE, self.handle_illegal_msg)
        self.hm.on(HiveMessageType.SHARED_BUS, self.handle_illegal_msg)
        self.hm.on(HiveMessageType.BUS, self.handle_bus)
        self.hm.on(HiveMessageType.HANDSHAKE, self.handle_handshake)

    @property
    def node_id(self):
        # this is how ovos-core bus refers to this slave's master
        return self.internal_protocol.node_id

    # TODO - handshake handlers
    # hivemind events
    def handle_illegal_msg(self, message: HiveMessage):
        # this should not happen,
        # only sent from client -> server NOT server -> client
        # TODO log, kill connection (?)
        LOG.warning(f"illegal message {message}")

    def handle_hello(self, message: HiveMessage):
        # this check is because other nodes in the hive
        # may also send HELLO with their pubkey
        # only want this on the first connection
        LOG.info(f"HELLO: {message.payload}")
        if not self.node_id:
            self.mpubkey = message.payload.get("pubkey")
            node_id = message.payload.get("node_id", "")
            self.internal_protocol.node_id = node_id
            LOG.info(f"Connected to HiveMind: {node_id}")
        if "session_id" in message.payload:
            self.internal_protocol.bus.session_id = message.payload["session_id"]
            LOG.debug("session_id updated to: " + message.payload["session_id"])

    def start_handshake(self):
        if self.binarize:
            LOG.info("hivemind supports binarization protocol")
        else:
            LOG.info("hivemind does not support binarization protocol")

        sess = Session(self.hm.session_id)
        if self.pswd_handshake is not None:
            envelope = self.pswd_handshake.generate_handshake()
            msg = HiveMessage(HiveMessageType.HANDSHAKE, {"envelope": envelope,
                                                          "binarize": self.binarize,
                                                          "session": sess.serialize(),
                                                          "site_id": self.site_id})
        else:
            msg = HiveMessage(HiveMessageType.HANDSHAKE, {"pubkey": self.handshake.pubkey,
                                                          "binarize": self.binarize,
                                                          "session": sess.serialize(),
                                                          "site_id": self.site_id})
        self.hm.emit(msg)

    def receive_handshake(self, envelope):
        if self.pswd_handshake is not None:
            LOG.info("Received password envelope")
            self.pswd_handshake.receive_and_verify(envelope)  # validate master password matched
            self.hm.crypto_key = self.pswd_handshake.secret  # update to new crypto key
        else:
            LOG.info("Received pubkey envelope")
            # if we have a pubkey let's verify the master node is who it claims to be
            # currently this is sent in HELLO, but advance use cases can read it from somewhere else
            if self.mpubkey:
                # authenticates the server to the client
                self.handshake.receive_and_verify(envelope, self.mpubkey)
            else:
                # implicitly trust the server
                self.handshake.receive_handshake(envelope)
            self.hm.crypto_key = self.handshake.secret  # update to new crypto key
        self.hm.handshake_event.set()

    def handle_handshake(self, message: HiveMessage):
        LOG.info(f"HANDSHAKE: {message.payload}")
        # master is performing the handshake
        if "envelope" in message.payload:
            envelope = message.payload["envelope"]
            self.receive_handshake(envelope)

        # master is requesting handshake start
        else:
            # required = message.payload.get("handshake")
            # if not required:
            #    self.hm.handshake_event.set()  # don't wait
            #    return

            if message.payload.get("crypto_key") and self.hm.crypto_key:
                pass
                # we can use the pre-shared key instead of handshake
                # TODO - flag to give preference to pre-shared key over handshake

            self.binarize = message.payload.get("binarize", False)
            # TODO - flag to give preference to / require password or not
            # currently if password is set then it is always used
            if message.payload.get("password") and self.identity.password:
                self.pswd_handshake = PasswordHandShake(self.identity.password)
                self.start_handshake()

    def handle_bus(self, message: HiveMessage):
        LOG.info(f"BUS: {message.payload.msg_type}")
        assert isinstance(message.payload, MycroftMessage)
        # master wants to inject message into mycroft bus
        pload = message.payload

        # update session sent from hivemind-core
        sess = Session.from_message(pload)
        if sess.session_id == self.hm.session_id:
            sess.site_id = self.site_id  # do not allow overwriting site_id
        SessionManager.update(sess)

        # from this point on, it should be a native source and execute audio
        if "destination" in pload.context:
            pload.context["source"] = pload.context.pop("destination")
        self.internal_protocol.bus.emit(pload)

    def handle_broadcast(self, message: HiveMessage):
        LOG.info(f"BROADCAST: {message.payload}")

        if message.payload.msg_type == HiveMessageType.INTERCOM:
            if self.handle_intercom(message):
                return True

        if message.payload.msg_type == HiveMessageType.BUS:
            # if the message targets our site_id, send it to internal bus
            site = message.target_site_id
            if site and site == self.site_id:
                self.handle_bus(message.payload)

        # if this device is also a hivemind server
        # forward to HiveMindListenerInternalProtocol
        data = message.serialize()
        ctxt = {"source": self.node_id}
        self.internal_protocol.bus.emit(MycroftMessage('hive.send.downstream', data, ctxt))

    def handle_propagate(self, message: HiveMessage):
        LOG.info(f"PROPAGATE: {message.payload}")

        if message.payload.msg_type == HiveMessageType.INTERCOM:
            if self.handle_intercom(message):
                return True

        if message.payload.msg_type == HiveMessageType.BUS:
            # if the message targets our site_id, send it to internal bus
            site = message.target_site_id
            if site and site == self.site_id:
                # might originate from untrusted
                # satellite anywhere in the hive
                # do not inject by default
                pass  # TODO - when to inject ? add list of trusted peers?
                # self.handle_bus(message.payload)

        # if this device is also a hivemind server
        # forward to HiveMindListenerInternalProtocol
        data = message.serialize()
        ctxt = {"source": self.node_id}
        self.internal_protocol.bus.emit(MycroftMessage('hive.send.downstream', data, ctxt))

    def handle_intercom(self, message: HiveMessage):
        LOG.info(f"INTERCOM: {message.payload}")

        # if the message targets our site_id, send it to internal bus
        k = message.target_public_key
        if k and k != self.identity.public_key:
            # not for us
            return False

        pload = message.payload
        if isinstance(pload, dict) and "ciphertext" in pload:
            try:
                message_from_blob = pgpy.PGPMessage.from_blob(pload["ciphertext"])

                with open(self.identity.private_key, "r") as f:
                    private_key = pgpy.PGPKey.from_blob(f.read())

                decrypted: str = private_key.decrypt(message_from_blob)
                message._payload = HiveMessage.deserialize(decrypted)
            except:
                if k:
                    LOG.error("failed to decrypt message!")
                else:
                    LOG.debug("failed to decrypt message, not for us")
                return False

        if message.msg_type == HiveMessageType.BUS:
            self.handle_bus(message)
            return True
        elif message.msg_type == HiveMessageType.PROPAGATE:
            self.handle_propagate(message)
            return True
        elif message.msg_type == HiveMessageType.BROADCAST:
            self.handle_broadcast(message)
            return True
        return False
