from flask import Flask, jsonify, request
from models.Products import Products

app = Flask(__name__)

incomes = [
    { 'description': 'salary', 'amount': 5000 },
    { 'description': 'salary', 'amount': 7500 },
    { 'description': 'salary', 'amount': 8000 },
    { 'description': 'salary', 'amount': 6500 },

]


@app.route('/incomes')
def get_incomes():
    return jsonify([income for income in incomes])


@app.route('/incomes', methods=['POST'])
def add_income():
    incomes.append(request.get_json())
    return '', 204

@app.route('/products')
def get_products():
    products = Products.get_all_products()
    return jsonify(products)

@app.route('/product/<int:product_id>')
def get_product(product_id):
    product = Products.get_product(product_id)
    return jsonify(product)

@app.route('/newproduct', methods=['GET'])
def add_product():
    return Products.add_product()

@app.route('/deleteproduct/<int:product_id>', methods=['GET'])
def delete_product(product_id):
    return Products.deleteproduct(product_id)

