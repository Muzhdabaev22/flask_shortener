import datetime
import random
import string


from . import db

SHORT_LEN = 6


def get_short():
    while True:
        short = "".join(random.choices(string.ascii_letters + string.ascii_letters, k=6))
        if URLModel.query.filter(URLModel.short == short).first():
            continue
        return short


class URLModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(255), unique=True)
    short = db.Column(db.String(SHORT_LEN ), unique=True)
    visits = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now())
