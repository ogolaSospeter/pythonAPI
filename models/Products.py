# Modelling the Products table in the MySQL database
# Using MySQL Connector/Python API

import mysql.connector
from mysql.connector import errorcode
import configparser
from flask import Flask, jsonify, request


config = configparser.ConfigParser()
config.read('config.ini')

def get_db_connection():
    return mysql.connector.connect(
        host=config['database']['host'],
        user=config['database']['user'],
        password=config['database']['password'],
        database=config['database']['database']
    )

class Products:
    def __init__(self, product_id, product_name, product_price, product_quantity):
        self.product_id = product_id
        self.product_name = product_name
        self.product_price = product_price
        self.product_quantity = product_quantity

    def get_product_id(self):
        return self.product_id

    def get_product_name(self):
        return self.product_name

    def get_product_price(self):
        return self.product_price

    def get_product_quantity(self):
        return self.product_quantity

    def set_product_id(self, product_id):
        self.product_id = product_id

    def set_product_name(self, product_name):
        self.product_name = product_name

    def set_product_price(self, product_price):
        self.product_price = product_price

    def set_product_quantity(self, product_quantity):
        self.product_quantity = product_quantity

    def __str__(self):
        return "Product ID: " + str(self.product_id) + "\nProduct Name: " + self.product_name + "\nProduct Price: " + str(self.product_price) + "\nProduct Quantity: " + str(self.product_quantity)

    def __repr__(self):
        return "Product ID: " + str(self.product_id) + "\nProduct Name: " + self.product_name + "\nProduct Price: " + str(self.product_price) + "\nProduct Quantity: " + str(self.product_quantity)

    @staticmethod
    def get_all_products():
        try:
            cnx = get_db_connection()
            cursor = cnx.cursor()
            cursor.execute("SELECT * FROM products")
            products = cursor.fetchall()
            return products
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                return "Something is wrong with your user name or password"
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                return "Database does not exist"
            else:
                return err

    @staticmethod
    def get_product(product_id):
        try:
            cnx = get_db_connection()
            cursor = cnx.cursor()
            cursor.execute("SELECT * FROM products WHERE product_id = %s", (product_id,))
            product = cursor.fetchone()
            return product
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                return "Something is wrong with your user name or password"
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                return "Database does not exist"
            else:
                return err
        
    @staticmethod
    def add_product():
        try:
            product_name = request.args.get('product_name')
            product_price = request.args.get('product_price')
            product_quantity = request.args.get('product_quantity')

            cnx = get_db_connection()
            cursor = cnx.cursor()
            cursor.execute("INSERT INTO products (product_name, product_price, product_quantity) VALUES (%s, %s, %s)",
                        (product_name, product_price, product_quantity))
            cnx.commit()
            return "Product added successfully"
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                return "Something is wrong with your user name or password"
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                return "Database does not exist"
            else:
                return str(err)

    @staticmethod
    def deleteproduct(product_id):
        try:
            cnx = get_db_connection()
            cursor = cnx.cursor()
            cursor.execute("DELETE FROM products WHERE product_id = %s", (product_id,))
            cnx.commit()
            return f"Product {product_id} deleted successfully"
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                return "Something is wrong with your user name or password"
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                return "Database does not exist"
            else:
                return err


if __name__ == "__main__":
    print(Products.get_all_products())


