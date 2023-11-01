# python-django-practice
Python Django Projects


# Django Setup Steps
1. Create Virtual Environment (virtualenv .venv - for mac, for windows - python -m venv .venv)
2. Activate Virtual Environment (source .venv/bin/activate | .venv/Scripts/activate)
3. Install Django (pip install django). (You can also install all the requirements file)
4. Start django project in the current directory (django-admin startproject project_name .)
5. Create new database in mysql (mypythondjangopractice)
6. Update settings file - DATABASES
`DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mypythondjangopractice',  # Name of your MySQL database
        'USER': 'username',  # MySQL username
        'PASSWORD': 'userpassword',  # MySQL password
        'HOST': 'hostname',  # MySQL server host (change to your MySQL server address) - localhost for local
        'PORT': '3306',  # MySQL server port (default is usually 3306)
        'ATOMIC_REQUESTS': True,
    }
}`
7. Run command - python manage.py migrate 
8. Run server - python manage.py runserver (http://127.0.0.1:8000/)

# Create first django app (common)
1. Create apps/common/__init__.py
2. create apps/common/apps.py 
Copy this code in apps.py
`from django.apps import AppConfig


class CommonConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.common"
`
3. Create apps/common/urls.py
Copy this code in urls.py - We will create a healthcheck api
`from django.urls import path

from apps.common import views

urlpatterns = [
    path("", views.HealthCheck.as_view(), name="health"),
]
`
4. Create a view for this in apps/common/views.py
We will be using djangorestframework for APIs (Install requirements.txt and add in `INSTALLED_APPS` - `'rest_framework'`)
Copy this code in views.py
`__author__ = "Deepak Verma"

from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

__all__ = ("HealthCheck",)

class HealthCheck(APIView):
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        try:
            return Response(
                {
                    "is_success": True,
                    "message": "Servers are running...",
                    "data": None,
                },
                status=status.HTTP_200_OK,
            )
        except Exception as ex:
            return Response(
                {"is_success": False, "message": None, "data": None},
                status=status.HTTP_200_OK,
            )
`
5. Modify project_name/urls.py to add the above route to `urlpatterns`.
`path('', include('apps.common.urls')),`
6. Add `apps.common` to `INSTALLED_APPS`
7. Run Server