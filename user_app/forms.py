from django import forms
from .models import User

class RegisterForm(forms.Form):
    email = forms.EmailField(max_length=50, min_length=5, widget=forms.EmailInput(attrs={
        'placeholder': "آدرس ایمیل",
        'class': "modern-input"
    }))
    phone = forms.CharField(max_length=15, min_length=10, widget=forms.NumberInput(attrs={
        'placeholder': "تلفن",
        'class': "modern-input phone-arrow",
        'dir': "rtl"
    }))
    password = forms.CharField(max_length=50, min_length=7, widget=forms.PasswordInput(attrs={
        'placeholder': "رمز عبور",
        'class':"modern-input",
        'id': 'eye-input'
    }))
    re_password = forms.CharField(max_length=50, min_length=7, widget=forms.PasswordInput(attrs={
        'placeholder': "تکرار رمز عبور",
        'class': "modern-input"
    }))


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=50, min_length=5, widget=forms.EmailInput(attrs={
        'placeholder': "آدرس ایمیل",
        'class': "modern-input"
    }))
    password = forms.CharField(max_length=50, min_length=7, widget=forms.PasswordInput(attrs={
        'placeholder': "رمز عبور",
        'class':"modern-input",
        'id': 'eye-input'
    }))
