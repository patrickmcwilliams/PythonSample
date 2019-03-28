from abc import ABC, abstractmethod

# base class if we want to convert to other base systems
class Converter(ABC):
    
    @abstractmethod
    def convert(self, number_to_convert):
        pass
    