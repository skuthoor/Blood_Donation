from donation import app
from flask import render_template, url_for ,redirect,url_for,flash, request
from donation.models import user
from donation.forms import registerform , loginform
from donation import db
from flask_login import login_user, logout_user,login_required, current_user




@app.route('/')
def home_page():
	return render_template('home.html')


@app.route('/register', methods=['GET','POST'])
def register_page():
	form = registerform()
	if form.validate_on_submit():
		user_to_create= user(username=form.username.data, email_address=form.email_address.data, blood_grp=form.blood_grp.data, mobile_no=form.mobile_no.data, district=form.district.data , password=form.password1.data)
		db.session.add(user_to_create)
		db.session.commit()
		login_user(user_to_create)
		flash(f'Account created sucessfully! You are now logged in as: {user_to_create.username}')
		return redirect(url_for('home_page'))
	if form.errors !={}:
		for err_msg in form.error.values():
			flash(f'There was an error in creating the user:{err_msg}',category='danger')
		

	return render_template('register.html',form=form)


@app.route('/login', methods=['GET','POST'])
def login_page():
	form = loginform()
	if form.validate_on_submit():
		attempted_user = user.query.filter_by(email_address=form.email_address.data).first()
		if attempted_user and attempted_user.check_password_correction(attempted_password=form.password.data):
			login_user(attempted_user)
			flash(f'Sucess! You are logged in as: {attempted_user.username}',category = 'success')
			return redirect(url_for('home_page'))
		else:
			flash('Username or Password is incorrect! Please try again', category= 'danger')


	return render_template('login.html',form=form)


@app.route('/logout')
def logout_page():
	logout_user()
	flash('You have been logged out!',category='info')
	return redirect(url_for('home_page'))
	