# Basic Student CRUD App in Django

This is a basic Student management crud application made using Django, Bootstrap and Datatables js library.

To use this project, follow the steps below:

## Step 1: Creating Python Virtual Environment

Verify if python is installed to create the virtual environment for the project.

```
python --version
```

Create and activate the virtual environment.

```
python -m venv .venv
source .\venv\Scripts\activate
```

## Step 2: Install dependencies

Install the dependencies mentioned in the requirements.txt file using the following pip command

```
pip install -r requirements.txt
```

## Step 3: Create superuser

Run the migration command for add
Go to 'student_management' directory using the 'cd' command and verify if it contains the 'manage.py' file using 'ls'. <br/>
If it exists, create a superuser for the admin panel.

```
cd student_management
ls
```

First run the migrate command to create the necessary tables for the admin panel

```
python manage.py migrate
```

Next is to create the admin user:

```
python manage.py createsuperuser
```

Add your username, email (this can be empty), and password to the createsuperuser command. <br/>
Now you can acces the admin panel by going to localhost:8000/admin in your browser. Enter your username and password to log in.

## Step 4: Make Migrations for the models
We have a student directory inside the project which is a django app and it contains the file 'models.py' where we have the Student model.
<br/>
To migrate the Student model into the database, we will run the following commands:

```
python manage.py makemigrations student
python manage.py migrate
```
This command will create a Student table in the database and you can access it from the admin panel.

## Step 5: Run the server
Now to see our project in action, we will use the runserver command to run a django  server in which we can access our app from the URL provided in the output
```
python manage.py runserver
```
It will output the localhost url in which the project is running. Access the url in the browser and check if everything is working fine.

