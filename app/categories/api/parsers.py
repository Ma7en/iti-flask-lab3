from flask_restful import reqparse

categories_parser = reqparse.RequestParser()

categories_parser.add_argument("name", type=str, required=True, help="Name is required")
categories_parser.add_argument(
    "image", type=str, required=True, help="Image is required"
)


# name = db.Column(db.String(100), nullable=True)
# image = db.Column(db.String(250), nullable=True)
# blogs = db.relationship("Blogs", backref="category", lazy=True)
