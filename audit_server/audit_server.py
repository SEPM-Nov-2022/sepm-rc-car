"""Audit Server Mock"""
from flask import Flask
from flask_restful import Api, Resource, request

# creates the server
app = Flask(__name__)
api = Api(app)


class ToyEntry(Resource):
    """Create the Resource"""
    def get(self, uuid):
        """echo service"""
        return f'echo {uuid}', 200

    def post(self, uuid):
        """maps HTTP POST to create a new entry"""
        print(f'received for uuid {uuid}: {request.get_json()}')
        return 'ok', 201


# maps the class Toy to a specific url
api.add_resource(ToyEntry, "/toy/<string:uuid>/")

app.run(debug=False)
