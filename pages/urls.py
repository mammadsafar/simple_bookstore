from django.urls import path
from .views import HomeView#, AboutView, ContactView, LoginView, LogoutView, SignUpView
urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),

]