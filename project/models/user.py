from datetime import datetime
from enum import Enum
from sqlalchemy import Enum as SQLEnum, DATETIME, UniqueConstraint
from uuid import uuid4
from passlib.apps import custom_app_context as pwd_context

from project import db, ma


def generate_uuid():
    return uuid4().hex


class UserStatus(Enum):
    INACTIVE = 0
    ACTIVE = 1


# -------------------------------------
# SQLAlchemy Entities
# -------------------------------------
class User(db.Model):
    id = db.Column(db.String(40), default=generate_uuid, primary_key=True)
    email = db.Column(db.String(255), nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    status = db.Column(SQLEnum(UserStatus), default=UserStatus.INACTIVE, nullable=False)
    avatar_uri = db.Column(db.Text(), nullable=True)
    creation_date = db.Column(DATETIME, default=datetime.utcnow, nullable=False)
    modification_date = db.Column(DATETIME, nullable=True)
    activation_date = db.Column(DATETIME, nullable=True)
    removed_date = db.Column(DATETIME, nullable=True)
    __table_args__ = UniqueConstraint('email', 'removed_date', name='UC_email')

    def hash_password(self, clear_password):
        self.password_hash = pwd_context.hash(clear_password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)


# -------------------------------------
# Marshmallow schemas
# -------------------------------------
class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'email', 'avatar_uri', 'creation_date')
