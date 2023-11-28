from model import Base
from model import Order

from repositories.order_itemrepository import OrderItemRepository
from translators.order_itemtranslator import OrderItemTranslator
from validators.validator import OrderItemValidator


class OrderItemService:
    repository = None

    def __init__(self):
        OrderItemService.repository = OrderItemRepository()
        OrderItemService.translator = OrderItemTranslator()

    def save(self, orderitemDict):
        OrderItemValidator.validate(self, orderitemDict)
        orderitem = OrderItemService.translator.toOrderItem(orderitemDict)
        return OrderItemService.repository.save(orderitem)

    def delete(self, id):
        OrderItemService.repository.delete(id)

    def findById(self, id):
        orderitem = OrderItemService.repository.findById(id)
        OrderItemValidator.exist(self, orderitem)
        orderitemDict = OrderItemService.translator.toOrderItemDict(orderitem)
        return orderitemDict

    def findByOrder(self, id):
        orderitem = OrderItemService.repository.findByOrder(id)
        OrderItemValidator.exist(self, orderitem)
        orderitemDict = OrderItemService.translator.toOrderItemsToList(orderitem)
        return orderitemDict
    
    def findByProduct(self, id):
        orderitem = OrderItemService.repository.findByProduct(id)
        OrderItemValidator.exist(self, orderitem)
        orderitemDict = OrderItemService.translator.toOrderItemsToList(orderitem)
        return orderitemDict
       
    def findAll():
        orderitems = OrderItemService.repository.findAll()
        orderitemList = OrderItemService.translator.toOrderItemsToList(orderitems)
        return orderitemList

    def update(self, orderitemDict):
        orderitem = OrderItemService.translator.toOrderItemUpdate(orderitemDict)
        OrderItemService.repository.update(orderitem)
