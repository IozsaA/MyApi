from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)


class DrinkModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    grade = db.Column(db.Integer, nullable=False)



drinks_put_args = reqparse.RequestParser()
drinks_put_args.add_argument("name", type=str, required=True)
drinks_put_args.add_argument("grade", type=int, required=True)


drinks_update_args= reqparse.RequestParser()
drinks_update_args.add_argument("name", type=str)
drinks_update_args.add_argument("grade", type=int)

resource_fields = {
    'id': fields.Integer,
    'name':fields.String,
    'grade':fields.String
}

drinks_data = {}
class Drinks(Resource):
    @marshal_with(resource_fields)
    def get(self, drink_id):
        result = DrinkModel.query.filter_by(id=drink_id).first()
        if not result:
            abort(404,message="Could not find this drink")
        return result

    @marshal_with(resource_fields)
    def put(self, drink_id):
        args = drinks_update_args.parse_args()
        result = DrinkModel.query.filter_by(id=drink_id).first()
        if result:
            abort(409,message="Drink already exists..")
        drink = DrinkModel(id = drink_id, name=args['name'], grade = args['grade'])
        db.session.add(drink)
        db.session.commit()
        return drink, 201

    @marshal_with(resource_fields)
    def patch(self,drink_id):
        args= drinks_put_args.parse_args()
        result = DrinkModel.query.filter_by(id=drink_id).first()
        if not result:
            abort(404, message="Could not find this drink")
        if args['name']:
            DrinkModel.name = args['name']
        if args['grade']:
            DrinkModel.grade = args['grade']
        db.session.commit()
        return result

    def delete(self, drink_id):

        del drinks_data[drink_id]
        return '', 204

api.add_resource(Drinks, "/drink/<int:drink_id>")


if __name__ == "__main__":
    app.run(debug=True)