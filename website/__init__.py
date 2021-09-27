from flask import Flask
#set up database
from flask_sqlalchemy import SQLAlchemy

#this path module determines whether the databse does or doesnt exist
from os import path

#define new database object(gonna be used whenever we wanna add a user or basically anything)
db=SQLAlchemy()
#pick the database name
DB_NAME="database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY']='ABCD'
    # telling flask that we will use this database and the file it will be located.
    app.config['SQLALCHEMY_DATABASE_URI']=f'sqlite:///{DB_NAME}'
    #initialize database
    db.init_app(app)

    # define the blueprints
    # from <name of file> import <name of blueprint>
    from .views import views
    from .auth import auth

    # register the blueprint 
    # the url_prefix means that youll have to add the section in the the url to access the route
        # for example if prefix is '/auth/' one has to type '/auth/hello 
    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/')


    #ensures the system checks for these two tables are present
    from .models import User,Note



    return app

# creating a database just in case one doesnt exist
def create_database(app):
    if not path.exists('website/'+ DB_NAME):
        db.create_all(app=app)
        print("Created Database!!")