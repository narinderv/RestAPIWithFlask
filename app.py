import os 
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.items import Item, ItemList
from resources.store import Store, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///tempDB.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'abcd@1234'
api = Api(app)

jwt = JWT(app, authenticate, identity)  # /auth endpoint

# GET OR POST http://127.0.0.1:5000/item/name
api.add_resource(Item, '/item/<string:name>')

# GET http://127.0.0.1:5000/items
api.add_resource(ItemList, '/items')

# POST http://127.0.0.1:5000/register
api.add_resource(UserRegister, '/register')

api.add_resource(StoreList, '/stores')
api.add_resource(Store, '/store/<string:name>')

if __name__ == "__main__":
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
