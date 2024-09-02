from flask import Flask
from flask_migrate import Migrate
from app.models import db
from app.config import config_options
from flask_bootstrap import Bootstrap5
from flask_restful import Resource, Api
from app.blogs.api.views import BlogsList, BlogsResource
from app.categories.api.views import CategoriesList


def create_app(config_name="prd"):
    app = Flask(__name__)

    current_config = config_options[config_name]
    app.config.from_object(current_config)
    app.config.SQLALCHEMY_DATABASE_URI = current_config.SQLALCHEMY_DATABASE_URI

    db.init_app(app)
    migrate = Migrate(app, db)

    # packages
    bootstrap = Bootstrap5(app)
    api = Api(app)

    # Apps
    # -1 -> Blogs
    from app.blogs import blogs_blueprint

    app.register_blueprint(blogs_blueprint)

    # -2 -> Categories
    from app.categories import categories_blueprint

    app.register_blueprint(categories_blueprint)

    # API
    # -1 -> Blogs
    api.add_resource(BlogsList, "/api/blogs")
    api.add_resource(BlogsResource, "/api/blogs/<int:id>")

    # -2 -> Categories
    api.add_resource(CategoriesList, "/api/categories")

    return app
