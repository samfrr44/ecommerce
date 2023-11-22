from flask import Blueprint, Response, request, render_template,  stream_with_context
from services.orderservice import OrderService
from validationexceptions import ValidationException
import json


order_bp = Blueprint('order_bp', __name__)

@order_bp.route('/', methods=['POST'])
def createOrder():
    service = OrderService()
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        orderDict = request.json
        try:
            uuid = service.save(orderDict)
            json_dic = service.findById(uuid)
            response = Response(json.dumps({"order  id": str(uuid), "info":json_dic}), status = 201, content_type ='application/json')
        except ValidationException as e:
            response = Response(json.dumps({"error":e.errors}), status = 401, content_type ='application/json')
        return response
    else:
        return 'Content-Type not supported!'
    
@order_bp.route('/<id>', methods=['GET'])
def findOrder(id):
        service = OrderService()
        try:
            json_dic = service.findById(id)
            response = Response(json.dumps(json_dic), status=200, mimetype='application/json')
        except ValidationException as e:
            response = Response(json.dumps({"error":e.errors}), status=400, mimetype='application/json')
        return response

@order_bp.route('/<id>', methods=['DELETE'])
def deleteOrder(id):
        service = OrderService()
        try:
            service.delete(id)
            response = Response("Order  was deleted", status=200, mimetype='application/json')
        except ValidationException as e:
            response = Response(json.dumps({"error":e.errors}), status=400, mimetype='application/json')
        return response