from flask_sqlalchemy import SQLAlchemy
from flask import url_for
from flask_login import UserMixin

# db
db = SQLAlchemy()


# =================================================================================================
# *** Users ***
class User(db.Model, UserMixin):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(250), nullable=False)
    last_name = db.Column(db.String(250), nullable=False)
    username = db.Column(db.String(250), unique=True, nullable=False)
    email = db.Column(db.String(250), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)
    image = db.Column(db.String(250), nullable=True)
    blogs = db.relationship("Blogs", backref="created_blogs", lazy=True)
    categories = db.relationship("Categories", backref="user_category", lazy=True)

    def __str__(self):
        return f"{self.username}"

    @property
    def image_url(self):
        return url_for("static", filename=f"assets/images/user/{self.image}")


# =================================================================================================
# *** Categories ***
class Categories(db.Model):
    __tablename__ = "categories"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=True)
    image = db.Column(db.String(250), nullable=True)
    blogs = db.relationship("Blogs", backref="category_ref", lazy=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=True)
    # user = db.relationship("User", backref=db.backref("categories", lazy=True))
    # user = db.relationship("User", backref=db.backref("categories", lazy=True))
    # user = db.relationship("User", backref=db.backref("categories", lazy="dynamic"))

    def __str__(self):
        return f"{self.name}"

    @property
    def image_url(self):
        return url_for("static", filename=f"assets/images/categories/{self.image}")

    @property
    def show_url(self):
        return url_for("categories.show", id=self.id)

    @property
    def update_url(self):
        return url_for("categories.update", id=self.id)

    @property
    def delete_url(self):
        return url_for("categories.delete", id=self.id)


# =================================================================================================
# *** Blogs ***
class Blogs(db.Model):
    __tablename__ = "blogs"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=True)
    description = db.Column(db.String(5000), nullable=True)
    image = db.Column(db.String(250), nullable=True)
    # category_id = db.Column(db.Integer, db.ForeignKey("categories.id"), nullable=True)
    # user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=True)
    # category = db.relationship("Categories", backref=db.backref("blogs_ref", lazy=True))
    # user = db.relationship("User", backref=db.backref("blogs", lazy=True))
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=True)
    category = db.relationship("Categories", backref=db.backref("blogs_ref", lazy=True))
    user = db.relationship("User", backref="created_blogs")

    def __str__(self):
        return f"{self.name}"

    @property
    def image_url(self):
        return url_for("static", filename=f"assets/images/blogs/{self.image}")

    @property
    def show_url(self):
        return url_for("blogs.show", id=self.id)

    @property
    def update_url(self):
        return url_for("blogs.update", id=self.id)

    @property
    def delete_url(self):
        return url_for("blogs.delete", id=self.id)
