#!/usr/bin/env python3
"""
User model
"""
from api.views import db
import bcrypt
from uuid import uuid4


user_group = db.Table(
    'user_group',
    db.Column('user_id', db.String(128), db.ForeignKey('users.id')),
    db.Column('group_id', db.String(128), db.ForeignKey('groups.id'))
)



class User(db.Model):
    """
    Defines a User object's attributes and properties
    """
    __tablename__ = 'users'
    id = db.Column(db.String(255), primary_key=True, nullable=False)
    firstName = db.Column(db.String(20), nullable=False)
    lastName = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(70))

    groups = db.relationship(
        'Group',
        secondary=user_group,
        backref='members'
    )

    def __init__(self):
        """
        Class constructor
        """
        self.id = str(uuid4())

    def set_password(self, password):
        """
        Hashes the password and sets it to the user password attribute
        """
        salt = bcrypt.gensalt()
        password = password.encode('utf-8')
        hashed_pw = bcrypt.hashpw(password, salt)
        hashed_pw_str = hashed_pw.decode('utf-8')
        self.password = hashed_pw_str

    def check_password(self, password):
        """
        Checks if the password if password valid
        """
        hashed_pw = password.encode('utf-8')
        user_pw = self.password.encode('utf-8')
        return bcrypt.checkpw(hashed_pw, user_pw)