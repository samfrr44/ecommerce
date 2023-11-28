from model import Base
from model import Customer

from repositories.customerrepository import CustomerRepository
from translators.customertranslator import CustomerTranslator
from validators.validator import CustomerValidator


class CustomerService:
    repository = None

    def __init__(self):
        CustomerService.repository = CustomerRepository()
        CustomerService.translator = CustomerTranslator()
        CustomerService.validator = CustomerValidator()

    def save(self, customerDict):
        CustomerValidator.validate(self, customerDict)
        customer = CustomerService.translator.toCustomer(customerDict)
        return CustomerService.repository.save(customer)

    def delete(self, id):
        CustomerService.repository.delete(id)

    def findById(self, id):
        customer = CustomerService.repository.findById(id)
        CustomerValidator.exist(self, customer)
        customerDict = CustomerService.translator.toCustomerDict(customer)
        return customerDict
    
    def findByName(self, name):
        customer = CustomerService.repository.findByName(name)
        CustomerValidator.exist(self, customer)
        customerDict = CustomerService.translator.toCustomersToList(customer)
        return customerDict
    
    def findByCity(self, city):
        customer = CustomerService.repository.findByCity(city)
        CustomerValidator.exist(self, customer)
        customerDict = CustomerService.translator.toCustomersToList(customer)
        if not customerDict:
            return "no customers"
        return customerDict
    
    def findByCountry(self, city):
        customer = CustomerService.repository.findByCountry(city)
        CustomerValidator.exist(self, customer)
        customerDict = CustomerService.translator.toCustomersToList(customer)
        if not customerDict:
            return "no customers"
        return customerDict

    def findAll(self):
        customers = CustomerService.repository.findAll()
        customerList = CustomerService.translator.toCustomersToList(customers)
        return customerList

    def update(self, customerDict):
        customer = CustomerService.translator.toCustomerUpdate(customerDict)
        CustomerService.repository.update(customer)
        
