:: STEPS TAKEN ::

Application Tested With --  (powershell - windows10)

Note: Enable Script exicution in powershell  (Set-ExecutionPolicy RemoteSigned)

A)  Steps Taken while creating APPLICATION
-----------------------------------------------------------------------------------------------
1. Create new folder dolist
2. go to dolist path
3. Create Virtual environment   --->   python -m venv myvenv         
4. Activate virtual environment --->   .\myvenv\Scripts\activate     
5. Download Django              --->   pip install django
6. Create Django project        --->   django-admin startproject myproj
7. notepad.py myproj/setting.py
      -- STATIC_URL = '/static/'
      -- STATIC_ROOT = os.path.join(BASE_DIR, 'static')
8. Create Django Application    --->   python manage.py startapp myapp
9. notepad.py myproj/setting.py
      -- add myapp in INSTALLED_APPS = [...]
10. python manage.py migrate
-----------------------------------------------------------------------------------------------



B)  Run APPLICATION
-----------------------------------------------------------------------------------------------
1. Download Github project 
2. Create ToDoList Folder and Download gitproject here
3. Create Virtual environment   --->   python -m venv myvenv         
4. Activate virtual environment --->   .\myvenv\Scripts\activate     
5. Download Django              --->   pip install django
6. Go to myproj folder          --->   cd myproj
6. Run Django Application       --->   python manage.py runserver 0.0.0.0:9000
-----------------------------------------------------------------------------------------------



C) USE CASE
-----------------------------------------------------------------------------------------------
url : http://127.0.0.1:9000/task/
   
1. ADD NEW TASK
   steps :  
            a) click Add Me Buttton 
            b) type new task name 
            c) click submit

2. Update Task 
   url :
            a) Click on task name 
            b) Edit 
                    ---  name of task
                    ---  completion status of task
3) Delete Task
   url  :
            a) Click delete button to delete task          
-----------------------------------------------------------------------------------------------
