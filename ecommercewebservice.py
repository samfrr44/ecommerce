from flask import Flask, render_template, redirect, url_for
from blueprints.categoryblueprint import category_bp
from blueprints.customerblueprint import customer_bp
from blueprints.order_itemblueprint import orderitem_bp
from blueprints.orderblueprint import order_bp
from blueprints.productblueprint import product_bp
from blueprints.supplierblueprint import supplier_bp
import os


app = Flask(__name__)

app.register_blueprint(category_bp, url_prefix='/category')

app.register_blueprint(customer_bp, url_prefix='/customer')

app.register_blueprint(orderitem_bp, url_prefix='/orderitem')

app.register_blueprint(order_bp, url_prefix='/order')

app.register_blueprint(product_bp, url_prefix='/product')

app.register_blueprint(supplier_bp, url_prefix='/supplier')

if __name__ == '__main__':
   app.run(debug = True)
