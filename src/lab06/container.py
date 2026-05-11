from typing import TypeVar, Generic, Callable, Optional, List, Iterator
from typing import Protocol

T = TypeVar('T')
R = TypeVar('R')

class TypedCollection(Generic[T]):
    def __init__(self) -> None:
        self._items: List[T] = []

    def add(self, item: T) -> None:
        self._items.append(item)

    def remove(self, item: T) -> None:
        self._items.remove(item)

    def get_all(self) -> List[T]:
        return list(self._items)

    def __len__(self) -> int:
        return len(self._items)

    def __iter__(self) -> Iterator[T]:
        return iter(self._items)

    def __getitem__(self, index: int) -> T:
        return self._items[index]

    def remove_at(self, index: int) -> T:
        if index < 0 or index >= len(self._items):
            raise IndexError("Индекс вне диапазона")
        return self._items.pop(index)

    def find_by_number(self, number: str) -> Optional[T]:
        for item in self._items:
            if item.number == number:
                return item
        return None

    def find_by_route(self, route: str) -> List[T]:
        return [item for item in self._items if item.route == route]

    def find_by_status(self, status: str) -> List[T]:
        return [item for item in self._items if item.status == status]

    def find_by_price_range(self, min_price: float, max_price: float) -> List[T]:
        return [item for item in self._items if min_price <= item.price <= max_price]

    def sort_by_price(self) -> None:
        self._items.sort(key=lambda item: item.price)

    def sort_by_route(self) -> None:
        self._items.sort(key=lambda item: item.route)

    def sort_by_status(self) -> None:
        order = {"available": 0, "sold": 1, "used": 2}
        self._items.sort(key=lambda item: order[item.status])

    def get_available(self) -> 'TypedCollection[T]':
        new_coll = TypedCollection[T]()
        for item in self._items:
            if item.status == "available":
                new_coll.add(item)
        return new_coll

    def get_sold(self) -> 'TypedCollection[T]':
        new_coll = TypedCollection[T]()
        for item in self._items:
            if item.status == "sold":
                new_coll.add(item)
        return new_coll

    def get_used(self) -> 'TypedCollection[T]':
        new_coll = TypedCollection[T]()
        for item in self._items:
            if item.status == "used":
                new_coll.add(item)
        return new_coll

    def get_by_route(self, route: str) -> 'TypedCollection[T]':
        new_coll = TypedCollection[T]()
        for item in self._items:
            if item.route == route:
                new_coll.add(item)
        return new_coll

    def get_expensive(self, threshold: float) -> 'TypedCollection[T]':
        new_coll = TypedCollection[T]()
        for item in self._items:
            if item.price > threshold:
                new_coll.add(item)
        return new_coll

    def find(self, predicate: Callable[[T], bool]) -> Optional[T]:
        for item in self._items:
            if predicate(item):
                return item
        return None

    def filter(self, predicate: Callable[[T], bool]) -> List[T]:
        return [item for item in self._items if predicate(item)]

    def map(self, transform: Callable[[T], R]) -> List[R]:
        return [transform(item) for item in self._items]

    def __str__(self) -> str:
        if not self._items:
            return "Коллекция пуста"
        return "\n".join(str(item) for item in self._items)


class Displayable(Protocol):
    def display(self) -> str:
        ...

class Scorable(Protocol):
    def score(self) -> float:
        ...

D = TypeVar('D', bound=Displayable)
S = TypeVar('S', bound=Scorable)