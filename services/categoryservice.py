from model import Base
from model import Category

from repositories.categoryrepository import CategoryRepository
from translators.categorytranslator import CategoryTranslator
from validators.validator import CategoryValidator


class CategoryService:
    repository = None

    def __init__(self):
        CategoryService.repository = CategoryRepository()
        CategoryService.translator = CategoryTranslator()

    def save(self, categoryDict):
        CategoryValidator.validate(self, categoryDict)
        category = CategoryService.translator.toCategory(categoryDict)
        return CategoryService.repository.save(category)

    def delete(self, id):
        CategoryService.repository.delete(id)

    def findById(self, id):
        category = CategoryService.repository.findById(id)
        CategoryValidator.exist(self, category)
        categoryDict = CategoryService.translator.toCategoryDict(category)
        return categoryDict

    def findAll(self):
        categories = CategoryService.repository.findAll()
        categoryList = CategoryService.translator.toCategoriesToList(categories)
        return categoryList

    def update(self, categoryDict):
        category = CategoryService.translator.toCategoryUpdate(categoryDict)
        CategoryService.repository.update(category)

        
