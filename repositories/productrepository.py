from sqlalchemy.orm import sessionmaker
import uuid
from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError
from validationexceptions import ValidationException
from validators.validator import ProductValidator

from model import *



class ProductRepository:
    count = 0
    session = None

    def __init__(self):
        print("Data1 Constructor")
        ProductRepository.count += 1
        engine = create_engine(
            "postgresql://postgres:admin@localhost:5432/company",
            echo=True,
            execution_options={"schema_translate_map": {None: "ecommerce"}},
        )
        Base.metadata.create_all(bind=engine)
        Session_ = sessionmaker(bind=engine)
        ProductRepository.session = Session_()

    def save(self, product):
        try:
            product.id = uuid.uuid4()
            ProductRepository.session.add(product)
            ProductRepository.session.commit()
            return product.id
        except IntegrityError as e:
            raise ValidationException("Could not create product",["Product already exists"])

    def delete(self, id):
        try:
            product = ProductRepository.session.query(Product).get(id)
            ProductValidator.exist(self, product)
            ProductRepository.session.delete(product)
            ProductRepository.session.commit()
        except IntegrityError as e:
            raise ValidationException("Error",["There is an order id(s) associated with this product"])

    def findById(self, id):
        product = ProductRepository.session.query(Product).get(id)
        return product

    def findAll():
        products = ProductRepository.session.query(Product).all()
        return products

    def update(self, product):
        productOld = ProductRepository.session.query(Product).get(product.id)
        if product.name != None and len(product.name) > 0:
            productOld.name = product.name
        if product.unit != None and len(product.unit) > 0:
            productOld.unit = product.unit
        if product.price != None and product.price > 0.0:
            productOld.price = product.price
        if product.category_id != None and len(product.category_id) > 0:
            productOld.category_id = product.category_id
        if product.supplier_id != None and len(product.supplier_id) > 0:
            productOld.supplier_id = product.supplier_id
        ProductRepository.session.commit()
