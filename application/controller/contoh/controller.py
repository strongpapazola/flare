from application.config.autoload import *

contoh = Blueprint('contoh', __name__, static_folder = 'application/upload/foto_contoh', static_url_path="/media")

@contoh.route('/get_contoh',methods=['GET','POST'])
def index():
    return str(sys.version)

@contoh.route('/oauth',methods=['GET','POST'])
def oauth():
    oauth = OAuth2Provider()
    oauth.init_app(contoh)
    return 'oauth'

@contoh.route("/mongodb")
def home_page():
    mongo = PyMongo(contoh)
    online_users = mongo.db.users.find()
    # online_users = mongo.db.users.find({"online": True})
    return online_users