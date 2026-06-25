from flask import Flask, abort
from flask_session import Session

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

app = Flask(__name__)

app.config['SECRET_KEY'] = "<key>"

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

uri = "mongodb+srv://kim169_db_user:<key>@dietsprintdb.uw39zbi.mongodb.net/"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    abort(408)

from application.routes import error_handlers
from application.routes import about
from application.routes import main
from application.routes import register
