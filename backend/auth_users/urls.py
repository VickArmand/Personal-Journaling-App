from django.urls import path
from . import views
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView, TokenBlacklistView, TokenVerifyView)

urlpatterns = [
    path('register', views.register),
    path('login', TokenObtainPairView.as_view()),
    path('token/refresh', TokenRefreshView.as_view()), #refresh token required in request body
    path('token/verify', TokenVerifyView.as_view()),
    path('edit', views.edit_user),
    path('logout', TokenBlacklistView.as_view()), #refresh token required in request body
    path('logout_all', views.signout),

]
