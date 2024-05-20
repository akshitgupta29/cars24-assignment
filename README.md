# Assignment - Akshit Gupta

This repository is created as part of the assignment shared. Below is the description for all the folders
- Screenshot: This folder contains the screenshots of the outputs as per the assignment. It has two screenshots, one from Postman while the docker container is running in the system and the other from the Swagger UI.
- dataset: Dataset folder contains the test images that I have used for testing the model and the API running in docker container.
- .gitignore: Git Ignore is a standard file that contains the details of the folders that needs to be ignored while making a commit in git repositories.
- Dockerfile: Dockerfile contains the commands used to build the docker image.
- 	app.py: app.py contains the fastapi application code with the code to load the model and the logic for the predict api.
-	deployment.yaml:  Deployment file for Kubernetes.
-	model.keras: Export of the trained model.
-	model_training.ipynb: File containing the exploratory data analysis and training code for the model.
-	models.py: File containing the model definition for the fastapi application.
-	requirements.txt: File containing the requirements used for building the application.
-	service.yaml: Yaml file containing the configuration for creating a service in Kubernetes. 
