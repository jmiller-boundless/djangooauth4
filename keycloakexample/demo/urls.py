from django.conf.urls import url  
from . import views

urlpatterns = [  
    url(r'^$', views.home, name='index'),
    url(r'^unprotected$', views.unprotected, name='unprotected'),
    url(r'^secure$', views.home, name='secure'),
]
