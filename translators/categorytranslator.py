from model import Base
from model import Category
from validators.validator import CategoryValidator


class CategoryTranslator:
    count = 0

    def __init__(self):
        print("Data1 Constructor")
        CategoryTranslator.count += 1

    def toCategory(self, categoryDict):
        category = Category()
        category.name = categoryDict["name"]
        category.description = categoryDict["description"]
        return category

    def toCategoryDict(self, category):
        categoryDict = {}
        categoryDict["name"] = category.name
        categoryDict["description"] = category.description
        return categoryDict
    
    def toCategoriesToList (self, categoryList):
        categories = []
        for category in categoryList:
            categories.append(self.toCategoryDict(category))
        return categories

    def toCategoryUpdate(self, categoryDict):
        category = Category()
        category.id = categoryDict["id"]
        if "name" in categoryDict:        
            category.name = categoryDict["name"]
        if "description" in categoryDict:
            category.description = categoryDict["description"]
        return category

