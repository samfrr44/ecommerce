from flask import Blueprint, Response, request, render_template,  stream_with_context
from services.order_itemservice import OrderItemService
from validationexceptions import ValidationException
import json


orderitem_bp = Blueprint('orderitem_bp', __name__)

@orderitem_bp.route('/', methods=['POST'])
def createOrderItem():
    service = OrderItemService()
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        orderitemDict = request.json
        try:
            uuid = service.save(orderitemDict)
            json_dic = service.findById(uuid)
            response = Response(json.dumps({"order item id": str(uuid), "info":json_dic}), status = 201, content_type ='application/json')
        except ValidationException as e:
            response = Response(json.dumps({"error":e.errors}), status = 401, content_type ='application/json')
        return response
    else:
        return 'Content-Type not supported!'
    
@orderitem_bp.route('/<id>', methods=['PUT'])
def updateOrderItem(id):
    service = OrderItemService()
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        orderitemDict = request.json
        try:
            orderitemDict["id"] = id
            service.update(orderitemDict)
            json_dic = service.findById(id)
            response = Response(json.dumps(json_dic), status=200, mimetype='application/json')
        except ValidationException as e:
            response = Response(json.dumps({"error":e.errors}), status=400, mimetype='application/json')
        return response
    else:
        return 'Content-Type not supported!'
    
@orderitem_bp.route('/<id>', methods=['GET'])
def findOrderItem(id):
        service = OrderItemService()
        try:
            json_dic = service.findById(id)
            response = Response(json.dumps(json_dic), status=200, mimetype='application/json')
        except ValidationException as e:
            response = Response(json.dumps({"error":e.errors}), status=400, mimetype='application/json')
        return response

@orderitem_bp.route('/<id>', methods=['DELETE'])
def deleteOrderItem(id):
        service = OrderItemService()
        try:
            service.delete(id)
            response = Response("Order Item was deleted", status=200, mimetype='application/json')
        except ValidationException as e:
            response = Response(json.dumps({"error":e.errors}), status=400, mimetype='application/json')
        return response