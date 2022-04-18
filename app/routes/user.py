import hashlib

from flask import Flask
from flask_restful import reqparse

from app.model import User

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


app = Flask(__name__)

@app.route('/')
def index():
    return 'hey, this is the homepage'

#C - CREATE
@app.route('/create', methods= ['POST'])
def create(self):
        data = _user_parser.parse_args()
        username = data["username"]
        user = User(username, hashlib.sha256(data["password"].encode("utf-8")).hexdigest())

        if user:            
            user.save_to_db()
            return {
                    "message": "User {} created!".format(username)
            }

#R - READ
@app.route('/read')
def read(self):
    return 'hey, this is the read page'

#U - UPDATE
@app.route('/update')
def update(self):
    return 'hey, this is the update page'

#D - delete
@app.route('/delete')
def delete(self, user_id):
    user = User.find_user_by_id(user_id)
    if user:
        user.remove_from_db()
        return {
            "User has been deleted!"
        }
