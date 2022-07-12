from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from .forms import UserLoginForm

urlpatterns = [
    path(
        'login/',
        LoginView.as_view(
            template_name="registration/login.html",
            authentication_form=UserLoginForm
        ),
        name='login'
    ),
    path('signup/', views.SignUpView.as_view(), name='signup'),
]
