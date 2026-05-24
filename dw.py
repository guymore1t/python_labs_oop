from abc import ABC, abstractmethod

class Fleet:
    def __init__(self, cars=None):
        self._cars = []
        if cars:
            for c in cars:
                self.add(c)

    def add(self, car):
        if not isinstance(car, Car):
            raise TypeError("нужен Car")
        for c in self._cars:
            if c.plate == car.plate:
                raise ValueError("такой номер уже есть")
        self._cars.append(car)

    def __iter__(self):
        return iter(self._cars)

    def __len__(self):
        return len(self._cars)

    def filter_by(self, predicate):
        new_fleet = Fleet()
        for car in self._cars:
            if predicate(car):
                new_fleet.add(car)
        return new_fleet

    def sort_by(self, key_func):
        return Fleet(sorted(self._cars, key=key_func))

    def estimate_trip(self, strategy, distance_km):
        out = {}
        for car in self._cars:
            out[car.plate] = strategy.calculate(car, distance_km)
        return out


def make_speed_filter(min_sp, max_sp):
    def f(car):
        return min_sp <= car.max_speed <= max_sp
    return f

def make_fuel_filter(min_fuel):
    def f(car):
        return car.fuel_level >= min_fuel
    return f

def make_model_filter(substr):
    def f(car):
        return substr.lower() in car.model.lower()
    return f


class TripCostStrategy(ABC):
    @abstractmethod
    def calculate(self, car, distance_km):
        pass

class FlatRate(TripCostStrategy):
    def __init__(self, rate_per_km):
        self.rate = rate_per_km
    def calculate(self, car, distance_km):
        return self.rate * distance_km

class FuelBased(TripCostStrategy):
    def __init__(self, price_per_litre, consumption_per_100km):
        self.price = price_per_litre
        self.consumption = consumption_per_100km
    def calculate(self, car, distance_km):
        litres = (distance_km / 100.0) * self.consumption
        return litres * self.price

class SpeedBased(TripCostStrategy):
    def __init__(self, base_rate, speed_coef):
        self.base = base_rate
        self.coef = speed_coef
    def calculate(self, car, distance_km):
        return self.base * distance_km + self.coef * car.max_speed


