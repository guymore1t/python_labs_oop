import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'lab01'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'lab02'))
from model import Ticket
from collection import TicketCollection

class ExtendedTicketCollection(TicketCollection):
    def sort_by(self, key_func):
        self._items.sort(key=key_func)
        return self

    def filter_by(self, predicate):
        new_coll = ExtendedTicketCollection()
        for item in self._items:
            if predicate(item):
                new_coll.add(item)
        return new_coll

    def apply(self, func):
        for item in self._items:
            func(item)
        return self