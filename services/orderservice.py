from model import Base
from model import Order

from repositories.orderrepository import OrderRepository
from translators.ordertranslator import OrderTranslator
from validators.validator import OrderValidator

class OrderService:
    repository = None

    def __init__(self):
        OrderService.repository = OrderRepository()
        OrderService.translator = OrderTranslator()
        OrderService.validator = OrderValidator()

    def save(self, orderDict):
        OrderValidator.validate(self, orderDict)
        order = OrderService.translator.toOrder(orderDict)
        return OrderService.repository.save(order)

    def delete(self, id):
        OrderService.repository.delete(id)

    def findById(self, id):
        order = OrderService.repository.findById(id)
        OrderValidator.exist(self, order)
        orderDict = OrderService.translator.toOrderDict(order)
        return orderDict

    def findAll():
        orders = OrderService.repository.findAll()
        orderList = OrderService.translator.toOrdersToList(orders)
        return orderList