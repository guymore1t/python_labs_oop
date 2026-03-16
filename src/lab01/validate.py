def validate_route(route):
    if not isinstance(route, str):
        raise ValueError("Маршрут должен быть строкой")
    if route.strip() == "":
        raise ValueError("Маршрут не может быть пустым")

def validate_price(price):
    if not isinstance(price, (int, float)):
        raise ValueError("Цена должна быть числом")
    if price <= 0:
        raise ValueError("Цена должна быть положительной")

def validate_status(status):
    if status not in ["available", "sold", "used"]:
        raise ValueError("Статус должен быть 'available', 'sold' или 'used'")