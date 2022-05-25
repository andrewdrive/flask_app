from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    # email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username) 









# class User(db.Model):

#     __tablename__ = 'user'

#     user_id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(64), index=True, unique=True)
#     password = db.Column(db.String)
#     authenticated = db.Column(db.Boolean, default=False)

#     def is_active(self):
#         """True, as all users are active"""
#         return True

#     def get_id(self):
#         return self.user_id

#     def is_authenticated(self):
#         return self.authenticated
    
#     def is_anonymous(self):
#         """False, as anonymous users aren't supported."""
#         return False 


#     # password_hash = db.Column(db.String(128))

#     # def __repr__(self) -> str:
#     #     return '<User {}>'.format(self.username)