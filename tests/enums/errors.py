from enum import Enum


class GlobalError(Enum):
    WRONG_STATUS_CODE = "Status code is not equal expected."
    WRONG_NUMBER_OF_POSTS = "The number of posts does not equal the expected number of posts."
