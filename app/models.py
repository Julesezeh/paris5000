from extensions import db

class Users(db.Model):
    username  = db.Column(db.String(100))
    name = db.Column(db.String(200))
    # date_of_birth = db.Column(db)....date field
