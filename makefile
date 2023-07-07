# A makefile to create a python virtual environment, used for
#opening a Practice Flask application
# Created by: YasmeenNoorDV
# Creation date: 2 March 2023

# Ensure you have the resources needed for the virtual environment
install_res:
	pip3 install virtualenv;
	python3 -m venv my_env

# Access the command to activate the virtual environment
env_act:
	@echo 'Please run the following command:';
	@echo 'source my_env/bin/activate'

# Install needed Python libraries
install_lib:
	pip3 install -r requirements.txt

# Run the Practice Flask application
run:
	flask --app practice run

# Remove binary files
clean:
	rm -r __pycache__

# Access the command to deactivate the virtual environment
env_deact:
	@echo 'Please run the following command:';
	@echo 'deactivate'
