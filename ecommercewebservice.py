from flask import Flask
from flask import render_template
from flask import request
from services.customerservice import CustomerService
from services.orderservice import OrderService
from services.order_itemservice import OrderItemService
from services.supplierservice import SupplierService
from services.productservice import ProductService
from validationexceptions import ValidationException
from blueprints.categoryapi import category_bp
import json
import uuid
import os

from flask import Flask, redirect, url_for, request

app = Flask(__name__)
print(os.environ['HOST'])
app.register_blueprint(category_bp, url_prefix='/category')

@app.route('/customer', methods=['POST'])
def createCustomer():
    service = CustomerService()
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        customerDict = request.json
        try:
            uuid = service.save(customerDict)
            json_dic = service.findById(uuid)
            response = app.response_class(
                response= (json.dumps({"customer id": str(uuid), "info":json_dic})),
                status=201,
                mimetype='application/json'
            )
        except ValidationException as e:
            response = app.response_class(
                response = (json.dumps({"error":e.errors})),
                status=400,
                mimetype='application/json'
            )
        return response
    else:
        return 'Content-Type not supported!'
    
@app.route('/order', methods=['POST'])
def createOrder():
    service = OrderService()
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        orderDict = request.json
        try:
            uuid = service.save(orderDict)
            json_dic = service.findById(uuid)
            response = app.response_class(
                response= (json.dumps({"order id": str(uuid), "info":json_dic})),
                status=201,
                mimetype='application/json'
            )
        except ValidationException as e:
            response = app.response_class(
                response = (json.dumps({"error":e.errors})),
                status=400,
                mimetype='application/json'
            )
        return response
    else:
        return 'Content-Type not supported!'
    
@app.route('/orderitem', methods=['POST'])
def createOrderItem():
    service = OrderItemService()
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        orderitemDict = request.json
        try:
            uuid = service.save(orderitemDict)
            json_dic = service.findById(uuid)
            response = app.response_class(
                response= (json.dumps({"order item id": str(uuid), "info":json_dic})),
                status=201,
                mimetype='application/json'
            )
        except ValidationException as e:
            response = app.response_class(
                response = (json.dumps({"error":e.errors})),
                status=400,
                mimetype='application/json'
            )
        return response
    else:
        return 'Content-Type not supported!'
    
@app.route('/product', methods=['POST'])
def createProduct():
    service = ProductService()
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        productDict = request.json
        try:
            uuid = service.save(productDict)
            json_dic = service.findById(uuid)
            response = app.response_class(
                response= (json.dumps({"product id": str(uuid), "info":json_dic})),
                status=201,
                mimetype='application/json'
            )
        except ValidationException as e:
            response = app.response_class(
                response = (json.dumps({"error":e.errors})),
                status=400,
                mimetype='application/json'
            )
        return response
    else:
        return 'Content-Type not supported!'
    
@app.route('/supplier', methods=['POST'])
def createSupplier():
    service = SupplierService()
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        supplierDict = request.json
        try:
            uuid = service.save(supplierDict)
            json_dic = service.findById(uuid)
            response = app.response_class(
                response= (json.dumps({"supplier id": str(uuid), "info":json_dic})),
                status=201,
                mimetype='application/json'
            )
        except ValidationException as e:
            response = app.response_class(
                response = (json.dumps({"error":e.errors})),
                status=400,
                mimetype='application/json'
            )
        return response
    else:
        return 'Content-Type not supported!'
          
@app.route('/customer/<id>', methods=['PUT'])
def updateCustomer(id):
    service = CustomerService()
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        customerDict = request.json
        try:
            customerDict["id"] = id
            service.update(customerDict)
            json_dic = service.findById(id)
            response = app.response_class(
                response=json.dumps(json_dic),
                status=200,
                mimetype='application/json'
            )
        except ValidationException as e:
            response = app.response_class(
                response = (json.dumps({"error":e.errors})),
                status=400,
                mimetype='application/json'
            )
        return response
    else:
        return 'Content-Type not supported!'
    
@app.route('/orderitem/<id>', methods=['PUT'])
def updateOrderItem(id):
    service = OrderItemService()
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        orderitemDict = request.json
        try:
            orderitemDict["id"] = id
            service.update(orderitemDict)
            json_dic = service.findById(id)
            response = app.response_class(
                response=json.dumps(json_dic),
                status=200,
                mimetype='application/json'
            )
        except ValidationException as e:
            response = app.response_class(
                response = (json.dumps({"error":e.errors})),
                status=400,
                mimetype='application/json'
            )
        return response
    else:
        return 'Content-Type not supported!'
    
@app.route('/product/<id>', methods=['PUT'])
def updateProduct(id):
    service = ProductService()
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        productDict = request.json
        try:
            productDict["id"] = id
            service.update(productDict)
            json_dic = service.findById(id)
            response = app.response_class(
                response=json.dumps(json_dic),
                status=200,
                mimetype='application/json'
            )
        except ValidationException as e:
            response = app.response_class(
                response = (json.dumps({"error":e.errors})),
                status=400,
                mimetype='application/json'
            )
        return response
    else:
        return 'Content-Type not supported!'
    

    
