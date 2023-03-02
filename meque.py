# A basic Flask application for the Meque project
# Created by: YasmeenNoorDV
# Date: 2 March 2023

#Imports
from flask import Flask, render_template, request
#import flask_login
import git

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

#Monitor a webhook to allow PythonAnywhere to automatically deploy new commits
@app.route('/webhook', methods=['POST'])
def webhook():
	if request.method == 'POST':
		repo = git.Repo.('./meque')
		meque = repo.remotes.meque
		repo.create_head('main',  meque.refs.main).set_tracking_branch(meque.refs.main).checkout()
		meque.pull()
		return '', 200
	else:
		return '', 400

#Basic python app run
if __name__ == '__main__':
	app.run()
