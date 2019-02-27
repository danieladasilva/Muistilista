from application import db
from application.models import Base
from flask_login import current_user
from sqlalchemy.sql import text


class Task(Base):

    name = db.Column(db.String(144), nullable=False)
    done = db.Column(db.Boolean, nullable=False)

    #FOREIGN KEY
    #Task-taulussa viittaus Account-tauluun
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)
    #FOREIGN KEY
    #Task-taulussa viittaus Account-tauluun
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'),
                           nullable=False)

    def __init__(self, name):
        self.name = name
        self.done = False

    @staticmethod
    def find_undone_tasks():
        stmt = text("SELECT DISTINCT Task.name, Task.group_id, Task.id FROM Task"
                     " LEFT JOIN Account ON Account.id = Task.account_id"
                     " WHERE (Task.done = :false) AND (Task.account_id = :currentid)").params(false = False, currentid=current_user.id)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"name":row[0], "group_id":row[1], "id":row[2]})

        return response

    @staticmethod
    def find_done_tasks():
        stmt = text("SELECT DISTINCT Task.name, Task.group_id, Task.id FROM Task"
                    " LEFT JOIN Account ON Account.id = Task.account_id"
                    " WHERE (Task.done = :true) AND (Task.account_id = :currentid)").params(true = True, currentid=current_user.id)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"name":row[0], "group_id":row[1], "id":row[2]})

        return response
