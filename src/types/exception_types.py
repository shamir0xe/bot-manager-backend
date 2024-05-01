from enum import Enum


class ExceptionTypes(Enum):
    LOGIN_NEEDED = "login-needed"
    NO_BOT_AVAILABLE = "no-bot-available"
    NO_SUCH_PAIR_FOUND = "no-such-pair-found"
    CANNOT_CREATE_PAIR = "cannot-create-pair"
    VALIDATOR_ERROR = "validator-error"
    NO_SUCH_OBJECT_EXISTS = "no-such-object-exists"
    INVALID_REQUEST = "invalid-request"
    INVALID_TOKEN = "invalid-token"
    INVALID_ARGUMENTS = "invalid-arguments"
    NOT_PERMITTED = "not-permitted"
    INTERNAL_ERROR = "internal-error"
    NO_OWNER_FOUND = "no-owner-found"
