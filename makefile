# A makefile to create a python virtual environment, used for
#opening a Meque Flask application
# Created by: YasmeenNoorDV
# Date: 2 March 2023

#Ensure you have the resources needed for the virtual environment
install_res:
	pip3 install virtualenv;
	python3 -m venv my_env

#Access the command to activate the virtual environment
env_act:
	echo 'source my_env/bin/activate'

#Install needed Python libraries
install_lib:
	pip3 install -r requirements.txt

#Access the command to deactivate the virtual environment
env_deact:
	echo 'deactivate'

#Run the Meque Flask application
run:
	flask --app meque run
