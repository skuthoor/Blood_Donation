from donation import app, index
from flask import render_template, url_for ,redirect,url_for,flash, request, jsonify, json
from donation.models import user, category, district, govt_pvt, blood_bank, userbank, doctor, blood
from donation.forms import registerform , loginform, Blood_bank, registerbankform, registerdoctorform, loginbankform, logindoctorform
from donation import db
from flask_login import login_user, logout_user,login_required, current_user


index = str()




@app.route('/')
def home_page():
	return render_template('home.html')

@app.route('/register')
def register_page():
	
	return render_template('register.html') 


@app.route('/register/user', methods=['GET','POST'])
def register_user_page():
	form = registerform()
	form.district.choices = [(district.id,district.district) for district in district.query.all()]
	if form.validate_on_submit():

		user_to_create= user(username=form.username.data, email_address=form.email_address.data, blood_grp=form.blood_grp.data, mobile_no=form.mobile_no.data, district=form.district.data , password=form.password1.data)
		db.session.add(user_to_create)
		db.session.commit()
		login_user(user_to_create)
		flash(f'Account created sucessfully! You are now logged in as: {user_to_create.username}')
		return redirect(url_for('home_page'))
	if form.errors !={}:
		for err_msg in form.errors.values():
			flash(f'There was an error in creating the user:{err_msg}',category='danger')
		

	return render_template('register_user.html',form=form)

@app.route('/register/doctor', methods=['GET','POST'])
def register_doctor_page():
	form = registerdoctorform()
	if form.validate_on_submit():
		user_to_create = doctor(username=form.username.data, email_address=form.email_address.data, mobile_no=form.mobile_no.data, password=form.password1.data)
		db.session.add(user_to_create)
		db.session.commit()
		login_user(user_to_create)
		flash(f'Account created sucessfully! You are now logged in as: {user_to_create.username}')
		return redirect(url_for('home_page'))
	if form.errors != {}:
		for err_msg in form.errors.values():
			flash(f'There was an error in creating the user:{err_msg}',category='danger')

	return render_template('register_doctor.html', form=form)



@app.route('/register/bank', methods=['GET','POST'])
def register_bank_page():

	form = registerbankform()
	form.district.choices = [(district.id,district.district) for district in district.query.all()]
	if form.validate_on_submit():
		x = form.name.data
		user_to_create = userbank(district_id=form.district.data, name_id=form.name.data, password=form.password1.data )
		db.session.add(user_to_create)
		db.session.commit()
		#login_user(user_to_create)
		#flash(f'Account created sucessfully! You are now logged in as: {user_to_create.name_id}')
		return redirect(url_for('home_page'))
	if form.errors !={}:
		for err_msg in form.errors.values():
			flash(f'There was an error in creating the user:{err_msg}',category='danger')
		


	return render_template('register_bank.html', form= form)

@app.route('/register/blood_bank/<get_district>')
def bank(get_district):
	bb =blood_bank.query.filter_by(district_id=get_district).all()
	districtArray = []
	for bloodbank in bb :
		districtobj = {}
		districtobj['id'] = bloodbank.id
		districtobj['name'] = bloodbank.name
		districtArray.append(districtobj)

	return jsonify({'bb' : districtArray})



@app.route('/login')
def login_page():
	
	return render_template('login.html') 



@app.route('/login/user', methods=['GET','POST'])
def user_login_page():
	form = loginform()
	if form.validate_on_submit():
		attempted_user = user.query.filter_by(email_address=form.email_address.data).first()
		if attempted_user and attempted_user.check_password_correction(attempted_password=form.password.data):
			login_user(attempted_user)
			flash(f'Sucess! You are logged in as: {attempted_user.username}',category = 'success')
			return redirect(url_for('home_page'))
		else:
			flash('Username or Password is incorrect! Please try again', category= 'danger')


	return render_template('login_user.html',form=form)

@app.route('/login/doctor', methods=['GET','POST'])
def doctor_login_page():
	form = logindoctorform()
	if form.validate_on_submit():
		attempted_user = doctor.query.filter_by(email_address=form.email_address.data).first()
		if attempted_user and attempted_user.check_password_correction(attempted_password=form.password.data):
			login_user(attempted_user)
			flash(f'Sucess! You are logged in as: {attempted_user.username}',category = 'success')
			return redirect(url_for('home_page'))
		else:
			flash('Username or Password is incorrect! Please try again', category= 'danger')


	return render_template('login_doctor.html',form=form)

@app.route('/login/bank', methods=['GET','POST'])
def bank_login_page():
	form = loginbankform()
	form.district.choices = [(district.id,district.district) for district in district.query.all()]

	if form.validate_on_submit():
		

		attempted_user = userbank.query.filter_by(name_id=form.name.data).first()

		if attempted_user and attempted_user.check_password_correction(attempted_password=form.password.data):
			login_user(attempted_user)
			flash(f'Sucess! You are logged in as: {attempted_user.name_id}',category = 'success')
			
			global index
			
			index = attempted_user.name_id


			
			# return index

			return redirect(url_for('official_blood_bank'))
			
		else:
			flash('Username or Password is incorrect! Please try again', category= 'danger')


	return render_template('login_bank.html',form=form)

@app.route('/login/blood_bank/<get_district>')
def logbank(get_district):
	bb =blood_bank.query.filter_by(district_id=get_district).all()
	districtArray = []
	for bloodbank in bb :
		districtobj = {}
		districtobj['id'] = bloodbank.id
		districtobj['name'] = bloodbank.name
		districtArray.append(districtobj)

	return jsonify({'bb' : districtArray})



@app.route('/logout')
def logout_page():
	logout_user()
	flash('You have been logged out!',category='info')
	return redirect(url_for('home_page'))


@app.route('/blood_bank_page', methods=['GET','POST'])
def blood_bank_page():
	form = Blood_bank()
	form.district.choices = [(district.id,district.district) for district in district.query.all()]
	#print(form.district.data) 
	if form.validate_on_submit():



		return redirect(url_for('official_blood_bank'))
	if form.errors !={}:
		for err_msg in form.errors.values():
			flash(f'There was an error in creating the user:{err_msg}',category='danger')
		
	#form.name.choices = [(blood_bank.id,blood_bank.name) for blood_bank in blood_bank.query.all()]

	return render_template('blood_bank.html', form=form)
	

@app.route('/blood_bank/<get_district>')
def bloodbank(get_district):
	bb =blood_bank.query.filter_by(district_id=get_district).all()
	districtArray = []
	for bloodbank in bb :
		districtobj = {}
		districtobj['id'] = bloodbank.id
		districtobj['name'] = bloodbank.name
		districtArray.append(districtobj)

	return jsonify({'bb' : districtArray})


@app.route('/blood_bank/blood_bank', methods=['GET'])
def official_blood_bank():
	
	x = index
	x = int(x)
	database = blood_bank.query.filter_by(id= x).first()
	y = database
	b = blood.query.filter_by(id=x).first()
	q = b.A_positive 

	return render_template('official_blood_bank.html', y=y, x=x,b=b, q=q)