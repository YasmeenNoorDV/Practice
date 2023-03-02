# A basic Flask application for the Meque project
# Created by: YasmeenNoorDV
# Date: 2 March 2023

#Imports
from flask import Flask, render_template
#import flask_login

#Initialize app
app = Flask(__name__)
#app.secret_key = 'science rift under'

#User session setup
#login_manager = flask_login.LoginManager()
#login_manager.init_app(app)

#Home page
@app.route("/")
def home():
	return render_template('home.html')

#Basic python app run
if __name__ == '__main__':
	app.run()
