from django.urls import path
from . import views

urlpatterns = [
    path('journals/', views.index),
    path('journals/summary', views.summary),
    path('journal/add', views.create),
    path('journal/edit/<int:id>', views.edit),
    path('journal/delete/<int:id>', views.delete),
    path('journal/<int:id>', views.find),
]
