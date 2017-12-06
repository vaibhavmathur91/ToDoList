"""myproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
]

"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from myapp.views import TaskCreate, TaskUpdate, TaskDelete, TaskList
app_name = 'myapp'

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^task/$', TaskList.as_view(), name='index'),
    url(r'task/add/$', TaskCreate.as_view(), name='task-add'),
    url(r'task/update/(?P<pk>[0-9]+)/$', TaskUpdate.as_view(), name='task-update'),
    url(r'task/delete/(?P<pk>[0-9]+)/$', TaskDelete.as_view(), name='task-delete'),
]