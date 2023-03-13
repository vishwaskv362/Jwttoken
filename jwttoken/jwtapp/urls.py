from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.welcome, name="api-overview"),
    path('createuser/', views.create_user, name='create_user'),
    path('users/', views.userList, name='create_user'),
]
