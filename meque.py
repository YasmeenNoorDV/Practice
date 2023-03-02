# A basic Flask application for the Meque project
# Created by: YasmeenNoorDV
# Date: 2 March 2023

#Imports
from flask import Flask

#Initialize app
app=Flask(__name__)

#Home page
@app.route("/")
def home():
	return "<h1>Meque</h1>"
