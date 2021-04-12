from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

drinks_data = {"palinca": {"grade": 52},
                "vodka": {"grade": 40}}

class Drinks(Resource):
    def get(self, name):
        return drinks_data[name]

    def put(self, name):
        return 

api.add_resource(Drinks, "/drinks/<string:name>/")


if __name__ == "__main__":
    app.run(debug=True)