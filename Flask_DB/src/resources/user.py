from flask_restful import Resource, reqparse
import sqlite3

from src.models.user import User


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        help="this help cannot be empty!"
                        )

    parser.add_argument('password',
                        type=str,
                        help="this help cannot be empty!"
                        )

    def post(self):
        # data = request.get_json()
        data = UserRegister.parser.parse_args()
        user = User.getByUsername(data['username'])
        if user is None:
            connection = sqlite3.connect('data.db')
            cursor = connection.cursor()
            query = "INSERT INTO users VALUES (NULL,?,?)"

            cursor.execute(query, (data['username'], data['password']))

            connection.commit()
            cursor.close()

            return {"message": "The User has been added successfuly!"}

        return {"message": "The Username is duplicated!"}, 400


