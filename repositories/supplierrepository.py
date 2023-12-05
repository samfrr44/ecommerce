from sqlalchemy.orm import sessionmaker
import uuid
from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError
from validationexceptions import ValidationException
from validators.validator import SupplierValidator
import os
from model import *



class SupplierRepository:
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
        SupplierRepository.session = Session_()

    def save(self,supplier):
        try:
            supplier.id = uuid.uuid4()
            SupplierRepository.session.add(supplier)
            SupplierRepository.session.commit()
            return supplier.id
        except IntegrityError as e:
            raise ValidationException("Could not create supplier",["Supplier already exists"])

    def delete(self, id):
        try:
            supplier = SupplierRepository.session.query(Supplier).get(id)
            SupplierValidator.exist(self, supplier)
            SupplierRepository.session.delete(supplier)
            SupplierRepository.session.commit()
        except IntegrityError as e:
            raise ValidationException("Error",["There is a product(s) associated with this supplier"])

    def findById(self, id):
        supplier = SupplierRepository.session.query(Supplier).get(id)
        return supplier
    
    def findByName(self, name):
        supplier = self.session.query(Supplier).filter(Supplier.name==name).all()
        SupplierValidator.exist(self, supplier)
        return supplier

    def findAll():
        suppliers = SupplierRepository.session.query(Supplier).all()
        return suppliers

    def update(self, supplier):
        supplierOld = SupplierRepository.session.query(Supplier).get(supplier.id)
        SupplierValidator.exist(self, supplierOld)
        if supplier.name != None and len(supplier.name) > 0:
            supplierOld.name = supplier.name
        if supplier.address != None and len(supplier.address) > 0:
            supplierOld.address = supplier.address
        if supplier.city != None and len(supplier.city) > 0:
            supplierOld.city = supplier.city
        if supplier.zipcode != None and len(supplier.zipcode) > 0:
            supplierOld.zipcode = supplier.zipcode
        if supplier.country != None and len(supplier.country) > 0:
            supplierOld.country = supplier.country
        if supplier.phone != None and len(supplier.phone) > 0:
            supplierOld.phone = supplier.phone
        SupplierRepository.session.commit()
