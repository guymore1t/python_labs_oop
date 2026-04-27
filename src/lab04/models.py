import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'lab01'))
from model import Ticket

from interfaces import Printable, Comparable

class BaseTicket(Ticket, Printable, Comparable):
    def to_string(self):
        return str(self)

    def compare_to(self, other):
        if not isinstance(other, Ticket):
            raise TypeError("Сравнение возможно только с объектами Ticket")
        if self.price < other.price:
            return -1
        elif self.price > other.price:
            return 1
        else:
            return 0

class SingleTicket(BaseTicket):
    def __init__(self, route, price, seat_number):
        super().__init__(route, price)
        self._seat_number = seat_number
        self._valid = True

    @property
    def seat_number(self):
        return self._seat_number

    def validate(self):
        return self._valid and self._status != "used"

    def use(self):
        if self._status != "sold":
            raise ValueError("Нельзя использовать непроданный билет")
        if not self._valid:
            raise ValueError("Билет недействителен")
        self._status = "used"
        self._valid = False
        print(f"Билет {self._number} использован. Место {self._seat_number}.")

    def to_string(self):
        return (f"Разовый билет {self._number}: маршрут {self._route}, "
                f"место {self._seat_number}, цена {self._price} руб., "
                f"статус {self._status}, действителен: {self._valid}")

    def compare_to(self, other):
        if not isinstance(other, Ticket):
            raise TypeError("Сравнение только с Ticket")
        price_cmp = super().compare_to(other)
        if price_cmp != 0:
            return price_cmp
        if isinstance(other, SingleTicket):
            if self._seat_number < other._seat_number:
                return -1
            elif self._seat_number > other._seat_number:
                return 1
        return 0

class ReturnTicket(BaseTicket):
    def __init__(self, route, price, return_route, return_price):
        super().__init__(route, price)
        self._return_route = return_route
        self._return_price = return_price
        self._outbound_used = False
        self._return_used = False

    @property
    def return_route(self):
        return self._return_route

    @property
    def return_price(self):
        return self._return_price

    def use(self):
        if self._status != "sold":
            raise ValueError("Нельзя использовать непроданный билет")
        if not self._outbound_used:
            self._outbound_used = True
            print(f"Билет {self._number}: использован прямой рейс {self._route}.")
        elif not self._return_used:
            self._return_used = True
            self._status = "used"
            print(f"Билет {self._number}: использован обратный рейс {self._return_route}. Билет использован полностью.")
        else:
            raise ValueError("Оба рейса уже использованы")

    def calculate_total_price(self):
        return self._price + self._return_price

    def to_string(self):
        return (f"Билет туда-обратно {self._number}: маршрут {self._route} -> {self._return_route}, "
                f"цена {self._price}+{self._return_price} руб., статус {self._status}, "
                f"прямой использован: {self._outbound_used}, обратный использован: {self._return_used}")

    def compare_to(self, other):
        if not isinstance(other, Ticket):
            raise TypeError("Сравнение только с Ticket")
        self_total = self.calculate_total_price()
        if isinstance(other, ReturnTicket):
            other_total = other.calculate_total_price()
        else:
            other_total = other.price
        if self_total < other_total:
            return -1
        elif self_total > other_total:
            return 1
        else:
            return 0