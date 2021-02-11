def flare_config(app):
    app.config['MONGO_URI'] = 'mongodb://localhost:27017/test'
    return app


