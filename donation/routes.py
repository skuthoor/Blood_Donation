from donation import app
from flask import render_template, url_for #,redirect,url_for,flash, request
from donation.models import user
from donation.forms import registerform #, loginform, PurchaseItemForm, SellItemForm
from donation import db
#from flask_login import login_user, logout_user,login_required, current_user




@app.route('/')
def home_page():
	return render_template('home.html')

@app.route('/register')
def register_page():
	form = registerform()
	return render_template('register.html',form=form)


'''@app.route('/login')
def login_page():
	form = loginform()
	return render_template('login.html',form=form)
	'''