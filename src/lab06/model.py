import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'lab01'))
from validate import validate_route, validate_price, validate_status

class Ticket:
    total_tickets: int = 0

    def __init__(self, route: str, price: float) -> None:
        validate_route(route)
        validate_price(price)

        self._route: str = route
        self._price: float = price
        self._status: str = "available"
        self._number: str = f"TICKET-{Ticket.total_tickets + 1}"

        Ticket.total_tickets += 1

    @property
    def route(self) -> str:
        return self._route

    @property
    def price(self) -> float:
        return self._price

    @property
    def status(self) -> str:
        return self._status

    @property
    def number(self) -> str:
        return self._number

    @price.setter
    def price(self, new_price: float) -> None:
        validate_price(new_price)
        self._price = new_price

    def sell(self) -> None:
        if self._status != "available":
            raise ValueError("Нельзя продать билет, который не доступен")
        self._status = "sold"
        print(f"Билет {self._number} продан.")

    def use(self) -> None:
        if self._status != "sold":
            raise ValueError("Нельзя использовать непроданный билет")
        self._status = "used"
        print(f"Билет {self._number} использован.")

    def refund(self) -> None:
        if self._status != "sold":
            raise ValueError("Нельзя вернуть билет, который не был продан")
        self._status = "available"
        print(f"Билет {self._number} возвращён, теперь доступен.")

    def display(self) -> str:
        return str(self)

    def score(self) -> float:
        return self._price

    def __str__(self) -> str:
        return f"Билет {self._number}: маршрут {self._route}, цена {self._price} руб., статус {self._status}"

    def __repr__(self) -> str:
        return f"Ticket('{self._route}', {self._price})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Ticket):
            return False
        return self._number == other._number

    def __hash__(self) -> int:
        return hash(self._number)