from flask import Flask
from flask import render_template
from flask import Blueprint
from flask import request
from services.categoryservice import CategoryService
from validationexceptions import ValidationException
import json
import uuid
from flask import app
from flask import Response, stream_with_context

category_bp = Blueprint('category_bp', __name__)



@category_bp.route('/', methods=['POST'])
def createCategory():
    service = CategoryService()
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        categoryDict = request.json
        try:
            uuid = service.save(categoryDict)
            json_dic = service.findById(uuid)
            response = Response(json.dumps({"category id": str(uuid), "info":json_dic}), status = 201, content_type ='application/json')
        except ValidationException as e:
            response = Response(json.dumps({"error":e.errors}), status = 401, content_type ='application/json')
        return response
    else:
        return 'Content-Type not supported!'
    
# @category_bp.route('/<id>', methods=['PUT'])
# def updateCategory(id):
#     service = CategoryService()
#     content_type = request.headers.get('Content-Type')
#     if (content_type == 'application/json'):
#         categoryDict = request.json
#         try:
#             categoryDict["id"] = id
#             service.update(categoryDict)
#             json_dic = service.findById(id)
#             response = category_bp.response_class(
#                 response=json.dumps(json_dic),
#                 # response=id,
#                 status=200,
#                 mimetype='application/json'
#             )
#         except ValidationException as e:
#             response = category_bp.response_class(
#                 response = (json.dumps({"error":e.errors})),
#                 status=400,
#                 mimetype='application/json'
#             )
#         return response
#     else:
#         return 'Content-Type not supported!'
    
# @category_bp.route('/<id>', methods=['GET'])
# def findCategory(id):
#         service = CategoryService()
#         try:
#             json_dic = service.findById(id)
#             response = category_bp.response_class(
#                 response= json.dumps(json_dic),
#                 status=200,
#                 mimetype='application/json'
#             )
#         except ValidationException as e:
#             response = category_bp.response_class(
#                 response = (json.dumps({"error":e.errors})),
#                 status=400,
#                 mimetype='application/json'
#             )

#         return response

# @category_bp.route('/<id>', methods=['DELETE'])
# def deleteCategory(id):
#         service = CategoryService()
#         try:
#             service.delete(id)
#             response = category_bp.response_class(
#                 response= "Category was deleted",
#                 status=200,
#                 mimetype='application/json'
#             )
#         except ValidationException as e:
#             response = category_bp.response_class(
#                 response = (json.dumps({"error":e.errors})),
#                 status=400,
#                 mimetype='application/json'
#             )

#         return response