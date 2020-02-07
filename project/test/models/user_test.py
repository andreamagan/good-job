from flask_testing import TestCase
from nose.tools import assert_equal, assert_is_none, assert_is_not_none, assert_raises
from pymysql import IntegrityError
from sqlalchemy.exc import IntegrityError

from project import app, db
from project.models.user import User, UserStatus


class UserTest(TestCase):
    # ----------------------------
    # Test configuration
    # ----------------------------
    def create_app(self):
        return app

    def setUp(self):
        db.create_all()

        user1 = User(email='user1@goodjob.com', password_hash='asdivfdndv')
        user2 = User(email='user2@goodjob.com', password_hash='zcczxczxzc')
        user3 = User(email='user3@goodjob.com', password_hash='r4rwdds323')
        user4 = User(email='user4@goodjob.com', password_hash='klsdcsdjkj')

        db.session.add(user1)
        db.session.add(user2)
        db.session.add(user3)
        db.session.add(user4)

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    # ----------------------------
    # Test cases
    # ----------------------------
    def test_create_user_and_find_by_id(self):
        user = User(email='user@goodjob.com', password_hash='klsdcsdjkj')

        db.session.add(user)
        db.session.flush()

        u = User.query.filter_by(id=user.id).first()

        assert_equal(u.id, user.id)

    def test_delete_user_and_find_by_email(self):
        user = User.query.filter_by(email='user4@goodjob.com').first()
        assert_is_not_none(user)

        db.session.delete(user)

        u = User.query.filter_by(email='user4@goodjob.com').first()
        assert_is_none(u)

    def test_get_all_enabled_user(self):
        users = User.query.filter_by(status=UserStatus.ACTIVE).all()
        assert_equal(len(users), 0)

        u1 = User.query.filter_by(email='user1@goodjob.com').first()
        u2 = User.query.filter_by(email='user2@goodjob.com').first()
        u3 = User.query.filter_by(email='user3@goodjob.com').first()

        u1.status = UserStatus.ACTIVE
        u2.status = UserStatus.ACTIVE
        u3.status = UserStatus.ACTIVE

        users = User.query.filter_by(status=UserStatus.ACTIVE).all()
        assert_equal(len(users), 3)

    def test_get_non_exists_user(self):
        u = User.query.filter_by(email='us3r@goodjob.com').first()
        assert_is_none(u)

    def test_duplicate_user_email(self):
        with assert_raises(IntegrityError):
            user = User(email='user1@goodjob.com', password_hash='klsdcsdjkj')
            db.session.add(user)
            db.session.flush()
            print(user.removed_date)

