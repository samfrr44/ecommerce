from sqlalchemy.orm import sessionmaker
import uuid
from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError
from validationexceptions import ValidationException
from validators.validator import CustomerValidator

from model import *



class CustomerRepository:
    count = 0
    session = None

    def __init__(self):
        print("Data1 Constructor")
        CustomerRepository.count += 1
        engine = create_engine(
            "postgresql://postgres:admin@localhost:5432/company",
            echo=True,
            execution_options={"schema_translate_map": {None: "ecommerce"}},
        )
        Base.metadata.create_all(bind=engine)
        Session_ = sessionmaker(bind=engine)
        CustomerRepository.session = Session_()

    def save(self, customer):
        customer.id = uuid.uuid4()
        CustomerRepository.session.add(customer)
        CustomerRepository.session.commit()
        return customer.id

    def delete(self, id):
        try:
            customer = CustomerRepository.session.query(Customer).get(id)
            CustomerValidator.exist(self, customer)
            CustomerRepository.session.delete(customer)
            CustomerRepository.session.commit()
        except IntegrityError as e:
            raise ValidationException("Could not delete customer",["There is an order associated with this customer"])

    def findAll(self):
        customers = CustomerRepository.session.query(Customer).all()
        return customers

    def findById(self, id):
        customer = CustomerRepository.session.query(Customer).get(id)
        return customer

    def update(self, customer):
        customerOld = CustomerRepository.session.query(Customer).get(customer.id)
        if customer.name != None and len(customer.name) > 0:
            customerOld.name = customer.name
        if customer.address != None and len(customer.address) > 0:
            customerOld.address = customer.address
        if customer.city != None and len(customer.city) > 0:
            customerOld.city = customer.city
        if customer.zipcode != None and len(customer.zipcode) > 0:
            customerOld.zipcode = customer.zipcode
        if customer.country != None and len(customer.country) > 0:
            customerOld.country = customer.country
        if customer.phone != None and len(customer.phone) > 0:
            customerOld.phone = customer.phone
        CustomerRepository.session.commit()
        
