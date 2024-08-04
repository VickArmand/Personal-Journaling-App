from django.urls import path
from . import views
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView, TokenBlacklistView)

urlpatterns = [
    path('register', views.register),
    path('login', TokenObtainPairView.as_view()),
    path('token/refresh', TokenRefreshView.as_view()), #refresh token required in request body
    path('edit', views.edit_user),
    path('logout', TokenBlacklistView.as_view()),
    path('logout_all', views.signout),

]
