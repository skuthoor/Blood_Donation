from donation import app
from flask import render_template, url_for ,redirect,url_for,flash, request
from donation.models import user
from donation.forms import registerform #, loginform
from donation import db
#from flask_login import login_user, logout_user,login_required, current_user




@app.route('/')
def home_page():
	return render_template('home.html')

@app.route('/register', methods=['GET','POST'])
def register_page():
	form = registerform()
	if form.validate_on_submit():
		user_to_create= user(username=form.username.data, email_address=form.email_address.data, blood_grp=form.blood_grp.data, password_hash=form.password1.data)
		db.session.add(user_to_create)
		db.session.commit()
		return redirect(url_for('home_page'))

		flash('Accout created sucessfully!')

	return render_template('register.html',form=form)


@app.route('/login')
def login_page():
	form = loginform()
	return render_template('login.html',form=form)
	