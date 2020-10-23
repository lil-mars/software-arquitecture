from abc import ABC, abstractmethod
 
class WorkShop(ABC):

    @abstractmethod
    def work(self):
        pass