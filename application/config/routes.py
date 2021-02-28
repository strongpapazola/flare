from application.config.config import *
from application.controller.contoh.controller import contoh

app = Flask(__name__)
app = config_app(app)
app.register_blueprint(contoh,url_prefix='/contoh')

if "__main__" == __name__:
    app.run(debug=True, port=9090)

# if "__main__" == __name__:
#     app.run()
