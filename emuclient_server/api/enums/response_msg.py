from enum import Enum

class ResponseMessage(Enum):
    UNAUTHORIZED = "You're not authorized to use this product"
    UNEXPECTED_ERROR = "An unexpected error ocurred during the proccess"