try:
    from enum import StrEnum
except ImportError:
    from strenum import StrEnum


class ClientError(Exception):
    """Base exception for all client errors"""
    pass


class RequestFailedError(ClientError):
    def __init__(self, response):
        self.response = response

    def __str__(self):
        return f"Invalid response: {self.response.status} - {self.response.reason}"


class CommandError(ClientError):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return f"Command not succesful: {self.data!r}"


class ApiError(ClientError):
    """API error"""
    def __init__(self, error_code, error_message):
        super().__init__()
        self.error_code = error_code
        self.error_message = error_message

    def __str__(self) -> str:
        return f"API error: {self.error_code} - {self.error_message}"


class AuthenticationError(ApiError):
    """Authentication error"""
    def __str__(self) -> str:
        return f"Authentication error: {self.error_code} - {self.error_message}"


class InvalidData(ClientError):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return f"Invalid data from server: {self.data!r}"


class AuthenticationErrorCodes(StrEnum):
    """Authentication error codes"""
    SESSION_CLOSED = "1001-0001"
    INVALID_USERNAME_OR_PASSWORD = "1001-1401"

    @staticmethod
    def values() -> list[str]:
        """Return all error codes"""
        return AuthenticationErrorCodes.__members__.values()
