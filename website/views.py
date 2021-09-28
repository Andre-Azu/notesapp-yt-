## where users will be navigating to
# this import below says that is file is a blueprint of the application that means it has a bunch of roots and urls' inside it
# it allows us to define views in multiple files.
from flask import Blueprint,render_template
from flask_login import login_required,current_user


#Defining a blueprint
views = Blueprint('views',__name__)


#for the homepage
@views.route('/')
@login_required
def home():
    return render_template("home.html", user=current_user)
