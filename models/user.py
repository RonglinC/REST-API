import sqlite3
from db import db

# extend db model
class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key =True)
    username = db.Column(db.String(80)) # limit the size of string
    password = db.Column(db.String(80))

    def __init__(self,username,password):
        self.username = username
        self.password = password
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


    @classmethod #use the current class
    def find_by_username(cls,username):
        return cls.query.filter_by(username=username).first()
    
    @classmethod #use the current class
    def find_by_id(cls,_id):
        return cls.query.filter_by(id=_id).first()