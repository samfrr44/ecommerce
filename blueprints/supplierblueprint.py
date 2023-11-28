from flask import Blueprint, Response, request, render_template,  stream_with_context
from services.supplierservice import SupplierService
from validationexceptions import ValidationException
import json


supplier_bp = Blueprint('supplier_bp', __name__)

@supplier_bp.route('/', methods=['POST'])
def createSupplierr():
    service = SupplierService()
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        supplierDict = request.json
        try:
            uuid = service.save(supplierDict)
            json_dic = service.findById(uuid)
            response = Response(json.dumps(json_dic), status = 201, content_type ='application/json')
        except ValidationException as e:
            response = Response(json.dumps({"error":e.errors}), status = 401, content_type ='application/json')
        return response
    else:
        return 'Content-Type not supported!'
    
@supplier_bp.route('/<id>', methods=['PUT'])
def updateSupplier(id):
    service = SupplierService()
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        supplierDict = request.json
        try:
            supplierDict["id"] = id
            service.update(supplierDict)
            json_dic = service.findById(id)
            response = Response(json.dumps(json_dic), status=200, mimetype='application/json')
        except ValidationException as e:
            response = Response(json.dumps({"error":e.errors}), status=400, mimetype='application/json')
        return response
    else:
        return 'Content-Type not supported!'
    
@supplier_bp.route('/id/<id>', methods=['GET'])
def findSupplier(id):
        service = SupplierService()
        try:
            json_dic = service.findById(id)
            response = Response(json.dumps(json_dic), status=200, mimetype='application/json')
        except ValidationException as e:
            response = Response(json.dumps({"error":e.errors}), status=400, mimetype='application/json')
        return response

@supplier_bp.route('/name/<name>', methods=['GET'])
def findByName(name):
        service = SupplierService()
        try:
            json_dic = service.findByName(name)
            response = Response(json.dumps(json_dic), status=200, mimetype='application/json')
        except ValidationException as e:
            response = Response(json.dumps({"error":e.errors}), status=400, mimetype='application/json')
        return response

@supplier_bp.route('/<id>', methods=['DELETE'])
def deleteSupplier(id):
        service = SupplierService()
        try:
            service.delete(id)
            response = Response("Supplier was deleted", status=200, mimetype='application/json')
        except ValidationException as e:
            response = Response(json.dumps({"error":e.errors}), status=400, mimetype='application/json')
        return response