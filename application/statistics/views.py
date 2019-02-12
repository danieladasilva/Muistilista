from application import app, db, login_required
from application.auth.models import User
from flask import redirect, render_template, request, url_for


@app.route("/statistics", methods=["GET"])
def statistics_index():
    return render_template("statistics/list.html", undone_tasks=User.find_users_with_undone_tasks())
