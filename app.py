from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
db = SQLAlchemy(app)


class UserModel(db.Model):
    id = db.Column(db.Integer,)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)

db.create_all()

_user_parser = reqparse.RequestParser()
_user_parser.add_argument(
    "username",
    type=str,
    required=True,
    help='This cannot be blank'
)

_user_parser.add_argument(
    "password",
    type=str,
    required=True,
    help='This cannot be blank'
)


_user_update_parser = reqparse.RequestParser()
_user_update_parser.add_argument(
    "username",
    type=str,
    required=True,
    help='This cannot be blank'
)

_user_update_parser.add_argument(
    "password",
    type=str,
    required=True,
    help='This cannot be blank'
)

resource_fields = {
	'id': fields.Integer,
	'username': fields.String,
    'password': fields.String,
}

db.create_all()


#R - READ
@app.route('api/<user_id>')
@marshal_with(resource_fields)
def get(self, user_id):
    result = UserModel.querty.filter_by(id=user_id).first()
    if not result:
        abort(404, message="Can't find a user with that id")
    return result
    
#C - CREATE
@app.route('api/create')
@marshal_with(resource_fields)
def post():
    user = UserModel()
        
    db.session.add(user)
    db.session.commit()
    pass
    
#U - UPDATE
@app.route('api/update')
@marshal_with(resource_fields)
def patch():
    #_user_update_parser
    #if _user_parser['username'] != user_update_args['username']:
        # user_update_args['username'] = _user_put_args['username']
        #if _user_parser['password'] != user_update_args['password']:
            # user_update_args['password'] = _user_put_args['password']
        #else:
            #abort('Message that it failed')
    #else:
        #abort('Message that it failed')
    pass
    
#D - DELETE
@app.route('api/delete')
def delete():
    user = UserModel()
        
    db.session.delete(user)
    db.session.commit()
    pass


if __name__ == "__main__":
    app.run(debug=True)