import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'lab03'))
from models import SingleTicket

def by_price(ticket):
    return ticket.price

def by_route(ticket):
    return ticket.route

def by_status_order(ticket):
    order = {"available": 0, "sold": 1, "used": 2}
    return order[ticket.status]

def is_available(ticket):
    return ticket.status == "available"

def is_single_ticket(ticket):
    return isinstance(ticket, SingleTicket)

def make_price_filter(max_price):
    def filter_fn(ticket):
        return ticket.price <= max_price
    return filter_fn

class DiscountStrategy:
    def __call__(self, ticket):
        ticket.price = ticket.price * 0.9