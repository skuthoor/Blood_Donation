from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, HiddenField, IntegerField, SelectField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from donation.models import user

class registerform(FlaskForm):
	def validate_email_address(self, email_address_to_check):
		email_address = user.query.filter_by(email_address = email_address_to_check.data).first()
		if email_address :
			raise ValidationError('Email already exits! Please try a different Email')

	username = StringField(label='Name', validators=[Length(min=2,max=30),DataRequired()])
	email_address = StringField(label="Email Address", validators=[Email(),DataRequired()])
	blood_grp = SelectField(label='Blood Group',choices=['A+ve','B+ve','AB+ve','O+ve','A-ve','B-ve','AB-ve','O-ve'])
	mobile_no =  StringField(label='Mobile Number', validators=[Length(min=4),DataRequired()])
	district = SelectField(label='District',choices=[]) #'Thiruvananthapuram', 'Kollam', 'Alappuzha', 'Pathanamthitta', 'Kottayam', 'Idukki', 'Ernakulam', 'Thrissur', 'Palakkad', 'Malappuram', 'Kozhikode', 'Wayanadu', 'Kannur','Kasaragod'
	password1 = PasswordField(label='Password', validators=[Length(min=5), DataRequired()])
	password2 = PasswordField(label='Confirm Password',validators=[EqualTo('password1'), DataRequired()])
	submit = SubmitField('Create Account')

class loginform(FlaskForm):
	email_address = StringField(label='Email Address', validators=[DataRequired()])
	password = PasswordField(label='Password', validators=[DataRequired()])
	submit = SubmitField(label='Log In')


class Blood_bank(FlaskForm):
	district = SelectField(label='district', choices=[])
	name = SelectField(label='Blood_bank', validate_choice=False)
	submit = SubmitField('Show Details')

class registerbankform(FlaskForm):
	district = SelectField(label='District',choices=[])
	name = SelectField(label='Blood_bank', validate_choice=False)
	password1 = PasswordField(label='Password', validators=[Length(min=5), DataRequired()])
	password2 = PasswordField(label='Confirm Password',validators=[EqualTo('password1'), DataRequired()])
	submit = SubmitField('Create Account')

class registerdoctorform(FlaskForm):
	username = StringField(label='Name', validators=[Length(min=2,max=30),DataRequired()])
	email_address = StringField(label="Email Address", validators=[Email(),DataRequired()])
	mobile_no =  StringField(label='Mobile Number', validators=[DataRequired()])
	password1 = PasswordField(label='Password', validators=[Length(min=5), DataRequired()])
	password2 = PasswordField(label='Confirm Password',validators=[EqualTo('password1'), DataRequired()])
	submit = SubmitField('Create Account')

class loginbankform(FlaskForm):
	district = SelectField(label='District',choices=[])
	name = SelectField(label='Blood_bank', validate_choice=False)
	password = PasswordField(label='Password', validators=[DataRequired()])
	submit = SubmitField(label='Log In')

class logindoctorform(FlaskForm):
	email_address = StringField(label='Email Address', validators=[DataRequired()])
	password = PasswordField(label='Password', validators=[DataRequired()])
	submit = SubmitField(label='Log In')

class finddoner(FlaskForm):
	district = SelectField(label='District',choices=[])
	blood_grp = SelectField(label='Blood Group',choices=['A+ve','B+ve','AB+ve','O+ve','A-ve','B-ve','AB-ve','O-ve'])
	submit = SubmitField(label='Send Notification')


class change(FlaskForm):
	blood_grp = SelectField(label='Blood Group',choices=['A+ve','B+ve','AB+ve','O+ve','A-ve','B-ve','AB-ve','O-ve'])
	do = SelectField(label='Add/Sub', choices=['add','subtract'])
	amount =   StringField(label='Unit Of Blood', validators=[DataRequired()])
	submit = SubmitField(label='Confirm Change')




