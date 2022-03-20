from flask import Flask, request, render_template
from database.db import db
from models.user import User

app = Flask(__name__)

def create_db():
    db.create_all()

#C - CREATE
@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'GET':
        return render_template('createuser.html')
    
    if request.method == 'POST':
        id = request.form('id')
        username = request.form('username')
        password = request.form('password')
        acc = User
        save_to_db(User)

#R - READ
@app.route('/read', methods=['POST'])
def read():
    users = User.query.all()
    return render_template('data.html', users=users)

#U - UPDATE
def save_to_db():
    db.session.add(User)
    db.session.commit()

def remove_from_db():
    db.session.delete(User)
    db.session.commit()

#D - DELELTE
@app.route('/delete', methods=['DELETE'])
def delete():
    user = User.quary.get(id)
    remove_from_db(user)
    return render_template('delete.html')