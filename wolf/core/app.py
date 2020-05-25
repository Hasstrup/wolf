from flask import Flask
from ..controllers.applications import ApplicationsController

app = Flask(__name__)

app.route("/applications", methods=["GET"])
ApplicationsController().index()
