import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'lab01'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'lab03'))

from model import Ticket
from models import SingleTicket, ReturnTicket
from container import TypedCollection, D, S

def main():
    coll: TypedCollection[Ticket] = TypedCollection()

    t1 = SingleTicket("A1", 120.0, 12)
    t2 = ReturnTicket("B2", 85.5, "B3", 60.0)
    t3 = SingleTicket("C3", 200.0, 7)

    coll.add(t1)
    coll.add(t2)
    coll.add(t3)

    print("=== Все билеты ===")
    for t in coll:
        print(t.display())

    print("\n=== find (по номеру) ===")
    found = coll.find(lambda t: t.number == "TICKET-1")
    print(found.display() if found else "не найден")

    print("\n=== filter (дороже 100) ===")
    expensive = coll.filter(lambda t: t.price > 100)
    for t in expensive:
        print(t.display())

    print("\n=== map: список цен ===")
    prices = coll.map(lambda t: t.price)
    print(prices)

    print("\n=== map: информация о билетах ===")
    info = coll.map(lambda t: f"{t.number}: {t.route} - {t.price}р")
    for line in info:
        print(line)

    print("\n=== Коллекция Displayable объектов ===")
    display_coll: TypedCollection[D] = TypedCollection()
    display_coll.add(t1)
    display_coll.add(t2)
    display_coll.add(t3)
    for obj in display_coll:
        print(obj.display())

    print("\n=== Коллекция Scorable объектов ===")
    score_coll: TypedCollection[S] = TypedCollection()
    score_coll.add(t1)
    score_coll.add(t2)
    score_coll.add(t3)
    for obj in score_coll:
        print(f"score = {obj.score()}")

    print("\n=== filter по протоколу (score < 150) ===")
    cheap = score_coll.filter(lambda obj: obj.score() < 150)
    for obj in cheap:
        print(f"{obj.display()} (score: {obj.score()})")

if __name__ == "__main__":
    main()