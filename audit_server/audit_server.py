"""Audit Server Mock"""
import json
from flask import Flask
from flask_restful import Api, Resource, reqparse

# creates the server
app = Flask(__name__)
api = Api(app)

class ToyEntry(Resource):
    """Create the Resource"""
    def post(self, uuid):
        """maps HTTP POST to create a new entry"""
        # parses the input
        parser = reqparse.RequestParser()
        parser.add_argument("timestamp")
        parser.add_argument("value")
        args = parser.parse_args()

        # builds the model
        toy_entry = {
            "uuid": uuid,
            "timestamp": args["timestamp"]
        }

        # logs the entry
        with open("audit_entries.log", "a", encoding="UTF-8") as file:
            file.write(f'{json.dumps(toy_entry)}\n')

        return toy_entry, 201

# maps the class Toy to a specific url
api.add_resource(ToyEntry, "/toy/<string:uuid>/")

app.run(debug=False)
