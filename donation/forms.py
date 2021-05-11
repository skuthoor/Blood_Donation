from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, HiddenField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from donation.models import user

class registerform(FlaskForm):
	def validate_email_address(self, email_address_to_check):
		email_addresss = user.qurey.filter_by(email_addresss = email_address_to_check.data).first()
		if email_addresss :
			raise ValidationError('Email already exits! Please try a different Email')

	username = StringField(label='Name', validators=[Length(min=2,max=30),DataRequired()])
	email_address = StringField(label="Email Address", validators=[Email(),DataRequired()])
	blood_grp = StringField(label='Blood Group ',validators=[Length(max=6), DataRequired()])
	password1 = PasswordField(label='Password1', validators=[Length(min=5), DataRequired()])
	password2 = PasswordField(label='Password2',validators=[EqualTo('password1'), DataRequired()])
	submit = SubmitField('Create Account')