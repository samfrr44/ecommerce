from flask import Blueprint, Response, request, render_template,  stream_with_context
from services.customerservice import CustomerService
from validationexceptions import ValidationException
import json


customer_bp = Blueprint('customer_bp', __name__)

@customer_bp.route('/', methods=['POST'])
def createCustomer():
    service = CustomerService()
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        customerDict = request.json
        try:
            uuid = service.save(customerDict)
            json_dic = service.findById(uuid)
            response = Response(json.dumps({"customer id": str(uuid), "info":json_dic}), status = 201, content_type ='application/json')
        except ValidationException as e:
            response = Response(json.dumps({"error":e.errors}), status = 401, content_type ='application/json')
        return response
    else:
        return 'Content-Type not supported!'
    
@customer_bp.route('/<id>', methods=['PUT'])
def updateCustomer(id):
    service = CustomerService()
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        customerDict = request.json
        try:
            customerDict["id"] = id
            service.update(customerDict)
            json_dic = service.findById(id)
            response = Response(json.dumps(json_dic), status=200, mimetype='application/json')
        except ValidationException as e:
            response = Response(json.dumps({"error":e.errors}), status=400, mimetype='application/json')
        return response
    else:
        return 'Content-Type not supported!'
    
@customer_bp.route('/<id>', methods=['GET'])
def findCustomer(id):
        service = CustomerService()
        try:
            json_dic = service.findById(id)
            response = Response(json.dumps(json_dic), status=200, mimetype='application/json')
        except ValidationException as e:
            response = Response(json.dumps({"error":e.errors}), status=400, mimetype='application/json')
        return response

@customer_bp.route('/<id>', methods=['DELETE'])
def deleteCustomer(id):
        service = CustomerService()
        try:
            service.delete(id)
            response = Response("Customer was deleted", status=200, mimetype='application/json')
        except ValidationException as e:
            response = Response(json.dumps({"error":e.errors}), status=400, mimetype='application/json')
        return response