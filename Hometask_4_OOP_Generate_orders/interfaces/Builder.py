from abc import ABC, abstractmethod

class Builder(ABC):
    @abstractmethod
    def setup_builder(self):
        pass

    @abstractmethod
    def get_ready_order(self):
        pass

