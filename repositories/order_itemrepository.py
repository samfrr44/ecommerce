from sqlalchemy.orm import sessionmaker
import uuid
from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError
from validationexceptions import ValidationException
from validators.validator import OrderItemValidator
import os
from model import *



class OrderItemRepository:
    count = 0
    session = None

    def __init__(self):
        print("Data1 Constructor")
        DB_USER=os.getenv("DB_USER")
        DB_PWD=os.getenv("DB_PWD")
        DB_HOST=os.getenv("DB_HOST")
        DB_PORT=os.getenv("DB_PORT")
        DB_NAME=os.getenv("DB_NAME")
        OrderItemRepository.count += 1
        engine = create_engine(
            "postgresql://"+DB_USER+":"+DB_PWD+"@"+DB_HOST+":"+DB_PORT+"/"+DB_NAME+"",
            echo=True,
            execution_options={"schema_translate_map": {None: "ecommerce"}},
        )
        Base.metadata.create_all(bind=engine)
        Session_ = sessionmaker(bind=engine)
        OrderItemRepository.session = Session_()

    def save(self, orderitem):
        try:
            orderitem.id = uuid.uuid4()
            OrderItemRepository.session.add(orderitem)
            OrderItemRepository.session.commit()
            return orderitem.id
        except IntegrityError as e:
            raise ValidationException("Could not create order item",["Order item already exists"])
        
    def delete(self, id):
        orderitem = OrderItemRepository.session.query(OrderItem).get(id)
        OrderItemValidator.exist(self, orderitem)
        OrderItemRepository.session.delete(orderitem)
        OrderItemRepository.session.commit()


    def findById(self, id):
        orderitem = OrderItemRepository.session.query(OrderItem).get(id)
        return orderitem
    
    def findByOrder(self, id):
        orderitem = OrderItemRepository.session.query(OrderItem).filter(OrderItem.order_id==id).all()
        return orderitem
    
    def findByProduct(self, id):
        orderitem = OrderItemRepository.session.query(OrderItem).filter(OrderItem.product_id==id).all()
        return orderitem

    def findAll():
        orders = OrderItemRepository.session.query(OrderItem).all()
        return orders

    def update(self, orderitem):
        orderOld = OrderItemRepository.session.query(OrderItem).get(orderitem.id)
        if orderitem.quantity != None and orderitem.quantity > 0:
            orderOld.quantity = orderitem.quantity
        if orderitem.order_id != None and len(orderitem.order_id) > 0:
            orderOld.order_id = orderitem.order_id
        if orderitem.product_id != None and len(orderitem.product_id) > 0:
            orderOld.product_id = orderitem.product_id
        OrderItemRepository.session.commit()
