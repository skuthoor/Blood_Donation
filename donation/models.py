from donation import db, login_manager
from donation import bcrypt
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return user.query.get(int(user_id))


class user(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False )
    email_address = db.Column(db.String(length=50), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)                         #to encript the password using hash
    blood_grp = db.Column(db.String(length=7), nullable= False)
    mobile_no = db.Column(db.Integer(), nullable= False,unique=True)
    district = db.Column(db.String(),nullable= False)



    @property
    def password(self):
    	return self.password

    @password.setter
    def password(self,plain_text_password):
    	self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')
    
    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)


class category(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key= True)
    category = db.Column(db.String())
    category_id = db.relationship('blood_bank', backref='Category', lazy=True)

class district(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key= True)
    district = db.Column(db.String())
    district_id = db.relationship('blood_bank', backref='District', lazy=True)

class govt_pvt(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key= True)
    govt_pvt = db.Column(db.String())
    govt_pvt_id = db.relationship('blood_bank', backref='Govt_Pvt', lazy=True)

class blood_bank(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key= True)
    name = db.Column(db.String())
    address = db.Column(db.String())
    district_id = db.Column(db.Integer(), db.ForeignKey('district.id'))
    govt_pvt_id = db.Column(db.Integer(), db.ForeignKey('govt_pvt.id'))
    category_id = db.Column(db.Integer(), db.ForeignKey('category.id'))
    blood_bank_id = db.relationship('blood', backref='Blood', lazy=True)
    #name_id = db.relationship('userbank', backref='Namebloodbank', lazy=True)

class blood(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key= True)
    blood_bank_id = db.Column(db.Integer(), db.ForeignKey('blood_bank.id'))
    A_positive = db.Column(db.Integer()) 
    B_positive = db.Column(db.Integer()) 
    AB_positive = db.Column(db.Integer()) 
    O_positive = db.Column(db.Integer()) 
    A_negative = db.Column(db.Integer()) 
    B_negative = db.Column(db.Integer()) 
    AB_negative = db.Column(db.Integer()) 
    O_negative = db.Column(db.Integer()) 

class userbank(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key= True)
    district_id = db.Column(db.String())
    name_id = db.Column(db.String())
    password_hash = db.Column(db.String(length=60), nullable=False)  

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self,plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')
    
    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)




class doctor(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(), nullable=False )
    email_address = db.Column(db.String(), nullable=False, unique=True)
    mobile_no = db.Column(db.Integer(), nullable= False,unique=True)
    password_hash = db.Column(db.String(), nullable=False)   

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self,plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')
    
    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)





