from app.models import Blogs, db
from flask import render_template, request, redirect, url_for, Blueprint
from app.blogs import blogs_blueprint


@blogs_blueprint.route("/", endpoint="list")
def blogs_list():
    blogs = Blogs.query.all()
    return render_template("blogs/list.html", blogs=blogs)


@blogs_blueprint.route("create", endpoint="create", methods=["GET", "POST"])
def blogs_create():
    # print(request.method, request.form)
    if request.method == "POST":
        blog = Blogs(
            name=request.form["name"],
            description=request.form["description"],
            image=request.form["image"],
        )
        db.session.add(blog)
        db.session.commit()
        return redirect(blog.show_url)

    return render_template("blogs/create.html")


@blogs_blueprint.route("<int:id>/update", endpoint="update", methods=["GET", "POST"])
def blogs_update(id):
    blog = db.get_or_404(Blogs, id)
    if request.method == "POST":
        # print("requested blog----------->\n", request.form)
        # print("-==->", request.POST["name"])
        # print("-==->", request.form["name"])
        blogobj = blog
        blogobj.name = request.form["name"]
        blogobj.description = request.form["description"]
        blogobj.image = request.form["image"]
        db.session.add(blogobj)
        db.session.commit()
        return redirect(url_for("blogs.list"))

    return render_template("blogs/update.html", blog=blog)


@blogs_blueprint.route("<int:id>", endpoint="show")
def blog_show(id):
    blog = db.get_or_404(Blogs, id)
    return render_template("blogs/show.html", blog=blog)


@blogs_blueprint.route("<int:id>/delete", endpoint="delete", methods=["POST"])
def blogs_delete(id):
    blog = db.get_or_404(Blogs, id)
    db.session.delete(blog)
    db.session.commit()
    return redirect(url_for("blogs.list"))


# use -> url_for
# @blogs_blueprint.route("<int:id>/delete", endpoint="delete")
# def blogs_delete(id):
#     blog = db.get_or_404(Blogs, id)
#     db.session.delete(blog)
#     db.session.commit()
#     return redirect(url_for("blogs.list"))
