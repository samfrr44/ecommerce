from model import Base
from model import Customer


class CustomerTranslator:
    count = 0

    def __init__(self):
        print("Data1 Constructor")
        CustomerTranslator.count += 1

    def toCustomer(self, customerDict):
        customer = Customer()
        customer.name = customerDict["name"]
        customer.address = customerDict["address"]
        customer.city = customerDict["city"]
        customer.zipcode = customerDict["zipcode"]
        customer.country = customerDict["country"]
        customer.phone = customerDict["phone"]
        return customer

    def toCustomerDict(self, customer):
        customerDict = {}
        customerDict["name"] = customer.name
        customerDict["address"] = customer.address
        customerDict["city"] = customer.city
        customerDict["zipcode"] = customer.zipcode
        customerDict["country"] = customer.country
        customerDict["phone"] = customer.phone
        return customerDict
    
    def toCustomersToList (self, customerList):
        customers = []
        for customer in customerList:
            customers.append(self.toCustomerDict(customer))
        return customers

    def toCustomerUpdate(self, customerDict):
        customer = Customer()
        customer.id = customerDict["id"]
        if "name" in customerDict:        
            customer.name = customerDict["name"]
        if "address" in customerDict:
            customer.address = customerDict["address"]
        if "city" in customerDict:
            customer.city = customerDict["city"]
        if "zipcode" in customerDict:
            customer.zipcode = customerDict["zipcode"]
        if "country" in customerDict:
            customer.country = customerDict["country"]
        if "phone" in customerDict:
            customer.phone = customerDict["phone"]
        return customer
