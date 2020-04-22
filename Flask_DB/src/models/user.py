import sqlite3
from src.database.ORM import db

class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, _id, email, password):
        self.id = _id
        self.email = email
        self.password = password

    def __repr__(self):
        return "<User {}>".format(self.email)

    @classmethod
    def getByEmail(cls,email):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "SELECT * FROM users where email=?"
        res = cursor.execute(query, (email,))
        row = res.fetchone()

        if row:
            user = cls(*row)
        else:
            user = None

        connection.commit()
        cursor.close()

        return user

    @classmethod
    def getById(cls, _id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "SELECT * FROM users where id=?"
        res = cursor.execute(query, (_id,))
        row = res.fetchone()

        if row:
            user = cls(*row)
        else:
            user = None

        connection.commit()
        cursor.close()

        return user




