from django.urls import  path
from .views import *

urlpatterns = [
    path('register/', Register.as_view(), name="register"),
    path("otp/", OTPView.as_view(), name="otp-view"),
    path("login/", LoginView.as_view(), name='login')
]