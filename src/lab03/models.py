from base import Ticket

class SingleTicket(Ticket):
    def __init__(self, route, price, seat_number):
        super().__init__(route, price)
        self._seat_number = seat_number
        self._valid = True

    @property
    def seat_number(self):
        return self._seat_number

    def use(self):
        if self._status != "sold":
            raise ValueError("Нельзя использовать непроданный билет")
        if not self._valid:
            raise ValueError("Билет уже использован или недействителен")
        self._status = "used"
        self._valid = False
        print(f"Билет {self._number} использован. Место {self._seat_number}.")

    def validate(self):
        return self._valid and self._status != "used"

    def __str__(self):
        return (f"Разовый билет {self._number}: маршрут {self._route}, "
                f"место {self._seat_number}, цена {self._price} руб., статус {self._status}, "
                f"действителен: {self._valid}")


class ReturnTicket(Ticket):
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

    def __str__(self):
        return (f"Билет туда-обратно {self._number}: маршрут {self._route} -> {self._return_route}, "
                f"цена {self._price}+{self._return_price} руб., статус {self._status}, "
                f"прямой использован: {self._outbound_used}, обратный использован: {self._return_used}")