from application import db
from application.models import Base

class Group(Base):

    name = db.Column(db.String(144), nullable=False)


    task_id = db.Column(db.Integer, db.ForeignKey('task.id'),
                           nullable=True)

    def __init__(self, name):
        self.name = name
