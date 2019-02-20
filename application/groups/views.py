from application import app, db, login_required
from flask import redirect, render_template, request, url_for

from application.groups.models import Group
from application.groups.forms import GroupForm
from flask_login import current_user

@app.route("/groups", methods=["GET"])
def groups_index():
    return render_template("groups/list.html", groups = Group.query.all())

@app.route("/groups/new/")
@login_required(role="ADMIN")
def groups_form():
    return render_template("groups/new.html", form = GroupForm())

@app.route("/groups/", methods=["POST"])
@login_required(role="ADMIN")
def groups_create():
    form = GroupForm(request.form)

    if not form.validate():
        return render_template("groups/new.html", form = form)

    t = Group(form.name.data)


    db.session().add(t)
    db.session().commit()

    return redirect(url_for("groups_index"))
