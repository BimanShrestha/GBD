# GBD
TASK-1:Parsing .json file into csv
TASK-2:Web Scrapping,Screenshots,Dumpfile
TASK-3:Getting data from API
TASK-4:Parsing multiple Data from Json file

Prepare Your Environment
When you’re ready to start your new Django web application, create a new folder and navigate into it. In this folder, you’ll set up a new virtual environment using your command line:

$ python3 -m venv env

This command sets up a new virtual environment named env in your current working directory. Once the process is complete, you also need to activate the virtual environment:

$ source env/bin/activate

Install Django and Pin Your Dependencies
Once you’ve created and activated your Python virtual environment, you can install Django into this dedicated development workspace:

(env) $ python -m pip install django
This command fetches the django package from the Python Package Index (PyPI) using pip. After the installation has completed, you can pin your dependencies to make sure that you’re keeping track of which Django version you installed:

(env) $ python -m pip freeze > requirements.txt

Suppose you’re working on an existing project with its dependencies already pinned in a requirements.txt file. In that case, you can install the right Django version as well as all the other necessary packages in a single command:

(env) $ python -m pip install -r requirements.txt



Step	Description	Command
1a	Set up a virtual environment	python -m venv env
1b	Activate the virtual environment	source env/bin/activate
2a	Install Django	python -m pip install django
2b	Pin your dependencies	python -m pip freeze > requirements.txt
3	Set up a Django project	django-admin startproject <projectname>
4	Start a Django app	python manage.py startapp <appname>

urls of the project
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('project/list_config',views.project),
    path('view_config/',views.view),
    path('project/edit_config',views.myview),
    path('update_config/',views.update),
    path('detail_view',views.detailview),
    path('csvupload',views.xpathedit),
    path('edit_view/<detail_id>',views.show_detail)

]
