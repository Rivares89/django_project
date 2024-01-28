from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from django.views.generic import TemplateView

from users.apps import UsersConfig
from users.views import RegisterView, ProfileView, generate_new_password, EmailVerify, MyLoginView

app_name = UsersConfig.name

urlpatterns = [
    # path('login/', MyLoginView.as_view(), name='my_login'),
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),

    path('invalid_verify/', TemplateView.as_view(template_name='users/invalid_verify.html'), name='invalid_verify'),
    path('valid_verify/', TemplateView.as_view(template_name='users/valid_verify.html'), name='valid_verify'),


    path(
        'verify_email/<uidb64>/<token>/',
        EmailVerify.as_view(),
        name='verify_email',
    ),
    path('confirm_email/',
         TemplateView.as_view(template_name='users/confirm_email.html'),
         name='confirm_email'
         ),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/genpassword', generate_new_password, name='generate_new_password'),
]
