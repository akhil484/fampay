from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('callapi/', views.getResponse, name='getResponse'),
    path('showvideos/', views.VideoList.as_view()),
]