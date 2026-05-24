import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'lab01'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'lab03'))

import json
from typing import Any
from model import Ticket
from models import SingleTicket, ReturnTicket

def ticket_to_dict(ticket: Any) -> dict[str, Any]:
    data: dict[str, Any] = {
        "type": type(ticket).__name__,
        "route": ticket.route,
        "price": ticket.price,
        "number": ticket.number,
        "status": ticket.status,
    }
    if isinstance(ticket, SingleTicket):
        data["seat_number"] = ticket.seat_number
        data["valid"] = ticket._valid
    elif isinstance(ticket, ReturnTicket):
        data["return_route"] = ticket.return_route
        data["return_price"] = ticket.return_price
        data["outbound_used"] = ticket._outbound_used
        data["return_used"] = ticket._return_used
    return data

def ticket_from_dict(data: dict[str, Any]) -> Any:
    ticket_type = data["type"]
    if ticket_type == "SingleTicket":
        ticket = SingleTicket(data["route"], data["price"], data["seat_number"])
        ticket._valid = data.get("valid", True)
    elif ticket_type == "ReturnTicket":
        ticket = ReturnTicket(data["route"], data["price"], data["return_route"], data["return_price"])
        ticket._outbound_used = data.get("outbound_used", False)
        ticket._return_used = data.get("return_used", False)
    else:
        ticket = Ticket(data["route"], data["price"])
    ticket._number = data["number"]
    ticket._status = data["status"]
    return ticket

def save(collection: Any, filepath: str) -> None:
    items = [ticket_to_dict(t) for t in collection]
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(items, f, ensure_ascii=False, indent=2)

def load(filepath: str) -> list[Any]:
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
        return [ticket_from_dict(d) for d in data]
    except FileNotFoundError:
        return []