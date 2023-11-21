from model import Base
from model import Product


class ProductTranslator:
    count = 0

    def __init__(self):
        print("Data1 Constructor")
        ProductTranslator.count += 1

    def toProduct(self, productDict):
        product = Product()
        product.name = productDict["name"]
        product.unit = productDict["unit"]
        product.price = productDict["price"]
        product.category_id = productDict["category_id"]
        product.supplier_id = productDict["supplier_id"]
        return product

    def toProductDict(self, product):
        productDict = {}
        productDict["name"] = product.name
        productDict["unit"] = product.unit
        productDict["price"] = product.price
        productDict["category_id"] = product.category_id
        productDict["category_id"] = str(productDict["category_id"])
        productDict["supplier_id"] = product.supplier_id
        productDict["supplier_id"] = str(productDict["supplier_id"])
        return productDict

    def toProductsToList (self, productList):
        products = []
        for product in productList:
            products.append(self.toProductDict(product))
        return products

    def toProductUpdate(self, productDict):
        product = Product()
        product.id = productDict["id"]
        if "name" in productDict:        
            product.name = productDict["name"]
        if "unit" in productDict:
            product.unit = productDict["unit"]
        if "price" in productDict:
            product.price = productDict["price"]
        if "category_id" in productDict:
            product.category_id = productDict["category_id"]
        if "supplier_id" in productDict:
            product.supplier_id = productDict["supplier_id"]
        return product
