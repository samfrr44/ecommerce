from model import Base
from model import Product

from repositories.productrepository import ProductRepository
from translators.producttranslator import ProductTranslator
from validators.validator import ProductValidator


class ProductService:
    repository = None

    def __init__(self):
        ProductService.repository = ProductRepository()
        ProductService.translator = ProductTranslator()

    def save(self, productDict):
        ProductValidator.validate(self, productDict)
        product = ProductService.translator.toProduct(productDict)
        return ProductService.repository.save(product)

    def delete(self, id):
        ProductService.repository.delete(id)

    def findById(self, id):
        product = ProductService.repository.findById(id)
        ProductValidator.exist(self, product)
        productDict = ProductService.translator.toProductDict(product)
        return productDict
    
    def findByName(self, name):
        products = ProductService.repository.findByName(name)
        productList = ProductService.translator.toProductsToList(products)
        return productList

    def findAll():
        products = ProductService.repository.findById(id)
        productList = ProductService.translator.toProductsToList(products)
        return productList

    def update(self, product):
        product = ProductService.translator.toProductUpdate(product)
        ProductService.repository.update(product)
