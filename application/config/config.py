from application.config.autoload import *

mongo = PyMongo()

def create_app(name):
    app = Flask(name)
    app.config['MONGO_URI'] = 'mongodb://admin:admin@portal.bisaai.id:27017/digileaps'
    mongo.init_app(app)
    return app

# class Config(object):
#     def __init__(self, app=None, uri=None, *args, **kwargs):
#         if app is not None:
#             self.init_app(app, uri, *args, **kwargs)

    # def init():
    #     app = Flask(__name__)
    #     app.config['MONGO_URI'] = 'mongodb://admin:admin@portal.bisaai.id:27017/test'

    # def init_mongo():
    #     self.init().app


