from abc import ABC,abstractmethod

class Entity(ABC):

    @abstractmethod
    def movement(self):
        pass

    @abstractmethod
    def update(self):
        pass
