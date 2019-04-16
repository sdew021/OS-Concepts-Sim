from django.conf.urls import url,include
from django.contrib import admin
#from django.urls import path

from . import views

app_name = 'home'
urlpatterns =[

    url(r'^$',views.main ),
    url(r'^desktop/',views.Desktop ,name='desktop'),

    url(r'^desktop/Task.html/', views.Task,name='task'),
    url(r'^desktop/terminal/',views.Terminal,name = 'terminal')


]