@app.route('/supplier/<id>', methods=['PUT'])
def updateSupplier(id):
    service = SupplierService()
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        supplierDict = request.json
        try:
            supplierDict["id"] = id
            service.update(supplierDict)
            json_dic = service.findById(id)
            response = app.response_class(
                response=json.dumps(json_dic),
                # response=id,
                status=200,
                mimetype='application/json'
            )
        except ValidationException as e:
            response = app.response_class(
                response = (json.dumps({"error":e.errors})),
                status=400,
                mimetype='application/json'
            )
        return response
    else:
        return 'Content-Type not supported!'
   
@app.route('/customer/<id>', methods=['GET'])
def findCustomer(id):
        service = CustomerService()
        try:
            json_dic = service.findById(id)
            response = app.response_class(
                response= json.dumps(json_dic),
                status=200,
                mimetype='application/json'
            )
        except ValidationException as e:
            response = app.response_class(
                response = (json.dumps({"error":e.errors})),
                status=400,
                mimetype='application/json'
            )

        return response

@app.route('/order/<id>', methods=['GET'])
def findOrder(id):
        service = OrderService()
        try:
            json_dic = service.findById(id)
            response = app.response_class(
                response= json.dumps(json_dic),
                status=200,
                mimetype='application/json'
            )
        except ValidationException as e:
            response = app.response_class(
                response = (json.dumps({"error":e.errors})),
                status=400,
                mimetype='application/json'
            )

        return response

@app.route('/orderitem/<id>', methods=['GET'])
def findOrderItem(id):
        service = OrderItemService()
        try:
            json_dic = service.findById(id)
            response = app.response_class(
                response= json.dumps(json_dic),
                status=200,
                mimetype='application/json'
            )
        except ValidationException as e:
            response = app.response_class(
                response = (json.dumps({"error":e.errors})),
                status=400,
                mimetype='application/json'
            )

        return response

@app.route('/product/<id>', methods=['GET'])
def findProduct(id):
        service = ProductService()
        try:
            json_dic = service.findById(id)
            response = app.response_class(
                response= json.dumps(json_dic),
                status=200,
                mimetype='application/json'
            )
        except ValidationException as e:
            response = app.response_class(
                response = (json.dumps({"error":e.errors})),
                status=400,
                mimetype='application/json'
            )

        return response

@app.route('/supplier/<id>', methods=['GET'])
def findSupplier(id):
        service = SupplierService()
        try:
            json_dic = service.findById(id)
            response = app.response_class(
                response= json.dumps(json_dic),
                status=200,
                mimetype='application/json'
            )
        except ValidationException as e:
            response = app.response_class(
                response = (json.dumps({"error":e.errors})),
                status=400,
                mimetype='application/json'
            )

        return response
       
@app.route('/customer/<id>', methods=['DELETE'])
def deleteCustomer(id):
        service = CustomerService()
        try:
            service.delete(id)
            response = app.response_class(
                response= "Customer was deleted",
                status=200,
                mimetype='application/json'
            )
        except ValidationException as e:
            response = app.response_class(
                response = (json.dumps({"error":e.errors})),
                status=400,
                mimetype='application/json'
            )

        return response
        
@app.route('/order/<id>', methods=['DELETE'])
def deleteOrder(id):
        service = OrderService()
        try:
            service.delete(id)
            response = app.response_class(
                response= "Order was deleted",
                status=200,
                mimetype='application/json'
            )
        except ValidationException as e:
            response = app.response_class(
                response = (json.dumps({"error":e.errors})),
                status=400,
                mimetype='application/json'
            )
        return response

@app.route('/orderitem/<id>', methods=['DELETE'])
def deleteOrderItem(id):
        service = OrderItemService()
        try:
            service.delete(id)
            response = app.response_class(
                response= "Order item was deleted",
                status=200,
                mimetype='application/json'
            )
        except ValidationException as e:
            response = app.response_class(
                response = (json.dumps({"error":e.errors})),
                status=400,
                mimetype='application/json'
            )
        return response

@app.route('/product/<id>', methods=['DELETE'])
def deleteProduct(id):
        service = ProductService()
        try:
            service.delete(id)
            response = app.response_class(
                response= "Product was deleted",
                status=200,
                mimetype='application/json'
            )
        except ValidationException as e:
            response = app.response_class(
                response = (json.dumps({"error":e.errors})),
                status=400,
                mimetype='application/json'
            )
        return response

@app.route('/supplier/<id>', methods=['DELETE'])
def deleteSupplier(id):
        service = SupplierService()
        try:
            service.delete(id)
            response = app.response_class(
                response= "Supplier was deleted",
                status=200,
                mimetype='application/json'
            )
        except ValidationException as e:
            response = app.response_class(
                response = (json.dumps({"error":e.errors})),
                status=400,
                mimetype='application/json'
            )
        return response

if __name__ == '__main__':
   app.run(debug = True)
