# lab04/demo.py
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'lab01'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'lab02'))
from collection import TicketCollection

from interfaces import Printable, Comparable
from models import BaseTicket, SingleTicket, ReturnTicket

def print_separator(title):
    print("\n" + "=" * 60)
    print(f" {title}")
    print("=" * 60)

def print_all(items):
    for item in items:
        if isinstance(item, Printable):
            print(item.to_string())
        else:
            print(item)

def get_printable(collection):
    result = []
    for item in collection:
        if isinstance(item, Printable):
            result.append(item)
    return result

def get_comparable(collection):
    result = []
    for item in collection:
        if isinstance(item, Comparable):
            result.append(item)
    return result

def get_sorted_by_compare(collection):
    items = []
    for item in collection:
        items.append(item)
    n = len(items)
    for i in range(n):
        for j in range(0, n - i - 1):
            if items[j].compare_to(items[j + 1]) > 0:
                items[j], items[j + 1] = items[j + 1], items[j]
    return items

def main():
    print_separator("1. Создание билетов разных типов")
    t1 = SingleTicket("A1", 120.0, 12)
    t2 = SingleTicket("B2", 85.5, 5)
    t3 = ReturnTicket("C3", 150.0, "C4", 100.0)
    t4 = ReturnTicket("A1", 90.0, "A2", 80.0)
    t5 = SingleTicket("B2", 95.0, 8)

    print(t1.to_string())
    print(t2.to_string())
    print(t3.to_string())
    print(t4.to_string())
    print(t5.to_string())

    print_separator("2. Добавление в коллекцию (из ЛР-2)")
    coll = TicketCollection()
    for t in [t1, t2, t3, t4, t5]:
        coll.add(t)
        print(f"Добавлен: {t.number}")

    print_separator("3. Вывод через интерфейс Printable")
    print_all(coll)

    print_separator("4. Сравнение через compare_to()")
    print(f"t1.compare_to(t2) = {t1.compare_to(t2)}")
    print(f"t2.compare_to(t1) = {t2.compare_to(t1)}")
    print(f"t3.compare_to(t4) = {t3.compare_to(t4)}")

    print_separator("5. Сортировка через Comparable (без изменения коллекции)")
    sorted_tickets = get_sorted_by_compare(coll)
    print("Отсортированный список:")
    print_all(sorted_tickets)

    print_separator("6. Проверка isinstance на интерфейсы")
    for t in coll:
        if isinstance(t, Printable):
            print(f"{t.number} реализует Printable")
        if isinstance(t, Comparable):
            print(f"{t.number} реализует Comparable")

    print_separator("7. Фильтрация по интерфейсу")
    printable_tickets = get_printable(coll)
    print(f"Объектов с Printable: {len(printable_tickets)}")
    comparable_tickets = get_comparable(coll)
    print(f"Объектов с Comparable: {len(comparable_tickets)}")

    print_separator("8. Сценарии")
    print("\nСценарий А: Вывод всех билетов через Printable")
    print_all(coll)

    print("\nСценарий Б: Сортировка билетов через Comparable")
    sorted_tickets = get_sorted_by_compare(coll)
    print_all(sorted_tickets)

    print("\nСценарий В: Фильтрация только разовых билетов и их сравнение")
    singles = []
    for t in coll:
        if isinstance(t, SingleTicket):
            singles.append(t)
    for t in singles:
        print(t.to_string())
    if len(singles) >= 2:
        print(f"Сравнение {singles[0].number} и {singles[1].number}: {singles[0].compare_to(singles[1])}")

if __name__ == "__main__":
    main()