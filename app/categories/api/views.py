from flask_restful import Resource, Api, marshal_with
from app.models import db, Categories
from app.categories.api.seriailzers import categories_serializers
from app.categories.api.parsers import categories_parser


class CategoriesList(Resource):
    @marshal_with(categories_serializers)
    def get(self):
        categories = Categories.query.all()
        return categories, 200

    @marshal_with(categories_serializers)
    def post(self):
        categories_args = categories_parser.parse_args()
        category = Categories(**categories_args)  # dictionary
        db.session.add(category)
        db.session.commit()
        return "category", 201
