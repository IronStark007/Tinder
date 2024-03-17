from email import message
from unicodedata import name


class AppException(Exception):
    message: str = "Base exception"
    error_code: int = 500

class UserAlreadyExistsError(AppException):
    error_code = 400
    message = "user already exists"

class EmailOrPasswordError(AppException):
    error_code = 400
    message = "email does not exist or incorrect password"
