# Codnity Homework

## Setup and requirements
To run the project you must have python version >= 3.9.x and npm version >= 8.1.x installed and have them added to environment variables (PATH - windows, env - MacOs/Linux), as well as have a MySQL server running.

- Setup
	- 
- Clone/Download all the files in git repository.
- Navigate to the project folder via terminal/CMD:
		
		cd path/to/project/codnity_project 

 - Import Database located in project folder (codnity_articles.sql) into your sql server.

 - Backend setup:
	 -
	- Navigate to the Backend folder in the project folder:
				
			cd Backend
	- Create virtual environment via command:
		Windows:

			py -m venv venv

		MacOs/Linux:
			
			python3 -m venv venv
	- Activate the virtual environment:
	Windows:
			
			venv/Scripts/activate

		MacOs/Linux
			
			. venv/bin/activate
	- Install all necessary dependencies
			
			pip install -r requirements.txt
			
	- Navigate to the src folder :

			cd src
	- To run flask service, simply type (py for windows, python3 for MacOs/Linux):
	
			py main.py
		After which the backend service will be active and accessible on localhost port 5000, it only has one endpoint "/get-articles", which returns dictionary containing id, title, link, points, date_created.

	- To run terminal app, type:
		
			py controller.py
		It accepts 3 commands, which are presented and explained once the app is running.

- Frontend setup
	-
	- Install react with:
		 
			npm i react
		
	- Navigate to the Frontend folder in the project folder, and type:
		
			npm i

			npm start

	- Now you will have the react app, containing all the scrapped data, start on your default browser, if not, it can be accessed at http://localhost:3000. If data is not being displayed, make sure you followed Backend setup instructions and flask app is running.


	
