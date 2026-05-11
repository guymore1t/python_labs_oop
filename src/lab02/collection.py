import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'lab01'))
from model import Ticket

class TicketCollection:
    def __init__(self):
        self._items = []

    def add(self, ticket):
        if not isinstance(ticket, Ticket):
            raise TypeError("В коллекцию можно добавлять только объекты Ticket")
        for t in self._items:
            if t.number == ticket.number:
                raise ValueError(f"Билет с номером {ticket.number} уже существует в коллекции")
        self._items.append(ticket)

    def remove(self, ticket):
        if ticket not in self._items:
            raise ValueError("Билет не найден в коллекции")
        self._items.remove(ticket)

    def get_all(self):
        return self._items.copy()

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        return iter(self._items)
    
    def __getitem__(self, index):
        return self._items[index]

    def remove_at(self, index):
        if index < 0 or index >= len(self._items):
            raise IndexError("Индекс вне диапазона")
        return self._items.pop(index)

    def find_by_number(self, number):
        for ticket in self._items:
            if ticket.number == number:
                return ticket
        return None

    def find_by_route(self, route):
        result = []
        for ticket in self._items:
            if ticket.route == route:
                result.append(ticket)
        return result

    def find_by_status(self, status):
        result = []
        for ticket in self._items:
            if ticket.status == status:
                result.append(ticket)
        return result

    def find_by_price_range(self, min_price, max_price):
        result = []
        for ticket in self._items:
            if min_price <= ticket.price <= max_price:
                result.append(ticket)
        return result

    def sort_by_price(self):
        self._items.sort(key=lambda t: t.price)

    def sort_by_route(self):
        self._items.sort(key=lambda t: t.route)

    def sort_by_status(self):
        order = {"available": 0, "sold": 1, "used": 2}
        self._items.sort(key=lambda t: order[t.status])

    def get_available(self):
        new_coll = TicketCollection()
        for ticket in self._items:
            if ticket.status == "available":
                new_coll.add(ticket)
        return new_coll

    def get_sold(self):
        new_coll = TicketCollection()
        for ticket in self._items:
            if ticket.status == "sold":
                new_coll.add(ticket)
        return new_coll

    def get_used(self):
        new_coll = TicketCollection()
        for ticket in self._items:
            if ticket.status == "used":
                new_coll.add(ticket)
        return new_coll

    def get_by_route(self, route):
        new_coll = TicketCollection()
        for ticket in self._items:
            if ticket.route == route:
                new_coll.add(ticket)
        return new_coll

    def get_expensive(self, threshold):
        new_coll = TicketCollection()
        for ticket in self._items:
            if ticket.price > threshold:
                new_coll.add(ticket)
        return new_coll

    def __str__(self):
        if not self._items:
            return "Коллекция пуста"
        s = ""
        for ticket in self._items:
            s += str(ticket) + "\n"
        return s.strip()