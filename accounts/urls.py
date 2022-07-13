from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordResetView, PasswordResetConfirmView
from . import forms

urlpatterns = [
    path(
        'login/',
        LoginView.as_view(
            authentication_form=forms.UserLoginForm
        ),
        name='login'
    ),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path(
        "password_change/", PasswordChangeView.as_view(
            form_class=forms.UserChangePasswordForm
        ), name="password_change"
    ),
    path("password_reset/", PasswordResetView.as_view(
        form_class=forms.CustomPasswordResetForm
    ), name="password_reset"),

    path("reset/<uidb64>/<token>/", PasswordResetConfirmView.as_view(
        form_class=forms.CustomPasswordResetConfirmForm
    ), name="password_reset_confirm", ),

]
