from django.urls import path
from . import views

urlpatterns = [
    path('journals/', views.index),
    path('journal/create', views.create),
    path('journal/edit/:id', views.edit),
    path('journal/delete/:id', views.delete),
    path('journal/:id', views.find),
]
