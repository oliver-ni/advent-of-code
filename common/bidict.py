from __future__ import annotations

from typing import Generic, Optional, TypeVar

A = TypeVar("A")
B = TypeVar("B")
T = TypeVar("T")


class Bidict(Generic[A, B]):
    def __init__(self, _orig: Optional[Bidict[B, A]] = None):
        if _orig is None:
            self._inner: dict[A, B] = {}
            self.reverse = Bidict(_orig=self)
        else:
            self._inner = {b: a for a, b in _orig.items()}
            self.reverse = _orig

    def __getitem__(self, key: A):
        return self._inner.__getitem__(key)

    def __setitem__(self, key: A, value: B, *, _initial: bool = True):
        if key in self:
            del self[key]
        if _initial:
            self.reverse.__setitem__(value, key, _initial=False)
        self._inner.__setitem__(key, value)

    def __delitem__(self, key: A, *, _initial: bool = True):
        if _initial:
            self.reverse.__delitem__(self[key], _initial=False)
        self._inner.__delitem__(key)

    def __contains__(self, key):
        return self._inner.__contains__(key)

    def __repr__(self):
        return self._inner.__repr__()

    def __iter__(self):
        return iter(self.keys())

    def keys(self):
        return self._inner.keys()

    def values(self):
        return self._inner.values()

    def items(self):
        return self._inner.items()
