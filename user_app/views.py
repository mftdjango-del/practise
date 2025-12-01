import hashlib
from django.contrib.auth import login, logout
from django.contrib.auth.hashers import make_password
from django.http import HttpRequest, Http404
from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string
from django.views import View
from .forms import RegisterForm, LoginForm
from django.db.models import  Q
from .models import User
from django.utils import timezone
from django.core.cache import cache
from django.contrib import messages
from utils.get_ip import get_user_ip
from utils.emails import send_otp_email
from utils.utils import create_random_code
# Create your views here.




class Register(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, "register-page.html", {
            'register_form': register_form
        })

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            email = register_form.cleaned_data.get("email")
            phone = register_form.cleaned_data.get("phone")
            password = register_form.cleaned_data.get("password")
            re_password = register_form.cleaned_data.get("re_password")
            if password != re_password:
                register_form.add_error("re_password", "رمز عبور و تکرار آن مطابقت ندارد")
                return render(request, "register-page.html", {
                    'register_form': register_form
                })

            user = User.objects.filter(Q(email=email) | Q(phone=phone)).first()
            if user is not None:
                register_form.add_error("email", "شما قبلا ثبت نام کردید")
                return render(request, "register-page.html", {
                    'register_form': register_form
                })
            otp_code = get_random_string(length=6, allowed_chars="0123456789")
            ip = get_user_ip(request)
            cache_data = {
                "phone": phone,
                "email": email,
                'password': make_password(password),
                "otp": hashlib.sha1(otp_code.encode()).digest(),
                "ip": ip.replace(".", "_"),
                "timestamp": timezone.now().timestamp()
            }
            send_otp_email("OTP verify", to=email, context={"phone": phone, "otp": otp_code}, template_name="emails/otp-template.html")
            cache_key = f"otp_{ip.replace(".", "_")}"
            cache.set(cache_key, cache_data, timeout=180)
            print(otp_code)
            return redirect("otp-view")

        else:
            return render(request, "register-page.html", {
                'register_form': register_form
            })


class OTPView(View):
    history = []
    def exist_user(self, request):
        ip = get_user_ip(request)
        cache_key = f"otp_{ip.replace(".", "_")}"
        cache_ = cache.get(cache_key)
        if cache_:
            return True, cache_
        else:
            return False, None
    def get(self, request):
        exist, data = self.exist_user(request)
        if exist:
            return render(request, "otp-page.html", {
                'email': data.get("email")
            })
        else:
            raise Http404

    def post(self, request):
        exist, data = self.exist_user(request)
        if exist:
            input1 = request.POST.get("inp1")
            input2 = request.POST.get("inp2")
            input3 = request.POST.get("inp3")
            input4 = request.POST.get("inp4")
            input5 = request.POST.get("inp5")
            input6 = request.POST.get("inp6")
            otp_code = f"{input1}{input2}{input3}{input4}{input5}{input6}"
            if hashlib.sha1(otp_code.encode()).digest() == data.get("otp"):
                user = User(email=data.get("email"), phone=data.get("phone"), username=data.get("phone"), password=data.get("password"), is_active=True)
                user.save()
                messages.success(request, "ثبت نام با موفقیت انجام شد")
                return redirect("home")
            else:
                return render(request, "otp-page.html", {
                    'error': True
                })
        else:
            raise Http404


class LoginView(View):
    def get(self, request):
        login_form = LoginForm()
        return render(request, 'login-page.html', {
            'login_form': login_form
        })
    def post(self , request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            email = login_form.cleaned_data.get("email")
            password = login_form.cleaned_data.get("password")
            user:User = User.objects.filter(email=email).first()
            if user is not None:
                if user.check_password(password):
                    login(request, user)
                    messages.success(request, "ورود با موفقیت انجام شد")
                    return redirect('home')
                else:
                    return render(request, 'login-page.html', {
                        'login_form': login_form
                    })
            else:
                return render(request, 'login-page.html', {
                    'login_form': login_form
                })


def logout_view(request):
    logout(request)
    return redirect("home")