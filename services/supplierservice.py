from model import Base
from model import Supplier

from repositories.supplierrepository import SupplierRepository
from translators.suppliertranslator import SupplierTranslator
from validators.validator import SupplierValidator


class SupplierService:
    repository = None

    def __init__(self):
        SupplierService.repository = SupplierRepository()
        SupplierService.translator = SupplierTranslator()

    def save(self, supplierDict):
        SupplierValidator.validate(self, supplierDict)
        supplier = SupplierService.translator.toSupplier(supplierDict)
        return SupplierService.repository.save(supplier)

    def delete(self, id):
        SupplierService.repository.delete(id)

    def findById(self, id):
        supplier = SupplierService.repository.findById(id)
        SupplierValidator.exist(self, supplier)
        supplierDict = SupplierService.translator.toSupplierDict(supplier)
        return supplierDict
    
    def findByName(self, name):
        supplier = SupplierService.repository.findByName(name)
        SupplierValidator.exist(self, supplier)
        supplierDict = SupplierService.translator.toSuppliersToList(supplier)
        return supplierDict

    def findAll():
        suppliers = SupplierService.repository.findById(id)
        supplierList = SupplierService.translator.toSuppliersToList(suppliers)
        return supplierList

    def update(self, supplier):
        supplier = SupplierService.translator.toSupplierUpdate(supplier)
        SupplierService.repository.update(supplier)
