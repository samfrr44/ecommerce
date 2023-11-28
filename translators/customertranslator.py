from model import Base
from model import Customer


class CustomerTranslator:
    count = 0

    def __init__(self):
        print("Data1 Constructor")
        CustomerTranslator.count += 1

    def toCustomer(self, customerDict):
        customer = Customer()
        customerDict["id"] = customer.id
        customerDict["id"] = str(customerDict["id"])
        customer.fname = customerDict["first name"]
        if "last name" in customerDict:
            customer.lname = customerDict["last name"]
        customer.address = customerDict["address"]
        if "address2" in customerDict:
            customer.address2 = customerDict["address2"]
        customer.city = customerDict["city"]
        customer.zipcode = customerDict["zipcode"]
        customer.country = customerDict["country"]
        customer.email = customerDict["email"]
        if "phone" in customerDict:
            customer.phone = customerDict["phone"]
        return customer

    def toCustomerDict(self, customer):
        customerDict = {}
        customerDict["id"] = customer.id
        customerDict["id"] = str(customerDict["id"])
        customerDict["first name"] = customer.fname
        customerDict["last name"] = customer.lname
        customerDict["address"] = customer.address
        customerDict["address2"] = customer.address2
        customerDict["city"] = customer.city
        customerDict["zipcode"] = customer.zipcode
        customerDict["country"] = customer.country
        customerDict["email"] = customer.email
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
        if "first name" in customerDict:        
            customer.fname = customerDict["first name"]
        if "last name" in customerDict:        
            customer.lname = customerDict["last name"]
        if "address" in customerDict:
            customer.address = customerDict["address"]
        if "address2" in customerDict:
            customer.address2 = customerDict["address 2"]
        if "city" in customerDict:
            customer.city = customerDict["city"]
        if "zipcode" in customerDict:
            customer.zipcode = customerDict["zipcode"]
        if "country" in customerDict:
            customer.country = customerDict["country"]
        if "email" in customerDict:
            customer.email = customerDict["email"]
        if "phone" in customerDict:
            customer.phone = customerDict["phone"]
        return customer
