import sqlite3
from src.database.ORM import db

class Item(db.Model):

    __tablename__ = 'items'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def json(self):
        return {
            "name": self.name,
            "price": self.price
        }

    @classmethod
    def getItemByName(cls, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "SELECT * FROM items where name=?"
        res = cursor.execute(query, (name,))
        row = res.fetchone()

        if row:
            item = cls(*row)
        else:
            item = None

        connection.commit()
        cursor.close()

        return item


