from sqlalchemy.orm import sessionmaker
import uuid
from sqlalchemy import create_engine
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from validationexceptions import ValidationException
from validators.validator import CategoryValidator

from model import *



class CategoryRepository:
    count = 0
    session = None

    def __init__(self):
        print("Data1 Constructor")
        CategoryRepository.count += 1
        engine = create_engine(
            "postgresql://postgres:admin@localhost:5432/company",
            echo=True,
            execution_options={"schema_translate_map": {None: "ecommerce"}},
        )
        Base.metadata.create_all(bind=engine)
        Session_ = sessionmaker(bind=engine)
        CategoryRepository.session = Session_()

    def save(self, category):
        try:
            category.id = uuid.uuid4()
            CategoryRepository.session.add(category)
            CategoryRepository.session.commit()
            return category.id
        except IntegrityError as e:
            raise ValidationException("Could not create category",["Category already exists"])

    def delete(self, id):
        try:
            category = CategoryRepository.session.query(Category).get(id)
            CategoryValidator.exist(self, category)
            CategoryRepository.session.delete(category)
            CategoryRepository.session.commit()
        except IntegrityError as e:
            raise ValidationException("Error",["There is a product(s) associated with this category"])

    def findById(self, id):
        category = CategoryRepository.session.query(Category).get(id)
        return category
    
    def findByName(self, name):
        category = self.session.query(Category).filter(Category.name==name).all()
        return category

    def findAll(self):
        categories = CategoryRepository.session.query(Category).all()
        return categories

    def update(self, category):
        categoryOld = CategoryRepository.session.query(Category).get(category.id)
        CategoryValidator.exist(self, categoryOld)
        if category.name != None and len(category.name) > 0:
            categoryOld.name = category.name
        if category.description != None and len(category.description) > 0:
            categoryOld.description = category.description
        CategoryRepository.session.commit()
