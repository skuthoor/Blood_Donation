from donation import db#, login_manager
from donation import bcrypt
#from flask_login import UserMixin

#@login_manager.user_loader
#def load_user(user_id):
 #   return user.query.get(int(user_id))


class user(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False )
    email_address = db.Column(db.String(length=50), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)                         #to encript the password using hash
    blood_grp = db.Column(db.String(length=6), nullable= False)

    @property
    def password(self):
    	return self.password

    @password.setter
    def password(self,plain_text_password):
    	self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')
    
    
      
