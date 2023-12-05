from sqlalchemy.orm import sessionmaker
import uuid
from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError
from validationexceptions import ValidationException
from validators.validator import CustomerValidator
import os
from model import *



class CustomerRepository:
    count = 0
    session = None

    def __init__(self):
        print("Data1 Constructor")
        DB_USER=os.getenv("DB_USER")
        DB_PWD=os.getenv("DB_PWD")
        DB_HOST=os.getenv("DB_HOST")
        DB_PORT=os.getenv("DB_PORT")
        DB_NAME=os.getenv("DB_NAME")
        engine = create_engine(
            "postgresql://"+DB_USER+":"+DB_PWD+"@"+DB_HOST+":"+DB_PORT+"/"+DB_NAME+"",
            echo=True,
            execution_options={"schema_translate_map": {None: "ecommerce"}},
        )
        Base.metadata.create_all(bind=engine)
        Session_ = sessionmaker(bind=engine)
        CustomerRepository.session = Session_()

    def save(self, customer):
        try:
            customer.id = uuid.uuid4()
            CustomerRepository.session.add(customer)
            CustomerRepository.session.commit()
            return customer.id
        except IntegrityError as e:
            raise ValidationException("Could not create customer",["Customer already exists"])

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
    
    def findByName(self, name):
        customer = self.session.query(Customer).filter(Customer.fname==name).all()
        CustomerValidator.exist(self, customer)
        return customer
    
    def findByCity(self, city):
        customer = self.session.query(Customer).filter(Customer.city==city).all()
        return customer

    def findByCountry(self, country):
        customer = self.session.query(Customer).filter(Customer.country==country).all()
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
        
