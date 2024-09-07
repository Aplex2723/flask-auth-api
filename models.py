from flask_pymongo import PyMongo
import certifi

print("CERTIFICATION")
print(certifi.where())

mongo = PyMongo(tlsCAFile=certifi.where(), tls=True)

def init_db(app):
    mongo.init_app(app)

