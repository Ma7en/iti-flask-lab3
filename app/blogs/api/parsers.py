from flask_restful import reqparse

blogs_parser = reqparse.RequestParser()

blogs_parser.add_argument("name", type=str, required=True, help="Name is required")
blogs_parser.add_argument(
    "description", type=str, required=True, help="Description is required"
)
blogs_parser.add_argument("image", type=str, required=True, help="Image is required")
blogs_parser.add_argument(
    "category_id", type=int, required=True, help="Category ID is required"
)


# "name": fields.String,
# "description": fields.String,
# "image": fields.String,
# "category_id": fields.Integer,
# "category": fields.Nested(category_serializers),
