from application.config.config import *

contoh = Blueprint('contoh', __name__, static_folder = 'application/upload/foto_contoh', static_url_path="/media")

@contoh.route('/get_contoh',methods=['GET','POST'])
def index():
    return str(sys.version)

@contoh.route('/oauth',methods=['GET','POST'])
def oauth():
    oauth = OAuth2Provider()
    oauth.init_app(contoh)
    return 'oauth'

@contoh.route("/mongodb", methods=["GET","POST"])
def home_page():
    # print(dict(request.args))
    if request.args:
        return json_response(mongo_loads(mongo.db.berita.find(dict(request.args), field=['judul'])))
    else:
        return json_response(mongo_loads(mongo.db.berita.find(), field=['judul']))

    # return make_response(jsonify([{item for item in data if item != '_id'} for data in mongo.db.berita.find()]))
    # return make_response(jsonify(mongo.db.berita.find()[0]))