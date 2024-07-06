from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register),
    path('login', views.signin),
    path('edit', views.edit_user),
    path('logout', views.signout),
]
