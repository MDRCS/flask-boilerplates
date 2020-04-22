from flask_restful import Resource, reqparse
import sqlite3
from flask_jwt import jwt_required

from src.models.item import Item

class ItemRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name',
                        type=str,
                        help="this help cannot be empty!"
                        )

    parser.add_argument('price',
                        type=str,
                        help="this help cannot be empty!"
                        )

    @jwt_required()
    def post(self):
        data = ItemRegister.parser.parse_args()

        connect = sqlite3.connect('data.db')
        cursor = connect.cursor()
        query = "INSERT INTO items VALUES (?,?)"

        cursor.execute(query, (data['name'], data['price']))

        connect.commit()
        cursor.close()

        return {"message": "The Item has been added successfuly!"}


class Item_(Resource):

    @jwt_required()
    def get(self):
        connect = sqlite3.connect('data.db')
        cursor = connect.cursor()
        query = "SELECT * FROM items"
        result = cursor.execute(query)
        items = result.fetchall()
        Items = []
        for item in items:
            Items.append(Item(*item).json())
        return Items


class GetOneItem(Resource):

    @jwt_required()
    def get(self, name):
        connect = sqlite3.connect('data.db')
        cursor = connect.cursor()
        query = "SELECT * FROM items where name=?"
        result = cursor.execute(query, (name,))
        item = result.fetchone()

        return Item(*item).json()
