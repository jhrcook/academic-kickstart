from typing import (
    Any,
    Iterable,
    SupportsIndex,
    Union,
    overload,
    TypeVar,
)

T = TypeVar("T")


class MyList(list[T]):
    @overload
    def __getitem__(self, i: SupportsIndex) -> T:
        ...

    @overload
    def __getitem__(self, i: slice) -> list[T]:
        ...

    def __getitem__(self, i: Union[SupportsIndex, slice]) -> Union[T, list[T]]:
        # Implement your specific features here.
        return super().__getitem__(i)

    @overload
    def __setitem__(self, i: SupportsIndex, o: T) -> None:
        ...

    @overload
    def __setitem__(self, s: slice, o: Iterable[T]) -> None:
        ...

    def __setitem__(self, *args: Any) -> None:
        # Implement your specific features here.
        super().__setitem__(*args)
        return None


class IntcodeMinimalTyping(list[int]):
    def __getitem__(self, i: Union[SupportsIndex, slice]) -> Union[int, list[int]]:
        self._extend_based_on_index(i)
        return super().__getitem__(i)

    def __setitem__(
        self, i: Union[SupportsIndex, slice], o: Union[int, Iterable[int]]
    ) -> None:
        if isinstance(i, (SupportsIndex, slice)):
            self._extend_based_on_index(i)

        super().__setitem__(i, o)
        return None

    def _ensure_length_atleast(self, x: int) -> None:
        if x >= len(self):
            self.extend([0] * (x + 1 - len(self)))

    def _extend_based_on_index(self, i: Union[SupportsIndex, slice]) -> None:
        if isinstance(i, SupportsIndex):
            self._ensure_length_atleast(x=int(i))
        elif isinstance(i, slice):
            x = max([a for a in (i.start, i.stop, i.stop) if a is not None])
            self._ensure_length_atleast(x=x)


class Intcode(list[int]):
    @overload
    def __getitem__(self, i: SupportsIndex) -> int:
        ...

    @overload
    def __getitem__(self, i: slice) -> list[int]:
        ...

    def __getitem__(self, i: Union[SupportsIndex, slice]) -> Union[int, list[int]]:
        self._extend_based_on_index(i)
        return super().__getitem__(i)

    @overload
    def __setitem__(self, i: SupportsIndex, o: int) -> None:
        ...

    @overload
    def __setitem__(self, s: slice, o: Iterable[int]) -> None:
        ...

    def __setitem__(self, *args: Any) -> None:
        assert len(args) == 2
        idx = args[0]
        if isinstance(idx, (SupportsIndex, slice)):
            self._extend_based_on_index(idx)

        super().__setitem__(*args)
        return None

    def _ensure_length_atleast(self, x: int) -> None:
        if x >= len(self):
            self.extend([0] * (x + 1 - len(self)))

    def _extend_based_on_index(self, i: Union[SupportsIndex, slice]) -> None:
        if isinstance(i, SupportsIndex):
            self._ensure_length_atleast(x=int(i))
        elif isinstance(i, slice):
            x = max([a for a in (i.start, i.stop, i.stop) if a is not None])
            self._ensure_length_atleast(x=x)
