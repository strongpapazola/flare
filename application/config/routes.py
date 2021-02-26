from application.config.config import *
from application.controller.contoh.controller import contoh

app = create_app(__name__)
app.register_blueprint(contoh,url_prefix='/contoh')

if "__main__" == __name__:
    app.run(debug=True, port=9090)

# if "__main__" == __name__:
#     app.run()
