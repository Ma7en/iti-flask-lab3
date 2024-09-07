from flask import render_template, request, redirect, url_for, Blueprint
from werkzeug.utils import secure_filename
import os, datetime
from flask_login import login_required, current_user

# app
from app.home import home_blueprint


# =================================================================================================
# *** list categories ***
@home_blueprint.route("/", endpoint="home")
def home():
    return render_template("home/home.html")
