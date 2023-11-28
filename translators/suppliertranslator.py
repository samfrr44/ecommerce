from model import Base
from model import Supplier


class SupplierTranslator:
    count = 0

    def __init__(self):
        print("Data1 Constructor")
        SupplierTranslator.count += 1

    def toSupplier(self, supplierDict):
        supplier = Supplier()
        supplierDict["id"] = supplier.id
        supplierDict["id"] = str(supplierDict["id"])
        supplier.name = supplierDict["name"]
        supplier.address = supplierDict["address"]
        if "address2" in supplierDict:
            supplier.address2 = supplierDict["address2"]
        supplier.city = supplierDict["city"]
        supplier.zipcode = supplierDict["zipcode"]
        supplier.country = supplierDict["country"]
        supplier.email = supplierDict["email"]
        supplier.phone = supplierDict["phone"]
        return supplier

    def toSupplierDict(self, supplier):
        supplierDict = {}
        supplierDict["id"] = supplier.id
        supplierDict["id"] = str(supplierDict["id"])
        supplierDict["name"] = supplier.name
        supplierDict["address"] = supplier.address
        supplierDict["address2"] = supplier.address2
        supplierDict["city"] = supplier.city
        supplierDict["zipcode"] = supplier.zipcode
        supplierDict["country"] = supplier.country
        supplierDict["email"] = supplier.email
        supplierDict["phone"] = supplier.phone
        return supplierDict
    
    def toSuppliersToList (self, supplierList):
        suppliers = []
        for supplier in supplierList:
            suppliers.append(self.toSupplierDict(supplier))
        return suppliers

    def toSupplierUpdate(self, supplierDict):
        supplier = Supplier()
        supplier.id = supplierDict["id"]
        if "name" in supplierDict:        
            supplier.name = supplierDict["name"]
        if "address" in supplierDict:
            supplier.address = supplierDict["address"]
        if "city" in supplierDict:
            supplier.city = supplierDict["city"]
        if "zipcode" in supplierDict:
            supplier.zipcode = supplierDict["zipcode"]
        if "country" in supplierDict:
            supplier.country = supplierDict["country"]
        if "phone" in supplierDict:
            supplier.phone = supplierDict["phone"]
        return supplier
