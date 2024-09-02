from flask import render_template, request, redirect, url_for, Blueprint
from app.models import Categories, db
from app.categories import categories_blueprint

# from app.blogs.forms import BlogsForm


# ================================================================================
@categories_blueprint.route("/", endpoint="list")
def categories_list():
    categories = Categories.query.all()
    return render_template("categories/list.html", categories=categories)


@categories_blueprint.route("create", endpoint="create", methods=["GET", "POST"])
def categories_create():
    if request.method == "POST":
        category = Categories(
            name=request.form["name"],
            image=request.form["image"],
        )
        db.session.add(category)
        db.session.commit()
        return redirect(category.show_url)
    return render_template("categories/forms/create.html")


@categories_blueprint.route(
    "<int:id>/update", endpoint="update", methods=["GET", "POST"]
)
def categories_update(id):
    category = db.get_or_404(Categories, id)
    if request.method == "POST":
        categoryobj = category
        categoryobj.name = request.form["name"]
        categoryobj.image = request.form["image"]
        db.session.add(categoryobj)
        db.session.commit()
        return redirect(url_for("categories.list"))

    return render_template("categories/forms/update.html", category=category)


@categories_blueprint.route("<int:id>", endpoint="show")
def category_show(id):
    category = db.get_or_404(Categories, id)
    return render_template("categories/show.html", category=category)


@categories_blueprint.route("<int:id>/delete", endpoint="delete", methods=["POST"])
def categories_delete(id):
    category = db.get_or_404(Categories, id)
    db.session.delete(category)
    db.session.commit()
    return redirect(url_for("categories.list"))
