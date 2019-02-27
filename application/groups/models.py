from application import db
from application.models import Base

class Group(Base):
    #tietokantataulun sarakkeet
    name = db.Column(db.String(144), nullable=False)

    #Task-taulussa viittaus Group-tauluun
    tasks = db.relationship("Task", backref='group', lazy=True)

    def __init__(self, name):
        self.name = name
