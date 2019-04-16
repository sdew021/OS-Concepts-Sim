from django.urls import path
from django.conf.urls import include,url
from . import views
app_name='page'
urlpatterns=[

    path('',views.demo,name='demo'),
path('page2/',views.demo2,name='demo2'),
    path('page2/algo/', views.algo2, name='algo2'),
    path('algo/',views.algo),
    #ADDED HERE
    path('wiki/', views.demo3,name='demo3'),
]