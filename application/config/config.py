from application.config.autoload import *

mongo = PyMongo()

def config_app(app):
    app.config['MONGO_URI'] = 'mongodb://admin:admin@portal.bisaai.id:27017/digileaps'
    mongo.init_app(app)
    return app

def config_jwt(app):
    app.config['SECRET_KEY'] = 'thisisthesecretkey'
    return app
