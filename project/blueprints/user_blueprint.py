from flask import Blueprint, request

from project import db
from project.models.user import User, UserSchema

user_blueprint = Blueprint("user", __name__)
user_schema = UserSchema()


@user_blueprint.route("/goodjob/v1/register", methods=['POST'])
def register_user():
    email = request.json.get('email')
    password = request.json.get('password')
    password_confirm = request.json.get('password_confirm')

    if password != password_confirm:
        message = "The passwords do not match"
        code = 400
    else:
        if User.query.filter_by(email=email) is not None:
            message = "Email is not available"
            code = 409
        else:
            user = User(email=email)
            user.hash_password(password)

            db.session.add(user)
            db.session.commit()

            message = user_schema.dump(user)
            code = 200
    return message, code
