from application import db, bcrypt
from application.models import Base
from sqlalchemy.sql import text

#Account-tietokantataulu
class User(Base):
    #tietokantataulun nimi
    __tablename__ = "account"

    #tietokantataulun sarakkeet
    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)

    #Task-taulussa viittaus Account-tauluun
    tasks = db.relationship("Task", backref='account', lazy=True)

    def __init__(self, name, password):
        self.name = name
        self.username = name
        self.password = bcrypt.generate_password_hash(password, 15).decode('utf-8')

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def roles(self):
        return ["ADMIN"]

    def is_correct_password(self, password):
        return bcrypt.check_password_hash(self.password, password)

    @staticmethod
    def find_users_with_undone_tasks():
        stmt = text("SELECT DISTINCT Account.id, Account.name FROM Account"
                     " LEFT JOIN Task ON Task.account_id = Account.id"
                     " WHERE (Task.done = :false)").params(false = False)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1]})

        return response
