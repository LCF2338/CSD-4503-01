# To install Flask, first run the following line in the terminal:
# pip install flask

# To import the flash into the project, use the following line:
from flask import Flask

flask_app = Flask(__name__)

from app import routes