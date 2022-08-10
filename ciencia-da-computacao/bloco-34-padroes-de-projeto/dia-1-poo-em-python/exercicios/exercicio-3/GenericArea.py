from abc import ABC, abstractmethod

class GenericArea(ABC):
    @abstractmethod
    def area(self):
        raise NotImplemented

    @abstractmethod
    def perimeter(self):
        raise NotImplemented