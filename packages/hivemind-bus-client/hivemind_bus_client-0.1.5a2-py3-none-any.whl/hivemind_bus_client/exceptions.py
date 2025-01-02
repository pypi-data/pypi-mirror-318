
class UnsupportedProtocolVersion(ValueError):
    """ Specified protocol version is not supported """


class HiveMindException(Exception):
    """ An Exception inside the HiveMind"""


class UnauthorizedKeyError(HiveMindException):
    """ Invalid Key provided """


class WrongEncryptionKey(HiveMindException):
    """ Wrong Encryption Key"""


class DecryptionKeyError(WrongEncryptionKey):
    """ Could not decrypt payload """


class EncryptionKeyError(WrongEncryptionKey):
    """ Could not encrypt payload """


class HiveMindConnectionError(ConnectionError, HiveMindException):
    """ Could not connect to the HiveMind"""


class SecureConnectionFailed(HiveMindConnectionError):
    """ Could not connect by SSL """


class HiveMindEntryPointNotFound(HiveMindConnectionError):
    """ can not connect to provided address """
