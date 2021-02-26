from application.config.autoload import *
from application.config.config import *

from application.controller.contoh.controller import contoh

app, null = main()
app.register_blueprint(contoh,url_prefix='/contoh')

if "__main__" == __name__:
    app.run()
