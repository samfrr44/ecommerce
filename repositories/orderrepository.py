from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects.postgresql import UUID
import uuid
from datetime import datetime 
from sqlalchemy import create_engine
from sqlalchemy.orm.exc import UnmappedInstanceError
from validationexceptions import ValidationException

from model import *

# Base.metadata.create_all(bind=engine)


class OrderRepository:
    count = 0
    session = None

    def __init__(self):
        print("Data1 Constructor")
        OrderRepository.count += 1
        engine = create_engine(
            "postgresql://postgres:admin@localhost:5432/company",
            echo=True,
            execution_options={"schema_translate_map": {None: "ecommerce"}},
        )
        Base.metadata.create_all(bind=engine)
        Session_ = sessionmaker(bind=engine)
        OrderRepository.session = Session_()

    def save(self, order):
        order.id = uuid.uuid4()
        order.date = datetime.datetime.now()
        OrderRepository.session.add(order)
        OrderRepository.session.commit()
        return order.id

    def delete(self, id):
        try:
            order = OrderRepository.session.query(Order).get(id)
            OrderRepository.session.delete(order)
            OrderRepository.session.commit()
        except UnmappedInstanceError as e:
            raise ValidationException("Order does not exist",[])
        
    def findAll(self):
        orders = OrderRepository.session.query(Order).all()
        return orders

    def findById(self, id):
        order = OrderRepository.session.query(Order).get(id)
        return order