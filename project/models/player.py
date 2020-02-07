from uuid import uuid4

from sqlalchemy import DATETIME, UniqueConstraint

from project import db, ma


def generate_uuid():
    return uuid4().hex


# -------------------------------------
# SQLAlchemy Entities
# -------------------------------------
class Player(db.Model):
    id = db.Column(db.String(40), default=generate_uuid, primary_key=True)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    nick_name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text(), nullable=True)
    remove_date = db.Column(DATETIME, nullable=True)
    user_id = db.Column(db.String(40), db.ForeingKey('user.id'))
    __table_arg__ = UniqueConstraint('nick_name', 'remove_date', name='UC_nickname')


# -------------------------------------
# Marshmallow schemas
# -------------------------------------
class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'first_name', 'last_name', 'nick_name', 'description')
