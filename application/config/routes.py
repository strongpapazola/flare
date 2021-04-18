from application.config.config import *
from application.helper import * #error root
from application.controller.berita.controller import berita
# from application.controller.komentar.controller import komentar
from application.controller.users.controller import users
# from application.controller.kategori.controller import kategori

app = Flask(__name__)
app = config_app(app)
app = config_jwt(app)
app = handle_error(app)

app.register_blueprint(berita,url_prefix='/berita')
# app.register_blueprint(komentar,url_prefix='/komentar')
app.register_blueprint(users,url_prefix='/users')
# app.register_blueprint(kategori,url_prefix='/kategori')


# if "__main__" == __name__:
#     app.run(debug=True, port=9090)

# if "__main__" == __name__:
#     app.run()
