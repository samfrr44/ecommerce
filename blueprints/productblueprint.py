from flask import Blueprint, Response, request, render_template,  stream_with_context
from services.productservice import ProductService
from validationexceptions import ValidationException
import json


product_bp = Blueprint('product_bp', __name__)

@product_bp.route('/', methods=['POST'])
def createProduct():
    service = ProductService()
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        productDict = request.json
        try:
            uuid = service.save(productDict)
            json_dic = service.findById(uuid)
            response = Response(json.dumps({"product id": str(uuid), "info":json_dic}), status = 201, content_type ='application/json')
        except ValidationException as e:
            response = Response(json.dumps({"error":e.errors}), status = 401, content_type ='application/json')
        return response
    else:
        return 'Content-Type not supported!'
    
@product_bp.route('/<id>', methods=['PUT'])
def updateProduct(id):
    service = ProductService()
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        productDict = request.json
        try:
            productDict["id"] = id
            service.update(productDict)
            json_dic = service.findById(id)
            response = Response(json.dumps(json_dic), status=200, mimetype='application/json')
        except ValidationException as e:
            response = Response(json.dumps({"error":e.errors}), status=400, mimetype='application/json')
        return response
    else:
        return 'Content-Type not supported!'
    
@product_bp.route('/<id>', methods=['GET'])
def findProduct(id):
        service = ProductService()
        try:
            json_dic = service.findById(id)
            response = Response(json.dumps(json_dic), status=200, mimetype='application/json')
        except ValidationException as e:
            response = Response(json.dumps({"error":e.errors}), status=400, mimetype='application/json')
        return response

@product_bp.route('/<id>', methods=['DELETE'])
def deleteProduct(id):
        service = ProductService()
        try:
            service.delete(id)
            response = Response("Product was deleted", status=200, mimetype='application/json')
        except ValidationException as e:
            response = Response(json.dumps({"error":e.errors}), status=400, mimetype='application/json')
        return response