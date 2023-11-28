from model import Base
from model import OrderItem


class OrderItemTranslator:
    count = 0

    def __init__(self):
        print("Data1 Constructor")
        OrderItemTranslator.count += 1

    def toOrderItem(self, orderitemDict):
        orderitem = OrderItem()
        orderitemDict["id"] = orderitem.id
        orderitemDict["id"] = str(orderitemDict["id"])
        orderitem.quantity = orderitemDict["quantity"]
        orderitem.order_id = orderitemDict["order_id"]
        orderitem.product_id = orderitemDict["product_id"]
        return orderitem

    def toOrderItemDict(self, orderitem):
        orderitemDict = {}
        orderitemDict["id"] = orderitem.id
        orderitemDict["id"] = str(orderitemDict["id"])
        orderitemDict["quantity"] = orderitem.quantity
        orderitemDict["order_id"] = orderitem.order_id
        orderitemDict["order_id"] = str(orderitemDict["order_id"])
        orderitemDict["product_id"] = orderitem.product_id
        orderitemDict["product_id"] = str(orderitemDict["product_id"])
        return orderitemDict

    def toOrderItemsToList (self, orderitemList):
        orderitems = []
        for orderitem in orderitemList:
            orderitems.append(self.toOrderItemDict(orderitem))
        return orderitems

    def toOrderItemUpdate(self, orderitemDict):
        orderitem = OrderItem()
        orderitem.id = orderitemDict["id"]
        if "quantity" in orderitemDict:        
            orderitem.quantity = orderitemDict["quantity"]
        if "order_id" in orderitemDict:        
            orderitem.order_id = orderitemDict["order_id"]
        if "product_id" in orderitemDict:        
            orderitem.product_id = orderitemDict["product_id"]
        return orderitem