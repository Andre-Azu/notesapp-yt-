from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY']='ABCD'

    # define the blueprints
    # from <name of file> import <name of blueprint>
    from .views import views
    from .auth import auth

    # register the blueprint 
    # the url_prefix means that youll have to add the section in the the url to access the route
        # for example if prefix is '/auth/' one has to type '/auth/hello 
    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/')



    return app
