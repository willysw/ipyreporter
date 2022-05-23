from typing import Any


class ReporterItem:
    """ Represents a single item to report.

    Is normally only used internally.
    """
    name: str
    value: Any
    units: str
    desc: str

    def __init__(self, name: str, value_args) -> None:
        self.name = name
        if isinstance(value_args, tuple):
            # Decode extra information
            self.value, self.units, self.desc = self._decode(value_args)
        else:
            self.value, self.units, self.desc = value_args, "", ""

    def __str__(self) -> str:
        str_out = f"{self.name}: {self.value}"
        if self.units:
            str_out += f" {self.units}"
        if self.desc:
            str_out += f", {self.desc}"
        return str_out

    def __repr__(self) -> str:
        return f"ReporterItem({self.name}, {self.value}, {self.units}, {self.desc})"

    @staticmethod
    def _decode(value_args) -> tuple[Any, str, str]:
        # Guarantee at least 3 elements
        value_args = list(value_args) + ['', '']
        value, unit, desc = value_args[:3]
        if not isinstance(unit, str):
            unit = str(unit)
        if not isinstance(unit, str):
            desc = str(desc)
        return value, unit, desc
