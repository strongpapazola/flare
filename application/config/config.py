from application.config.autoload import *
from flask_pymongo import PyMongo

def main():
    app = Flask(__name__)
    app.config['MONGO_URI'] = 'mongodb://admin:admin@portal.bisaai.id:27017/test'
    mongo = PyMongo(app)
    return app, mongo


def init_mongo(app):
    return PyMongo(app)


