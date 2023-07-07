# A basic Flask application for the Practice project
# Created by: YasmeenNoorDV
# Creation date: 2 March 2023

# Imports
from flask import Flask, render_template

# Initialize app
app = Flask(__name__)

# Home page
@app.route("/")
def home():
	return render_template('home.html')

# About me page
@app.route("/about")
def about():
	return render_template('about.html')

# Contact me page
@app.route("/contact")
def contact():
	return render_template('contact.html')


# Basic python app run
if __name__ == '__main__':
	app.run()
