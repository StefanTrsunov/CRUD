from distutils.log import debug
from flask import Flask


app = Flask(__name__)

@app.route('/')
def index():
    return 'hey, this is the homepage'

#C - CREATE
@app.route('/create')
def create():
    return 'hey, this is the create page'

#R - READ
@app.route('/read')
def read():
    return 'hey, this is the read page'

#U - UPDATE
@app.route('/update')
def update():
    return 'hey, this is the update page'

#D - delete
@app.route('/delete')
def delete():
    return 'hey, this is the delete page'

if __name__ == '__main__':
    app.run(debug=True)