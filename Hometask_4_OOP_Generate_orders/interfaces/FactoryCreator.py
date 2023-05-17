from abc import ABC, abstractmethod

class FactoryCreator(ABC):    

    @abstractmethod
    def generate_value(self, context) -> str:
        pass