# 8916-Midterm

## Introduction

The following code is for a simple REST API that supports basic CRUD operations 
(Create, Read, Update, Delete) for a Student entity

## Festures

- Get: Retrieve a list of all students.
- Post: Adds a new student
- Put: Update an existing student
- Delete: Delete a student

## Prerequisites

- Pip
- Python
- Flask

## Project Structure

- app.py: Main Flask application 
- requirements.txt: List of Python dependencies 
- test-api.http: Test the REST API using the REST Client extension in Visual Studio Code
- README.md: Documentation

## Running the application

1. Install packages 

``` bash
pip install Flask Flask-SQLAlchemy Flask-RESTful

```

2. Install dependencies

``` bash
pip install -r requirements.txt

```

3. Running the application

``` bash
python3 app.py

```

## Deploying to Azure 

The rest API will be deployed on Azure web service 

1. Log in to Azure portal
2. Create a new resource group
3. Create a new app service web application and select the runtime app python 3.x

### Deployment
1. In the left menu, select "Deployment Center."
2. Under "Source," choose "GitHub" and authorize Azure to access your GitHub account.
3. Select your repository and branch (e.g., main) to deploy.
4. Click "Finish" to set up the deployment.

## Access your API
Once the deployment is successful, you can access your Flask API using the URL provided by Azure:

``` link

https://<your-app-name>.azurewebsites.net

```
