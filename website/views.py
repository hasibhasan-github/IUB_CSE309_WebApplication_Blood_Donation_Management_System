from flask import Blueprint, render_template, request, flash
from flask_login import  login_required, current_user

from .models import Fighter, Hero, BloodRequestDonate
from . import db

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("index.html")

@views.route('/homeg')
def homeg():
    return render_template("index.html")


# Profile Templates Route Fighter

@views.route('/Fdashboard')
@login_required
def Fdashboard():
    return render_template("BloodFighterDashboard.html", user = current_user)


@views.route('/Fprofile', methods = ['GET', 'POST'])
@login_required
def Fprofile():
    fighterUser = Fighter.query.filter_by(email = current_user.email).first()
    return render_template("FighterProfile.html", user = current_user, fight = fighterUser)

@views.route('/Donor', methods = ['GET', 'POST'])
@login_required
def Donor():
    fighterUser = Fighter.query.filter_by(email = current_user.email).first()
    heroUser = Hero.query.filter_by(bloodgroup = current_user.bloodgroup).all()
    userid = request.form.get("userid")
    heroalert = Hero.query.filter_by(email = userid).first()
    if heroalert is None:
        pass
    else:
        newReq = BloodRequestDonate(
            requester_email = current_user.email,
            requester_name = current_user.username,
            donor_email = heroalert.email,
            donor_name = heroalert.username,
            blood_group = current_user.bloodgroup,
            city = current_user.city,
            hospital = fighterUser.hospital
        )
        db.session.add(newReq)
        db.session.commit()
    useremail = request.form.get("useremail")
    if useremail is None:
        pass
    else:
        pass
    return render_template("AvailableDonor.html", user = current_user, blood = heroUser)


@views.route('/ActiveReq')
@login_required
def ActiveReq():
    bReqD = BloodRequestDonate.query.filter_by(requester_email = current_user.email).all()
    return render_template("ActiveRequest.html", user = current_user, stat = bReqD)



@views.route('/Ratings')
@login_required
def Ratings():
    return render_template("Ratings.html", user = current_user)


# Profile Templates Route Hero

@views.route('/Hdashboard')
@login_required
def Hdashboard():
    return render_template("HeroDashboard.html", user = current_user)


@views.route('/Hprofile')
@login_required
def Hprofile():
    return render_template("HeroProfile.html", user = current_user)

@views.route('/Hnotify')
@login_required
def Hnotify():
    bReqD = BloodRequestDonate.query.filter_by(donor_email = current_user.email).all()
    return render_template("HeroNotification.html", user = current_user, data = bReqD)