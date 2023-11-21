from model import Base
from model import Order


class OrderTranslator:
    count = 0

    def __init__(self):
        print("Data1 Constructor")
        OrderTranslator.count += 1

    def toOrder(self, orderDict):
        order = Order()
        order.customer_id = orderDict["customer_id"]
        return order

    def toOrderDict(self, order):
        orderDict = {}
        orderDict["date"] = order.date.isoformat()
        orderDict["customer_id"] = str(order.customer_id)
        return orderDict

    def toOrdersToList (self, orderList):
        orders = []
        for order in orderList:
            orders.append(self.toOrderDict(order))
        return orders