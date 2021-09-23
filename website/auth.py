from flask import Blueprint,render_template,request,flash


auth = Blueprint('auth',__name__) 

@auth.route('/login',methods=['GET', 'POST'])
def login():
    return render_template("login.html", text="Welcome back ", boolean=True)

@auth.route('/logout')
def logout():
    return render_template("home.html")

@auth.route('/sign-up', methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName=request.form.get('firstName')
        password1=request.form.get('password1')
        password2=request.form.get('password2')

        # add validations/flash messages 

        if len("email")<2:
            flash("email must be greater than two characters",category='Success')
        elif len('firstName')<3:
            flash("firstname too short",category='error')
        elif len('password')<4:
            flash('password too short',category='error')
        elif password1 != password2:
            flash("passwords dont match", category="error")
        else:
            #add user to database
            flash('account created',category='success')

    return render_template("sign_up.html" ,text="Hello new user :)") 