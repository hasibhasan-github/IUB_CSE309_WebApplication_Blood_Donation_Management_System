from flask import Blueprint, render_template, request, flash
from flask_login import  login_required, current_user

# from .models import Verification, Property, LeaseAgreement
# from . import db

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("index.html")

@views.route('/homeg')
def homeg():
    return render_template("HeroBase.html")


# Profile Templates Route Landlord

@views.route('/Fdashboard')
@login_required
def Fdashboard():
    return render_template("BloodFighterDashboard.html", user = current_user)