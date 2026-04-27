from abc import ABC, abstractmethod

class Printable(ABC):
    @abstractmethod
    def to_string(self):
        pass

class Comparable(ABC):
    @abstractmethod
    def compare_to(self, other):
        pass