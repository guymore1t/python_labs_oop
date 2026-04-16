import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'lab01'))
from model import Ticket
from collection import TicketCollection

def print_separator(title):
    print("\n" + "=" * 60)
    print(f" {title}")
    print("=" * 60)

def main():
    print_separator("1. Создание билетов")
    t1 = Ticket("A1", 120.0)
    t2 = Ticket("B2", 85.5)
    t3 = Ticket("A1", 120.0)
    t4 = Ticket("C3", 200.0)
    t5 = Ticket("B2", 95.0)

    print(t1)
    print(t2)
    print(t3)
    print(t4)
    print(t5)

    print_separator("2. Добавление в коллекцию")
    coll = TicketCollection()
    tickets = [t1, t2, t3, t4, t5]
    for t in tickets:
        try:
            coll.add(t)
            print(f"Добавлен: {t.number} ({t.route})")
        except ValueError as e:
            print(f"Ошибка: {e}")

    print("\nПопытка добавить дубликат:")
    duplicate = Ticket("D4", 50.0)
    duplicate._number = t1.number
    try:
        coll.add(duplicate)
    except ValueError as e:
        print(f"Ошибка: {e}")

    print_separator("3. Вывод всех билетов")
    print(coll)

    print_separator("4. Изменение статусов")
    t1.sell()
    t2.sell()
    t2.use()
    t4.sell()
    t4.refund()
    print("\nПосле изменений:")
    print(coll)

    print_separator("5. Поиск")
    print("Поиск по номеру TICKET-1:", coll.find_by_number("TICKET-1"))
    print("\nПоиск по маршруту A1:")
    for t in coll.find_by_route("A1"):
        print("  ", t)
    print("\nПоиск по статусу sold:")
    for t in coll.find_by_status("sold"):
        print("  ", t)
    print("\nПоиск по цене от 100 до 150:")
    for t in coll.find_by_price_range(100, 150):
        print("  ", t)

    print_separator("6. Длина и итерация")
    print(f"Всего билетов: {len(coll)}")
    print("Перебор через for:")
    for t in coll:
        print(f"  - {t.number} | {t.route} | {t.price:.2f} руб | {t.status}")

    print_separator("7. Индексация")
    if len(coll) >= 3:
        print(f"Первый билет: {coll[0].number}")
        print(f"Третий билет: {coll[2].number}")

    print_separator("8. Сортировка")
    print("По цене:")
    coll.sort_by_price()
    for t in coll:
        print(f"  {t.price:.2f} руб - {t.number}")
    print("\nПо маршруту:")
    coll.sort_by_route()
    for t in coll:
        print(f"  {t.route} - {t.number}")
    print("\nПо статусу:")
    coll.sort_by_status()
    for t in coll:
        print(f"  {t.status} - {t.number}")

    print_separator("9. Фильтрация")
    available = coll.get_available()
    print("Доступные билеты:")
    print(available)
    sold = coll.get_sold()
    print("\nПроданные билеты:")
    print(sold)
    used = coll.get_used()
    print("\nИспользованные билеты:")
    print(used)
    route_a1 = coll.get_by_route("A1")
    print("\nБилеты маршрута A1:")
    print(route_a1)
    expensive = coll.get_expensive(100)
    print("\nБилеты дороже 100 руб:")
    print(expensive)

    print_separator("10. Удаление")
    print("Удаляем билет TICKET-3")
    coll.remove(t3)
    print(f"Осталось {len(coll)} билетов")
    print("Удаляем первый билет по индексу")
    removed = coll.remove_at(0)
    print(f"Удалён: {removed.number}")
    print(f"Теперь в коллекции {len(coll)} билетов:")
    print(coll)

    print_separator("11. Сценарии")

    print("\nСценарий А: Отчёт по маршрутам")
    routes = []
    for t in coll:
        if t.route not in routes:
            routes.append(t.route)
    for route in routes:
        count = 0
        total = 0
        for t in coll:
            if t.route == route:
                count += 1
                total += t.price
        print(f"Маршрут {route}: {count} билетов, сумма {total:.2f} руб")

    print("\nСценарий Б: Анализ продаж")
    sold_count = 0
    sold_sum = 0
    used_count = 0
    for t in coll:
        if t.status == "sold":
            sold_count += 1
            sold_sum += t.price
        elif t.status == "used":
            used_count += 1
    print(f"Продано: {sold_count} билетов")
    print(f"Использовано: {used_count} билетов")
    if sold_count > 0:
        print(f"Средняя цена проданного: {sold_sum/sold_count:.2f} руб")

    print("\nСценарий В: Скидка на дорогие билеты")
    print("Билеты дороже 150 руб:")
    expensive_list = []
    for t in coll:
        if t.price > 150:
            expensive_list.append(t)
            print("  ", t)
    if len(expensive_list) > 0:
        print("Применяем скидку 20%")
        for t in expensive_list:
            t.price = t.price * 0.8
        print("После скидки:")
        for t in expensive_list:
            print("  ", t)
    else:
        print("  Нет билетов дороже 150 руб")

if __name__ == "__main__":
    main()