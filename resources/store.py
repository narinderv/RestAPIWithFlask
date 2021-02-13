from flask_restful import Resource
from models.store import StoreModel

class Store(Resource):
    def get(self, name):
        store = StoreModel.find_item_by_name(name)
        if store is None:
            return {'message': 'Store not found'}, 404
        
        return store.json()

    def post(self, name):
        if StoreModel.find_item_by_name(name):
            return {'error': 'A Store with this name already exists'}, 400
        
        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {'message': 'An error occured while creating the store'},500
        
        return store.json(), 201

    def delete(self, name):
        store = StoreModel.find_item_by_name(name)
        if store:
            store.delete_from_db()
            return {'message': 'Store deleted'}
        return {'message': 'Store does not exist'}


class StoreList(Resource):
    def get(self):
        return {'stores': [store.json() for store in StoreModel.query.all()]}, 200


