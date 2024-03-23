1ST DAY DJANGO WORKSHOP
======================

INSTALLATION FOR PYTHON 3.6.8
-----------------------------
python.org->downloads->windows->3.6.8
Install 3.6.8 version in python


SETTING PATH IN CMD
--------------------
cmd-->pip install django
   -->>python -m pip install --upgrade pip



PROJECT CREATION IN DJANGO
--------------------------
project creation in django:
    for project creation enter this command--->django-admin startproject FirstProject

we can see a file with your project name in your path


UPDATE YOUR FOLDER IN VS
------------------------
set your folder in vs code
we have various options under FirstProject 
click on init_.py-->empty python file
asgi.py-->asynchronous server gateway interface
wsgi.py-->web server gateway interface
settings.py-->we can see all project settings
urls.py-->we can create userdefined urls
manage.py-->it django serverfile, without this file we can't run server in django


APP CREATION IN DJANGO:
----------------------
	-manage.py
	-for app creation django provides command
		i.e python manage.py startapp FirstApp
	Then we can see another folder in FirstProject is FirstApp
		init.py-->it is an empty python file
		admin.py-->it contains administrative database related configurations
		app.py-->it contain django app information
		models.py-->it contains database files
		views.py-->it is a controller file, it controlles both templates,models..
		test.py-->it is used to test testcases in django 


DJANGO SERVER:
-------------
 command--->python manage.py runserver
		it will show the django version settings

url creation :
------------
	-->urls.py
	-->path(p1,p2,p3)
	-->path('urlname/',views.funtionname,name of url)

		
DYNAMIC URL'S:
-------------
	-path('urlname/<datatype:variable>',views.function)
	-views--> we have a send a parameter of a variable








2ND DAY WORKSHOP
================

DJANGO TEMPLATES:
----------------
	-template:
		-we can store.html files
		-render(p1,p2,p3)
			render(request,'html filename',dictionary)
		user-->django server-->urls.py-->views.py-->.html


CREATION OF TEMPELATES IN DJANGO:
--------------------------------
	-Django app folder-->FirstApp-->New folder-->templates
	i.e create one new folder in FirstApp with the name of templates
	IN VS CODE-->templates-->new file-->temp.html
	we can upload your new file in settings.py


DTL-->DJANGO TEMPLATE LANGUAGE:
------------------------------
	-conditional statements
		-{% if (condition)%}
			{{}}
		{% endif %}
		-loops
		{% for i in variable name%}
			{{i}}
		{% end for %}





CSS(Cascading Style Sheet)
--------------------------
	-To provide styles on html tags
	-syntax:
		property:value;


Types of css:
-------------
	-inline css
		-To provide css properties in single line/same line
	-internal css
		-To provide css properties in head tag
	-external css
		-we can create one seperate.css file in that we can apply css properties to 		 the html tag
		-static file handling is used for store the .css files,.js files and bootstrap links...

CREATION OF STATIC FILES:
------------------------
	-FirstApp-->new folder-->static
	In static we create 3 folders which are
	-static-->css
		-->js
		-->images



3RD DAY WORDKSHOP
=================
	-Http request methods
		-get-->default
		-post
	-Data Rendering from templates to views
		user-->server-->urls-->views-->.html
		.html-->views
			-.html-->Http Method="POST"
			-token-->csrf_token-->security
		views.py
			-->if request.method=="POST":


DJANGO ADMIN:
-------------
	-django administration GUI
		-http://127.0.0.1:8000/admin/login/?next=/admin/
	-Superuser account:
		python manage.py migrate          ###18 tables are created
		python manage.py createsuperuser
			-username:
			-email:
			-psw:
			-cpsw:






BOOTSTRAP:
----------
	https://getbootstrap.com/
	  -online Bootstrap
		-we can copy both css and js links from online
		-syntax:
			-property-value
		-By using 
	  -offline Bootstrap
	 	-we can store both css and js links in our pc



4TH DAY WORKSHOP
================
	-Task:
		-url name:register
		-registration form
			-username
			-email
			-mobile
			-radio button
				-m,fe
			-check box
				-telugu,english,hindi
			-dropdown
				-cse,ece,csi,ai,mech
			-joining data
			-update resume
			-psw
			-cpsw
				register


MODEL CREATION:
---------------

https://sqlitebrowser.org/dl/


	-model:
		we can store data base files
-in models.py file we can create data base in django
-data base name:student
	-name
	-roll num
	-age
	-mobile
	-email
	-address
      -By class we can create db
      -syntax:
		class classbane-->dbname
	-data fields:
		str-->charField
		int-->IntegerField
		email-->EmailField
		large text-->TextField
		image-->ImageField

	-after completion of model creation we have to perform 2 operations:
		-make migrations
			-It generate one interface file for our db
			-command:
				python manage.py makemigrations
		-migrate
			-it converts interface file into table
			-command:
				python manage.py migrate



ORM QUERIES:
	-insert,read,update,delete
	-python shell:
		python manage.py shell
		from FirstApp.models import student



How to insert data into db by using ORM:
---------------------------------------
	-save()
		-Query:
			data=modelname(name='xxxx',age='xx',mobile='xxxxx',email='xx@gmail.com',a	ddress='xxxx')
	Ex:data=student(id='5',name='sarma',rollnum='5000',age='52',mobile='9494183516',ema                       	il='sarma@gmail.com',address='kakinada')
	data.save()
	data
	-create():
		-query():
			-data=student.objects.create(id='6'.name='Family',rollnum='123',age='100',mobile='123456789',email='family@gmail.com',address='kkd')
data



How to retrive data from database:
----------------------------------
	-if you want to retrive all rows from database
		-all()
		-query:
			data=modelname.objects.all()
	-if you want to acess single column from db
		-for i in data:
			print(i.name)
	-if you want to access specific row details from db
		-get()
		-query:
			-modelname.objects.get(id=record no)
	-if you want to access duplicate data from database
		-filter
		-query:
			modelname.objects.filter(columnname='value')
	-Slicing:
		-modelname.objects.all()[:3]        //it will print all data up to 3
		-modelname.objects.all()[::-1]      //it will print all data in reverse order


How to update particular value in database:
-------------------------------------------
	-First fetch the data from db by using record number
		-get()
			g=modelname.objects.get(id=record no)
			g
	-we will update
		g.column name="New value/Updated value"
		g.save()
		g
   	-multiple values:
		g=student.objects.all().update(email='kousalya@gmail.com')
		g
How to delete record from db using ORM:
---------------------------------------
	-First fetch the data from db by using record number
		-get()
			g=modelname.objects.get(id=record no)
			g
	-we will delete
		-g.delete()
	-for all records we will delete
		g=student.objects.all()
		g
		g.delete()







5TH DAY WORKSHOP
================
	-CRUD operations using Html Pages
		-CrudProject-->project name
			-django-admin startproject CrudProject
		-CrudApp-->App name This command is applied after cd CrudProject
			-python manage.py startapp CrudApp
		-server
			-python manage.py runserver



DATA INSERTION IN CRUD OPERATIONS:
---------------------------------
	front-end
		url,view,template,bootstrap
		-html-->student db
		-registration form-->submit-->db
	Back-end:
		db--student
		-html-->student db
		-registration form-->submit-->db


	url:
	-insert
	-we have to import views
		i.e,from CrudApp import views

	views:
		-we have to import from django.http import HttpResponse this line
	templates:
		-CrudApp-->newfolder-->templates
		-templates-->new file-->insert.html
