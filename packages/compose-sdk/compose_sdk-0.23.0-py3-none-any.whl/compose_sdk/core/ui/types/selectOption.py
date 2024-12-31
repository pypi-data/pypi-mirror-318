from typing import TypedDict, Union, List
from typing_extensions import NotRequired

SelectOptionValue = Union[str, int, bool]


class SelectOptionDict(TypedDict):
    value: SelectOptionValue
    label: str
    description: NotRequired[str]


SelectOptionPrimitive = SelectOptionValue

SelectOptions = List[Union[SelectOptionDict, SelectOptionPrimitive]]
