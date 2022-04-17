import hashlib

from flask import Flask
from flask_restful import reqparse

from database import db

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
class User(db.Model):
    username = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(), nullable=False, server_default='')

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save_to_db(self):

        db.session.add(self)
        db.session.commit()

    def remove_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def find_user_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()



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

if __name__ == '__main__':
    app.run(debug=True)