from enum import Enum

from pydantic import BaseModel
from triggers.bases.enums import QuotedEnum


def process_value(value) -> str:
    if value is None:
        raise Exception("Something has None")

    if isinstance(value, QuotedEnum):
        return f'"{value.value}"'

    if isinstance(value, Enum):
        return value.value

    if isinstance(value, int):
        return str(value)

    return value


class BaseNode(BaseModel):
    def get_parameters(self):
        parameter_order = self.parameter_order()
        param_length = len(parameter_order)
        result = ""
        for i in range(param_length):
            result += process_value(parameter_order[i])
            if i < param_length - 1:
                result += ","
        return result

    def get_trigger(self):
        format = f"{self.__class__.__name__}("
        format += self.get_parameters()
        format += ");"
        return format

    def parameter_order(self):
        return [
            getattr(self, field_name)
            for field_name in self.__annotations__.keys()  # noqa
        ]  # noqa
