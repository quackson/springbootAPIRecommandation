from flask import Flask, request, json, Response
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)