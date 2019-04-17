
from django.contrib import admin
#from django.urls import path
from django.conf.urls import include,url
from . import views

app_name='ossim'
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/',include('home.urls')),
    url(r'^',include('booting.urls')),
    url(r'^sockets/',include('sockets.urls')),
    url(r'^synchro/',include('synchro.urls')),
    url(r'^file_allocation/',include('file_alloc.urls')),
    url(r'^deadlock/',include('deadlock.urls')),
    url(r'^page/',include('page.urls')),
    url(r'^matdemo/', include('mat.urls')),
    url(r'^team/', views.matindex),
    url(r'^wiki/', views.wiki),
    url(r'^pr/', views.pr),
    url(r'^ds/', views.ds),
    url(r'^ba/', views.ba),
    url(r'^fa/', views.fa),
    url(r'^mvt/', views.mvt),
    url(r'^mft/', views.mft),
    url(r'^ps/', views.ps),
    url(r'^soc/', views.soc),
    url(r'^sync/', views.sync),
    url(r'^disk/',include('disk_sched.urls'),name='disk'),
    url(r'^process/',include('process.urls'))
]
