from application import app, db, login_required
from application.auth.models import User
from flask import redirect, render_template, request, url_for
from application.tasks.models import Task


@app.route("/statistics", methods=["GET"])
def statistics_index():
    return render_template("statistics/list.html", undone_tasks=User.find_users_with_undone_tasks(), users_undone_tasks=Task.find_undone_tasks(), users_done_tasks=Task.find_done_tasks())
