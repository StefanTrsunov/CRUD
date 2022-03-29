from flask_restful import reqparse
from flask_sqlalchemy import SQLAlchemy
from app.models.user import User
from app.database.db import db
from flask import current_app as app
from flask import Flask, request

id = 1

_user_parser = reqparse.RequestParser()
_user_parser.add_argument(
    "username",
    type=str,
    required=True,
    help="This field cannot be blank"
)
_user_parser.add_argument(
    "password",
    type=str,
    required=True,
    help="This field cannot be blank"
)


def save_to_db(user):
    db.session.add(user)
    db.session.commit()

def del_from_db(user_id):
    db.session.delete(user_id)
    db.session.commit()

#C - CREATE
@app.route('/create', methods=['POST'])
def create():
    global id
    if request.method == 'POST':
        data = _user_parser.parse_args()

        username = data["username"]
        password = data["password"]
        user = User(id, username, password)
        id += 1
        return save_to_db(user)
    else:
        print('Wrong method')

#R - READ
@app.route('/read', methods=['POST'])
def read():
    if request.method == 'POST':
        return User.query.all()
    else:
        print('Wrong method')

#U - UPDATE
@app.route('/update', methods=['PUT'])
def update():
    if request.method == 'PUT':
        return
    else:
        print('Wrong method')

#D - DELELTE
@app.route('/delete', methods=['DELETE'])
def delete():
    if request.method == 'DELETE':
        return del_from_db(1)
    else:
        print('Wrong method')