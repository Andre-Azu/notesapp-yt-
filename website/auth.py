from flask import Blueprint,render_template,request,flash,redirect,url_for
# redirect and url_for are used to redirect users

from .models import User
from werkzeug.security import check_password_hash,generate_password_hash
from . import db


auth = Blueprint('auth',__name__) 

@auth.route('/login',methods=['GET', 'POST'])
def login():
    #to login users
    if request.method == 'POST':
        email=request.form.get('email')
        password=request.form.get('password')

        user=User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash("logged in succesfully", category='success')
                return redirect(url_for('views.home'))
            else:
                flash("incorrect password, try again", category='error')
        else:
            flash("account does not exist.", category='error')
    return render_template("login.html", text="Welcome back ", boolean=True)

@auth.route('/logout')
def logout():
    return render_template("home.html")

@auth.route('/sign-up', methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name=request.form.get('firstName')
        password1=request.form.get('password1')
        password2=request.form.get('password2')

        # To prevent a user to sign up with the same email,
        user=User.query.filter_by(email=email).first()
        if user:
            flash("email already exists", category='error')
        # add validations/flash messages 

        elif len("email")<2:
            flash("email must be greater than two characters",category='Success')
        elif len('first_name')<3:
            flash("firstname too short",category='error')
        elif len('password')<4:
            flash('password too short',category='error')
        elif password1 != password2:
            flash("passwords dont match", category="error")
        else:
            new_user=User(email=email,password=generate_password_hash(password1, method='sha256'),first_name=first_name)
            db.session.add(new_user)
            db.session.commit()
            #add user to database
            flash('account created',category='success')
            #to redirect the user to the homepage of the website, 
            return redirect(url_for('views.home'))


    return render_template("sign_up.html" ,text="Hello new user :)") 