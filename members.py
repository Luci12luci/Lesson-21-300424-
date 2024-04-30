from main import db


class Genres(db.Model):
    __tablename__ = "members"

    member_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    email = db.Column(db.String(), unique=True)
    password = db.Column(db.String(255), nullable=False)
    registration_date = db.Column(db.DateTime)

