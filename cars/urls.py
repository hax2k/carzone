from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns=[
    path('', views.cars, name='cars'),
    path('<int:id>', views.car_detail, name='car_detail'),
    path('search', views.car_search, name='car_search'),
]
urlpatterns += staticfiles_urlpatterns() #if static file won't load or univarsal staticloader