from application.config.autoload import *

def json_response(dictionary):
    return make_response(jsonify(dictionary))
