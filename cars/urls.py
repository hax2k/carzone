from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns=[
    path('', views.cars, name='cars'),
]
urlpatterns += staticfiles_urlpatterns() #if static file won't load or univarsal staticloader