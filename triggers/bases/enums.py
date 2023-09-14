from enums import Enum


class strEnum(str, Enum):
    pass


class QuotedEnum(strEnum):
    pass


class QuotedStr(str):
    pass
