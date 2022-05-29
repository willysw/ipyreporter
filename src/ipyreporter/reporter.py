from collections.abc import MutableMapping
from typing import Any, Iterator

from reporter_item import ReporterItem


class Reporter(MutableMapping):
    subsection: str

    def __init__(self, subsection: str = '') -> None:
        self._item_dict = dict()
        self.subsection = subsection

    def __call__(self, **kwargs) -> None:
        for key, val in kwargs.items():
            self.__setitem__(key, val)

    # =========================
    # =   Attribute Support   =
    # =========================

    def __getattr__(self, key) -> Any:
        item: ReporterItem = self._item_dict.__getitem__(key)
        return item.value

    def __setattr__(self, key, value) -> None:
        # Set variable if it exists
        if ('_item_dict' in self.__dict__) and (key in self._item_dict):
            self._item_dict.__setitem__(key, ReporterItem(key, value))

        # Delegate to object otherwise
        else:
            object.__setattr__(self, key, value)

    # ===========================
    # =   Implement Abstracts   =
    # ===========================

    def __getitem__(self, key) -> Any:
        item: ReporterItem = self._item_dict.__getitem__(key)
        return item.value

    def __setitem__(self, key, value) -> None:
        self._item_dict.__setitem__(key, ReporterItem(key, value))

    def __delitem__(self, key) -> None:
        self._item_dict.__delitem__(key)

    def __len__(self) -> int:
        return self._item_dict.__len__()

    def __iter__(self) -> Iterator[Any]:
        return ((key, item.value) for key, item in self._item_dict.items())

    def update(*args, **kwargs) -> None:
        raise NotImplementedError

    def __str__(self) -> str:
        item_strings = "\n".join([item.__str__()
                                 for item in self._item_dict.values()])
        if self.subsection:
            return self.subsection + "\n" + item_strings
        else:
            return item_strings

    def __repr__(self) -> str:
        return self.__str__()
