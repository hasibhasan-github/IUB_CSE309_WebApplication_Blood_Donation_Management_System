from flask import Blueprint, render_template, request, flash, redirect, url_for
from . import db
from flask_login import login_user, login_required, logout_user, current_user

from .models import User, Fighter, Hero

auth = Blueprint('auth', __name__)

@auth.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get form data (username and password)
        email = request.form.get('email')
        password = request.form.get('password')

        # Check if the user exists in the database
        user = User.query.filter_by(email=email).first()

        if user:
            if user.password == password :
                if user.userRole == "fighter":
                    flash("Login successful!", category="success")
                    login_user(user, remember=True)
                    return redirect(url_for('views.Fdashboard'))
                else:
                    flash("Login successful!", category="success")
                    login_user(user, remember=True)
                    return redirect(url_for('views.Hdashboard'))
            else:
                flash("Invalid email or password. Please try again.", category="error")
        else:
            flash("Email doesn't exist. Please try again.", category="error")

    return render_template("login.html")


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('views.home'))

@auth.route('/signup',  methods = ['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('name')
        email = request.form.get('email')
        city = request.form.get('city')
        userRole = request.form.get('role')
        phone = request.form.get('phone')
        bloodgroup = request.form.get('bloodGroup')
        reqBloodGroup = request.form.get('reqBloodGroup')
        lastdonationdate = request.form.get('lastDonation')
        hospital =  request.form.get('hospital')
        weight = request.form.get('weight')
        password = request.form.get('password')
        confirmPassword = request.form.get('confirm')

        user = User.query.filter_by(email=email).first()

        if user:
            flash("Email already exist. Please try another.", category="error")
        elif len(email) < 4:
            flash('Email must be greater than 4 characters', category='error')
        elif len(username) < 2:
            flash('Username must be greater than 2 characters', category='error')
        elif password != confirmPassword:
            flash("Password doesn't match", category='error')
        elif len(password) < 7:
            flash('Password must be greater than 8 characters', category='error')
        elif len(confirmPassword) < 7:
            flash('ConfirmPassword must be greater than 8 characters', category='error')
        elif len(phone) <= 10:
            flash('contactNumber must be greater than 10 characters', category='error')
        else:
            # Add User to Database

            if userRole == "fighter":
                new_user = User(
                email=email,        
                password=password,          
                username=username,              
                weight=weight, 
                phone=phone,         
                userRole=userRole,                
                city = city,
                bloodgroup = reqBloodGroup,
                lastdonationdate = "00-00-00")               
                db.session.add(new_user)
                db.session.commit()
                new_user1 = Fighter(
                email=email,        
                password=password,          
                username=username,              
                weight=weight, 
                phone=phone,         
                userRole=userRole,                
                city = city,
                bloodgroup = reqBloodGroup,
                hospital = hospital)               
                db.session.add(new_user1)
                db.session.commit()
                flash('Registration Successful', category='success')
                # login_user(user, remember=True)
                return redirect(url_for('views.home'))
                pass
            else:
                new_user = User(
                    email=email,        
                    password=password,          
                    username=username,              
                    weight=weight, 
                    phone=phone,         
                    userRole=userRole,                
                    city = city,
                    bloodgroup = bloodgroup,
                    lastdonationdate = lastdonationdate)
                db.session.add(new_user)
                db.session.commit()
                hero = Hero(
                    email=email,        
                    password=password,          
                    username=username,              
                    weight=weight, 
                    phone=phone,         
                    userRole=userRole,                
                    city = city,
                    bloodgroup = bloodgroup,
                    lastdonationdate = lastdonationdate)
                db.session.add(hero)
                db.session.commit()
                flash('Registration Successful', category='success')
                    # login_user(user, remember=True)
                return redirect(url_for('views.home'))

    return render_template("signup.html")