import subprocess, os, logging
from app import create_app
from app.database.db import db

app = create_app('app.config.')

if __name__ == "__main__":
    app.run(debug=True)