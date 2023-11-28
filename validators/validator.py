from validationexceptions import ValidationException

class CategoryValidator:
    x = ""

    def _init_(self):
        self.x

    def validate(self, categoryDict):
        list = []

        if categoryDict["name"] is None or len(categoryDict["name"]) == 0:
            list.append("Name is required")
        if categoryDict["description"] is None or len(categoryDict["description"]) == 0:
            list.append("Description is required")    
        if len(list) > 0:
            raise ValidationException("Required Fields", list)
        
    def exist(self, category):
        if category is None or not category:
            raise ValidationException("Error", ["Category does not exist"])

class CustomerValidator:
    x = ""

    def _init_(self):
        self.x

    def validate(self, customer):
        list = []

        if customer.get("first name") == None or len(customer["first name"]) == 0:
            list.append("First name is required")
        if customer.get("address") == None or len(customer["address"]) == 0:
            list.append("Address is required")
        if customer.get("city") == None or len(customer["city"]) == 0:
            list.append("City is required")
        if customer.get("zipcode") == None or customer["zipcode"] == 0:
            list.append("Zipcode is required")
        if customer.get("country") == None or len(customer["country"]) == 0:
            list.append("Country is required")
        if customer.get("email") == None or len(customer["email"]) == 0:
            list.append("Email is required")
        if len(list) > 0:
            raise ValidationException("Required Fields", list)
        
    def exist(self, customer):
        list = []

        if customer is None or not customer:
            list.append("Customer(s) do not exist")
        if len(list) > 0:
            raise ValidationException("Error", list)
        

class OrderValidator:
    x = ""

    def _init_(self):
        self.x

    def validate(self, orderDict):
        if orderDict["customer_id"] is None or len(orderDict["customer_id"]) == 0:
            raise ValidationException("Required Fields", ["Customer ID is rquired"])
        
    def exist(self, order):
        if order is None or not order:
            raise ValidationException("Error", ["Order does not exist"])
        
class OrderItemValidator:
    x = ""

    def _init_(self):
        self.x

    def validate(self, orderitem):
        list = []

        if orderitem.get("quantity") == None or len(orderitem["quantity"]) == 0:
            list.append("Quantity is required")
        if orderitem.get("order_id") == None or len(orderitem["order_id"]) == 0:
            list.append("Order ID is required")
        if orderitem.get("product_id") == None or len(orderitem["product_id"]) == 0:
            list.append("Product ID is required")
        if len(list) > 0:
            raise ValidationException("Required Fields", list)

    def exist(self, orderitem):
        if orderitem is None or not orderitem:
            raise ValidationException("Error", ["Order item does not exist"])
        
class ProductValidator:
    x = ""

    def _init_(self):
        self.x

    def validate(self, product):
        list = []

        if product.get("name") == None or len(product["name"]) == 0:
            list.append("Name is required")
        if product.get("unit") == None or len(product["unit"]) == 0:
            list.append("Unit is required")
        if product.get("price") == None or len(str(product["price"])) == 0:
            list.append("Price is required")
        if product.get("category_id") == None or product["category_id"] == 0:
            list.append("Category ID is required")
        if product.get("supplier_id") == None or len(product["supplier_id"]) == 0:
            list.append("Supplier ID is required")
        if len(list) > 0:
            raise ValidationException("Required Fields", list)
        
    def exist(self, product):
        list = []

        if product is None or not product:
            list.append("Product does not exist")
        if len(list) > 0:
            raise ValidationException("Error", list)
        

class SupplierValidator:
    x = ""

    def _init_(self):
        self.x

    def validate(self, supplier):
        list = []

        if supplier.get("name") == None or len(supplier["name"]) == 0:
            list.append("Name is required")
        if supplier.get("address") == None or len(supplier["address"]) == 0:
            list.append("Address is required")
        if supplier.get("city") == None or len(supplier["city"]) == 0:
            list.append("City is required")
        if supplier.get("zipcode") == None or supplier["zipcode"] == 0:
            list.append("Zipcode is required")
        if supplier.get("country") == None or len(supplier["country"]) == 0:
            list.append("Country is required")
        if supplier.get("phone") == None or supplier["phone"] == 0:
            list.append("Phone format must be 999.999.9999")
        if len(list) > 0:
            raise ValidationException("Required Fields", list)
        
    def exist(self, supplier):
        list = []

        if supplier is None or not supplier:
            list.append("Supplier does not exist")
        if len(list) > 0:
            raise ValidationException("Error", list)
