## where users will be navigating to
# this import below says that is file is a blueprint of the application that means it has a bunch of roots and urls' inside it
# it allows us to define views in multiple files.
from flask import Blueprint


#Defining a blueprint
views = Blueprint('views',__name__)


#for the homepage
@views.route('/')
def home():
    return "<h1>Test</h1>"
