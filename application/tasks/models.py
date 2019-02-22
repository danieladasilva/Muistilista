from application import db
from application.models import Base


class Task(Base):

    name = db.Column(db.String(144), nullable=False)
    done = db.Column(db.Boolean, nullable=False)

    #FOREIGN KEY
    #Task-taulussa viittaus Account-tauluun
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)
    #FOREIGN KEY
    #Task-taulussa viittaus Account-tauluun
    # group_id = db.Column(db.Integer, db.ForeignKey('group.id'),
                           nullable=False)

    def __init__(self, name):
        self.name = name
        self.done = False
