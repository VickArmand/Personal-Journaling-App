from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.index),
    path('category/add', views.create),
    path('category/edit/:id', views.edit),
    path('category/delete/:id', views.delete),
    path('category/:id', views.find),
]
