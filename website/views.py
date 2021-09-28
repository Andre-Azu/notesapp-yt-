## where users will be navigating to
# this import below says that is file is a blueprint of the application that means it has a bunch of roots and urls' inside it
# it allows us to define views in multiple files.
from flask import Blueprint,render_template,request,flash
from flask_login import login_required,current_user
from .models import Note
from . import db

#Defining a blueprint
views = Blueprint('views',__name__)


#for the homepage
@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note=request.form.get('note')

        if len(note) <=1:
            flash('Note too short', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash("Note added!", category="success")

    return render_template("home.html", user=current_user)
