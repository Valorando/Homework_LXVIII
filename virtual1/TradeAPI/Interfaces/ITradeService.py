from abc import ABC, abstractmethod
from TradeAPI.Models.InputOutputModel import IOModel
from TradeAPI.Models.EditModel import EModel

class ITS(ABC):
    @abstractmethod
    def Get_all_orders(self):
        pass

    @abstractmethod
    def Add_order(self, order: IOModel):
        pass

    @abstractmethod
    def Edit_order(self, order: EModel):
        pass

    @abstractmethod
    def Delete_order(self, order_id: int):
        pass