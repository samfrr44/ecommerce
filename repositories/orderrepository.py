from sqlalchemy.orm import sessionmaker
import uuid
from datetime import datetime 
from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError
from validationexceptions import ValidationException
from validators.validator import OrderValidator

from model import *



class OrderRepository:
    count = 0
    session = None

    def __init__(self):
        print("Data1 Constructor")
        OrderRepository.count += 3
        engine = create_engine(
            "postgresql://postgres:admin@localhost:5432/company",
            echo=True,
            execution_options={"schema_translate_map": {None: "ecommerce"}},
        )
        Base.metadata.create_all(bind=engine)
        Session_ = sessionmaker(bind=engine)
        OrderRepository.session = Session_()

    def save(self, order):
        try:
            order.id = uuid.uuid4()
            order.date = datetime.datetime.now()
            OrderRepository.session.add(order)
            OrderRepository.session.commit()
            return order.id
        except IntegrityError as e:
            raise ValidationException("Could not create order",["Order already exists"])

    def delete(self, id):
        try:
            order = OrderRepository.session.query(Order).get(id)
            OrderValidator.exist(self, order)
            OrderRepository.session.delete(order)
            OrderRepository.session.commit()
        except IntegrityError as e:
            raise ValidationException("Error",["There is an order id(s) associated with this order"])
              
    def findAll(self):
        orders = OrderRepository.session.query(Order).all()
        return orders

    def findById(self, id):
        order = OrderRepository.session.query(Order).get(id)
        return order