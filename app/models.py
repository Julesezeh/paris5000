from extensions import db

class Courts(db.Model):
    city = db.Column(db.String(30))