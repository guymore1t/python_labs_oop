# lab05/demo.py
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'lab01'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'lab03'))
from model import Ticket
from models import SingleTicket, ReturnTicket
from ext_collection import ExtendedTicketCollection
from strategies import (by_price, by_route, by_status_order,
                        is_available, is_single_ticket,
                        make_price_filter, DiscountStrategy)

def print_sep(title):
    print("\n" + "=" * 50)
    print(" " + title)
    print("=" * 50)

def show_collection(coll, msg="Коллекция:"):
    print(msg)
    if len(coll) == 0:
        print("  (пусто)")
    for t in coll:
        print("  ", t)

def main():
    print_sep("1. Создание билетов")
    t1 = SingleTicket("A1", 120.0, 12)
    t2 = SingleTicket("B2", 85.5, 5)
    t3 = ReturnTicket("C3", 150.0, "C4", 100.0)
    t4 = ReturnTicket("A1", 90.0, "A2", 80.0)
    t5 = SingleTicket("B2", 95.0, 8)
    tickets = [t1, t2, t3, t4, t5]
    for t in tickets:
        print(t)

    coll = ExtendedTicketCollection()
    for t in tickets:
        coll.add(t)

    print_sep("2. Сортировка тремя стратегиями")
    coll.sort_by(by_price)
    show_collection(coll, "Сортировка по цене:")

    coll.sort_by(by_route)
    show_collection(coll, "Сортировка по маршруту:")

    t2.sell()
    t3.sell()
    coll.sort_by(by_status_order)
    show_collection(coll, "Сортировка по статусу:")

    print_sep("3. Фильтрация двумя фильтрами")
    print("Доступные билеты (is_available):")
    avail = coll.filter_by(is_available)
    show_collection(avail)

    print("\nТолько разовые билеты (is_single_ticket):")
    singles = coll.filter_by(is_single_ticket)
    show_collection(singles)

    cheap_filter = make_price_filter(100.0)
    print("\nБилеты с ценой <= 100 (make_price_filter):")
    cheap = coll.filter_by(cheap_filter)
    show_collection(cheap)

    print_sep("4. map() - преобразование")
    info_list = list(map(lambda t: f"{t.number}: {t.price} руб", coll))
    print("Информация о билетах (номер: цена):")
    for info in info_list:
        print("  ", info)

    discounted_prices = list(map(lambda t: round(t.price * 0.9, 2), coll))
    print("\nЦены после скидки 10% (исходные не меняются):")
    for i, t in enumerate(coll):
        print(f"  {t.number}: было {t.price} -> стало {discounted_prices[i]}")

    print_sep("5. Паттерн Стратегия: callable-объект")
    discount = DiscountStrategy()
    copy_coll = ExtendedTicketCollection()
    for t in coll:
        copy_coll.add(t)
    print("До скидки:")
    show_collection(copy_coll)
    copy_coll.apply(discount)
    print("\nПосле применения DiscountStrategy (10%):")
    show_collection(copy_coll)

    print_sep("6. Цепочка операций на новой коллекции")
    # Создаём свежие билеты, чтобы они были available
    f1 = SingleTicket("A1", 120.0, 12)
    f2 = SingleTicket("B2", 85.5, 5)
    f3 = ReturnTicket("C3", 150.0, "C4", 100.0)
    fresh = ExtendedTicketCollection()
    fresh.add(f1)
    fresh.add(f2)
    fresh.add(f3)
    f1.sell()
    f2.sell()
    print("Исходная коллекция:")
    show_collection(fresh)

    result = (fresh
              .filter_by(is_available)
              .sort_by(by_price)
              .apply(discount))
    print("\nПосле цепочки filter_by(available) -> sort_by(price) -> apply(10%):")
    show_collection(result)

    print_sep("7. Сценарии")
    scene = ExtendedTicketCollection()
    s1 = SingleTicket("D1", 50.0, 1)
    s2 = SingleTicket("D2", 30.0, 2)
    s3 = ReturnTicket("E1", 100.0, "E2", 70.0)
    scene.add(s1)
    scene.add(s2)
    scene.add(s3)

    print("Сортировка по маршруту:")
    scene.sort_by(by_route)
    show_collection(scene)

    print("Сортировка по цене:")
    scene.sort_by(by_price)
    show_collection(scene)

if __name__ == "__main__":
    main()