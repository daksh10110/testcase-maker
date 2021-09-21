from typing import List, Union, TYPE_CHECKING

import attr

from testcase_maker.values import BaseValue, Constant, LoopValue

if TYPE_CHECKING:
    from testcase_maker.resolver import Resolver


@attr.define()
class ValueGroup(BaseValue):
    values: List[BaseValue] = attr.ib(factory=list)

    def add(self, value: BaseValue):
        self.values.append(value)

    def space(self):
        self.add(Constant(" "))

    def newline(self):
        self.add(Constant("\n"))

    def repeat(self, value: "BaseValue", amount: Union[BaseValue, int], delimiter: str):
        self.add(LoopValue(value, amount, delimiter))

    def generate(self, resolver: "Resolver") -> str:
        output_string = ""
        for value in self.values:
            resolved_value = resolver.resolve(value)
            output_string += str(resolved_value)

        return output_string
