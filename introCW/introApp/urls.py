from django.urls import path

from . import views
# sets path to call functions
urlpatterns = [
    path('', views.index, name='index'),
    path('gogetthegoods/', views.gogetthegoods),
    path('happyhappyjoyjoy/', views.happyhappyjoyjoy, name='index'),
]