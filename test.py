from flask import Flask, make_response, jsonify
from flask_pymongo import PyMongo, MongoClient
import json
from flask_oauthlib.provider import OAuth2Provider

app = Flask(__name__)
app.config['MONGO_URI'] = "mongodb://admin:admin@portal.bisaai.id:27017/digileaps"
oauth = OAuth2Provider(app)
mongo = PyMongo(app)
# app.config['MONGOALCHEMY_DATABASE'] = 'library'
# db = MongoAlchemy(app)
# oauth = OAuth2Provider(app)

@app.route('/')
def root():
    # documents = [i for i in mongo.db.berita.find()]
    # output = [{item: data[item] for item in data if item != '_id'} for data in documents]
    # for data in documents:
    for item in mongo.db.berita.find()[1]:
        # if item != '_id':
        print("AWAL =====================")
        print(type(item))
        print(item)
        print("AKHIR =====================")
        print(type(mongo.db.berita.find()[1][item]))
        print(mongo.db.berita.find()[1][item])
    # return make_response(jsonify(output)), 200
    return make_response(jsonify({item: mongo.db.berita.find()[1][item] for item in mongo.db.berita.find()[1] if item != '_id'})), 200
    # return 'lol'

if "__main__" == __name__:
    app.run(debug=True, port=9090)