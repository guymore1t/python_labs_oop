import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'lab02'))
from collection import TicketCollection

from base import Ticket
from models import SingleTicket, ReturnTicket

def print_separator(title):
    print("\n" + "=" * 60)
    print(f" {title}")
    print("=" * 60)

def main():
    # 1. Создание объектов разных типов
    print_separator("1. Создание билетов разных типов")
    t1 = SingleTicket("A1", 120.0, 12)
    t2 = SingleTicket("B2", 85.5, 5)
    t3 = ReturnTicket("C3", 150.0, "C4", 100.0)
    t4 = ReturnTicket("A1", 90.0, "A2", 80.0)
    t5 = SingleTicket("B2", 95.0, 8)

    print(t1)
    print(t2)
    print(t3)
    print(t4)
    print(t5)

    # 2. Добавление в коллекцию (она теперь хранит любые Ticket)
    print_separator("2. Добавление в коллекцию")
    coll = TicketCollection()
    tickets = [t1, t2, t3, t4, t5]
    for t in tickets:
        coll.add(t)
        print(f"Добавлен: {t.number} ({type(t).__name__})")

    # 3. Использование методов базового и дочернего классов
    print_separator("3. Продажа и использование")
    t1.sell()
    t1.use()  # SingleTicket.use() выводит место
    t3.sell()
    t3.use()  # Первый раз использует прямой рейс
    t3.use()  # Второй раз – обратный, статус меняется на used
    t4.sell()

    print("\nСостояние после операций:")
    for t in coll:
        print(t)

    # 4. Проверка типов isinstance
    print_separator("4. Проверка типов")
    for t in coll:
        if isinstance(t, SingleTicket):
            print(f"{t.number} – разовый билет")
        elif isinstance(t, ReturnTicket):
            print(f"{t.number} – билет туда-обратно")

    # 5. Полиморфизм: вызов одного метода use() даёт разное поведение
    print_separator("5. Полиморфизм метода use()")
    # Уже видели выше, но добавим комментарии
    # Для SingleTicket: проверка _valid, использование и вывод места
    # Для ReturnTicket: поэтапное использование рейсов
    print("Поведение use() зависит от типа билета (показано ранее).")

    # 6. Специфичные методы дочерних классов
    print_separator("6. Специфичные методы")
    print(f"t1.seat_number = {t1.seat_number}")
    print(f"t1.validate() = {t1.validate()}")  # после use() должно быть False
    print(f"t3.calculate_total_price() = {t3.calculate_total_price()}")

    # 7. Фильтрация по типу (задание на 5)
    print_separator("7. Фильтрация по типу")
    single_list = []
    return_list = []
    for t in coll:
        if isinstance(t, SingleTicket):
            single_list.append(t)
        elif isinstance(t, ReturnTicket):
            return_list.append(t)
    print(f"Разывых билетов: {len(single_list)}")
    for t in single_list:
        print("  ", t)
    print(f"Билетов туда-обратно: {len(return_list)}")
    for t in return_list:
        print("  ", t)

    # 8. Сценарии
    print_separator("8. Сценарии")

    print("\nСценарий А: Обработка только разовых билетов")
    for t in coll:
        if isinstance(t, SingleTicket) and t.status == "available":
            t.sell()
            print(f"Продан {t.number}")

    print("\nСценарий Б: Подсчёт общей стоимости всех билетов (полиморфный метод)")
    total = 0
    for t in coll:
        if isinstance(t, ReturnTicket):
            total += t.calculate_total_price()
        else:
            total += t.price
    print(f"Общая стоимость всех билетов: {total:.2f} руб")

    print("\nСценарий В: Проверка валидности и перепродажа")
    for t in coll:
        if isinstance(t, SingleTicket):
            if not t.validate():
                print(f"{t.number} недействителен, создаём новый такой же")
                new_t = SingleTicket(t.route, t.price, t.seat_number)
                coll.add(new_t)
                print(f"Создан и добавлен {new_t.number}")

    print("\nИтоговое содержимое коллекции:")
    print(coll)

if __name__ == "__main__":
    main()