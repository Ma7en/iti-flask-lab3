from flask_sqlalchemy import SQLAlchemy
from flask import url_for

db = SQLAlchemy()


class Categories(db.Model):
    __tablename__ = "categories"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=True)
    image = db.Column(db.String(250), nullable=True)
    blogs = db.relationship("Blogs", backref="category", lazy=True)

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


class Blogs(db.Model):
    __tablename__ = "blogs"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=True)
    description = db.Column(db.String(5000), nullable=True)
    image = db.Column(db.String(250), nullable=True)
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"), nullable=True)

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
