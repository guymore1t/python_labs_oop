from model import Ticket

def main():
    print("=== Демонстрация работы класса Ticket ===\n")

    try:
        t1 = Ticket("15А", 350.0)
        t2 = Ticket("22", 120.5)
        print("Созданы билеты:")
        print(t1)
        print(t2)
    except ValueError as e:
        print("Ошибка при создании:", e)
        return

    print("\n--- Сравнение билетов ---")
    print(f"t1 == t2? {t1 == t2}")
    t3 = Ticket("15А", 350.0)
    print(f"t1 == t3? {t1 == t3} (разные номера)")

    print("\n--- Атрибут класса ---")
    print(f"Всего создано билетов: {Ticket.total_tickets}")
    print(f"Доступ через экземпляр t1: {t1.total_tickets}")

    print("\n--- Изменение цены через setter ---")
    print(f"Старая цена t1: {t1.price}")
    t1.price = 400.0
    print(f"Новая цена t1: {t1.price}")

    try:
        t1.price = -100
    except ValueError as e:
        print(f"Ошибка при установке цены: {e}")

    print("\n=== Сценарий 1: Продажа и использование ===")
    try:
        t1.sell()
        t1.use()
    except ValueError as e:
        print("Ошибка:", e)

    print("\n=== Сценарий 2: Продажа и возврат ===")
    try:
        t2.sell()
        t2.refund()
        t2.sell()
        print(t2)
    except ValueError as e:
        print("Ошибка:", e)

    print("\n=== Сценарий 3: Некорректные операции ===")
    try:
        t3 = Ticket("10", 500)
        print(t3)
        t3.use()
    except ValueError as e:
        print("Ошибка при использовании:", e)

    try:
        t2.sell()
    except ValueError as e:
        print("Ошибка при повторной продаже:", e)

    print("\n=== Некорректное создание ===")
    try:
        t_invalid = Ticket("", 100)
    except ValueError as e:
        print("Ошибка (пустой маршрут):", e)

    try:
        t_invalid = Ticket("15", -50)
    except ValueError as e:
        print("Ошибка (отрицательная цена):", e)

if __name__ == "__main__":
    main()