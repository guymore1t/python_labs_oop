from validate import validate_route, validate_price, validate_status

class Ticket:
    total_tickets = 0

    def __init__(self, route, price):
        validate_route(route)
        validate_price(price)

        self._route = route
        self._price = price
        self._status = "available"
        self._number = f"TICKET-{Ticket.total_tickets + 1}"

        Ticket.total_tickets += 1

    @property
    def route(self):
        return self._route

    @property
    def price(self):
        return self._price

    @property
    def status(self):
        return self._status

    @property
    def number(self):
        return self._number

    @price.setter
    def price(self, new_price):
        validate_price(new_price)
        self._price = new_price

    def __str__(self):
        return f"Билет {self._number}: маршрут {self._route}, цена {self._price} руб., статус {self._status}"

    def __repr__(self):
        return f"Ticket('{self._route}', {self._price})"

    def __eq__(self, other):
        if not isinstance(other, Ticket):
            return False
        return self._number == other._number

    def sell(self):
        if self._status != "available":
            raise ValueError("Нельзя продать билет, который не доступен")
        self._status = "sold"
        print(f"Билет {self._number} продан.")

    def use(self):
        if self._status != "sold":
            raise ValueError("Нельзя использовать непроданный билет")
        self._status = "used"
        print(f"Билет {self._number} использован.")

    def refund(self):
        if self._status != "sold":
            raise ValueError("Нельзя вернуть билет, который не был продан")
        self._status = "available"
        print(f"Билет {self._number} возвращён, теперь доступен.")