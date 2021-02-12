from application.config.autoload import *
from application.config.config import *

from application.controller.contoh.controller import contoh

app = Flask(__name__)
app = flare_config(app)
app.register_blueprint(contoh,url_prefix='/contoh')

if "__main__" == __name__:
    app.run()
