from flask import render_template, request, redirect, url_for, Blueprint, flash
from werkzeug.utils import secure_filename
import os, datetime

# flask login
from flask_login import (
    LoginManager,
    UserMixin,
    login_user,
    logout_user,
    current_user,
    login_required,
)

# app db
from app.models import db, User
from app.models import Blogs
from app.models import Categories

# user
from app.user import users_blueprint
from app.user.login_forms import LoginForm
from app.user.register_forms import RegisterForm

login_manager = LoginManager()


# =================================================================================================
# *** loader user ***
# @login_manager.user_loader
# def loader_user(user_id):
#     return User.query.get(user_id)


# =================================================================================================
# *** current user ***
@users_blueprint.route("profile", endpoint="profile", methods=["GET", "POST"])
@login_required
def user_profile():
    user = current_user
    # print(user.username)

    blogs = Blogs.query.filter_by(user_id=user.id).all()
    # print("------------------------------")
    # print(blogs)
    # print("------------------------------")
    blogs = Blogs.query.filter_by(user_id=user.id).all()
    categories = Categories.query.filter_by(user_id=user.id).all()

    # return render_template("profile.html", user=user, blogs=blogs)
    return render_template(
        "user/profile.html", user=user, blogs=blogs, categories=categories
    )


# =================================================================================================
# *** Register user ***
@users_blueprint.route("register", endpoint="register", methods=["GET", "POST"])
def user_register():
    # print("------------------------------")
    # # print(request)  # <Request 'http://127.0.0.1:5000/account/register' [POST]>
    # print(request.form)  #
    # # print(request.form["password"])  #
    # print("-------------------------------")
    form = RegisterForm()
    date = datetime.datetime.now()
    default_image = "default_image.png"

    if request.method == "POST":
        if form.validate_on_submit():
            con_name = default_image

            if request.files.get("image"):
                image = form.image.data
                image_name = secure_filename(image.filename)
                # con_name = f"{date.strftime('%Y%m%d%H%M%S')}_{image_name}"
                con_name = f"{date.day}-{date.hour}-{date.minute}-{image_name}"
                image.save(os.path.join("static/assets/images/user/", con_name))

            data = dict(request.form)
            del data["csrf_token"]
            del data["submit"]

            data["image"] = con_name

            user = User(**data)
            db.session.add(user)
            db.session.commit()

        return redirect(url_for("user.login"))
    return render_template("user/sign_up.html", form=form)


# =================================================================================================
# *** login user ***
@users_blueprint.route("login", endpoint="login", methods=["GET", "POST"])
def user_login():
    # print("------------------------------")
    # print(request)
    # print("------------------------------")
    # user = Users.query.filter_by(username=request.form.get("username")).first()
    # if user and user.password == request.form.get("password"):
    #     login_user(user)
    #     return redirect(url_for("home"))
    print("------------------------------")
    print("request.form")
    print(request.form)
    print("------------------------------")
    form = LoginForm()
    if request.method == "POST":
        if form.validate_on_submit():
            user = User.query.filter_by(email=request.form["email"]).first()
            print("------------------------------")
            print("user")
            print(user)
            print("------------------------------")
            if user and user.password == request.form["password"]:
                u = login_user(user)
                print("------------------------------")
                print(u)
                print("------------------------------")
                return redirect(url_for("blogs.list"))
    return render_template("user/login.html", form=form)


# =================================================================================================
# *** logout user ***
@users_blueprint.route("logout", endpoint="logout", methods=["GET"])
def user_logout():
    logout_user()
    return redirect(url_for("user.login"))
