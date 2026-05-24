import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'lab01'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'lab03'))

from typing import Callable, List
from app import TicketApp
from model import Ticket
from models import SingleTicket, ReturnTicket
from exceptions import ItemNotFoundError, DuplicateItemError

def print_menu() -> None:
    print("\n=== Управление билетами ===")
    print("1. Добавить билет")
    print("2. Показать все билеты")
    print("3. Найти билет по номеру")
    print("4. Удалить билет")
    print("5. Фильтрация по статусу")
    print("6. Сортировка")
    print("7. Сохранить в файл")
    print("0. Выход")

def input_int(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Ошибка: введите целое число")

def input_float(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка: введите число")

def add_ticket_flow(app: TicketApp) -> None:
    print("\nТип билета:")
    print("1. Разовый (SingleTicket)")
    print("2. Туда-обратно (ReturnTicket)")
    ttype = input_int("Выберите тип: ")
    if ttype == 1:
        route = input("Маршрут: ")
        price = input_float("Цена: ")
        seat = input_int("Номер места: ")
        ticket = SingleTicket(route, price, seat)
    elif ttype == 2:
        route = input("Прямой маршрут: ")
        price = input_float("Цена прямого: ")
        ret_route = input("Обратный маршрут: ")
        ret_price = input_float("Цена обратного: ")
        ticket = ReturnTicket(route, price, ret_route, ret_price)
    else:
        print("Неверный тип.")
        return
    try:
        app.add_ticket(ticket)
        print(f"Добавлен билет: {ticket.number}")
    except DuplicateItemError as e:
        print(f"Ошибка: {e}")

def remove_ticket_flow(app: TicketApp) -> None:
    number = input("Введите номер билета: ")
    ticket = app.find_by_number(number)
    if ticket is None:
        print(f"Билет с номером {number} не найден.")
        return
    confirm = input(f"Удалить {ticket}? (y/n): ").lower()
    if confirm == "y":
        try:
            app.remove_ticket(number)
            print("Билет удалён.")
        except ItemNotFoundError:
            print("Ошибка удаления.")
    else:
        print("Отмена.")

def show_all_tickets(app: TicketApp) -> None:
    tickets = app.get_all_tickets()
    if not tickets:
        print("Коллекция пуста.")
        return
    for t in tickets:
        print(t.display())

def filter_flow(app: TicketApp) -> None:
    print("\nДоступные статусы: available, sold, used")
    status = input("Введите статус: ").strip()
    result = app.filter_by_status(status)
    if not result:
        print("Ничего не найдено.")
    else:
        for t in result:
            print(t.display())

def sort_flow(app: TicketApp) -> None:
    print("\nКритерии сортировки:")
    print("1. По цене")
    print("2. По маршруту")
    print("3. По статусу")
    choice = input_int("Выберите: ")
    if choice == 1:
        app.sort_by(lambda t: t.price)
    elif choice == 2:
        app.sort_by(lambda t: t.route)
    elif choice == 3:
        order = {"available": 0, "sold": 1, "used": 2}
        app.sort_by(lambda t: order[t.status])
    else:
        print("Неверный выбор.")
        return
    print("Сортировка выполнена. Используйте пункт 2 для просмотра.")

def run_cli(app: TicketApp) -> None:
    while True:
        print_menu()
        choice = input_int("Ваш выбор: ")
        if choice == 1:
            add_ticket_flow(app)
        elif choice == 2:
            show_all_tickets(app)
        elif choice == 3:
            number = input("Введите номер билета: ")
            ticket = app.find_by_number(number)
            if ticket:
                print(ticket.display())
            else:
                print("Билет не найден.")
        elif choice == 4:
            remove_ticket_flow(app)
        elif choice == 5:
            filter_flow(app)
        elif choice == 6:
            sort_flow(app)
        elif choice == 7:
            app.save_to_file()
            print("Данные сохранены.")
        elif choice == 0:
            print("Выход...")
            break
        else:
            print("Неверный пункт меню.")