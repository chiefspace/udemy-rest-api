from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import RegisterUser
from resources.item import Item, ItemList

app = Flask(__name__)
app.secret_key = 'P@ssw0rd'
api = Api(app)

jwt = JWT(app, authenticate, identity)  # The jwt object creates a new endpoing called /auth
      
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(RegisterUser, '/register')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
