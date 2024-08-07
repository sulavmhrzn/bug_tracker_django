from django.urls import path

from . import views

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("login/", views.LoginView.as_view(), name="login"),
]
