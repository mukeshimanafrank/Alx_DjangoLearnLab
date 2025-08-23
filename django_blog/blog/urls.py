from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Built-in auth views
    path("login/",  auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="registration/logged_out.html"), name="logout"),

    # Custom views
    path("register/", views.register, name="register"),
    path("profile/",  views.profile,  name="profile"),

    # Optional home (can point to a simple template)
    path("", views.home, name="home"),
]
