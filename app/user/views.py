from flask import render_template, request, redirect, url_for, Blueprint

from app.models import db, Users
from app.account import account_blueprint

from app.account.forms import AccountLoginForm, AccountRegisterForm

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

login_manager = LoginManager()


# =================================================================================================
# *** loader user ***
@login_manager.user_loader
def loader_user(user_id):
    return Users.query.get(user_id)


# =================================================================================================
# *** Register user ***
@account_blueprint.route("/register", endpoint="register", methods=["GET", "POST"])
def account_register():
    if request.method == "POST":
        print("------------------------------")
        print(request)  # <Request 'http://127.0.0.1:5000/account/register' [POST]>
        print(request.form["username"])  #
        print(request.form["password"])  #
        print("------------------------------")
        user = Users(
            username=request.form.get("username"),
            password=request.form.get("password"),
            image=request.form.get("image"),
        )

        db.session.add(user)
        db.session.commit()

        return redirect(url_for("account.login"))
    return render_template("account/sign_up.html")


# =================================================================================================
# *** login user ***
@account_blueprint.route("/login", endpoint="login", methods=["GET", "POST"])
def account_login():
    if request.method == "POST":
        print("------------------------------")
        print(request)
        print("------------------------------")
        # user = Users.query.filter_by(username=request.form.get("username")).first()
        # if user and user.password == request.form.get("password"):
        #     login_user(user)
        #     return redirect(url_for("home"))
    return render_template("account/login.html")


# =================================================================================================
# *** logout user ***
# @account_blueprint.route("/logout")
# def account_logout():
#     logout_user()
#     return redirect(url_for("home"))
