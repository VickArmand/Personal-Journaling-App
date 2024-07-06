from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.index),
    path('category/add', views.create),
    path('category/edit/<int:id>', views.edit),
    path('category/delete/<int:id>', views.delete),
    path('category/<int:id>', views.find),
]
