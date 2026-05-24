import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'lab01'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'lab03'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'lab06'))

from model import Ticket
from models import SingleTicket, ReturnTicket
from container import TypedCollection
from exceptions import ItemNotFoundError, DuplicateItemError
from storage import save, load
from typing import TypeVar, Callable, Optional, List

T = TypeVar('T', bound=Ticket)

class TicketApp:
    def __init__(self, data_file: Optional[str] = None) -> None:
        self._collection: TypedCollection[Ticket] = TypedCollection()
        self._data_file = data_file
        if data_file:
            self._load_from_file()

    def _load_from_file(self) -> None:
        items = load(self._data_file)
        for item in items:
            try:
                self.add_ticket(item)
            except DuplicateItemError:
                pass

    def add_ticket(self, ticket: Ticket) -> None:
        if self._collection.find_by_number(ticket.number) is not None:
            raise DuplicateItemError(f"Билет с номером {ticket.number} уже существует")
        self._collection.add(ticket)

    def remove_ticket(self, number: str) -> Ticket:
        ticket = self._collection.find_by_number(number)
        if ticket is None:
            raise ItemNotFoundError(f"Билет с номером {number} не найден")
        self._collection.remove(ticket)
        return ticket

    def get_all_tickets(self) -> List[Ticket]:
        return self._collection.get_all()

    def find_by_number(self, number: str) -> Optional[Ticket]:
        return self._collection.find_by_number(number)

    def filter_by_status(self, status: str) -> List[Ticket]:
        return self._collection.filter(lambda t: t.status == status)

    def sort_by(self, key_func: Callable[[Ticket], object]) -> None:
        self._collection.sort_by(key_func)

    def save_to_file(self) -> None:
        if self._data_file:
            save(self._collection, self._data_file)