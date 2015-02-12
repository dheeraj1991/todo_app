from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import View
from .forms import SignUpForm, LoginForm
from django.contrib.auth import login, logout


def redirect(view_func):
    def _wrapped_view_func(request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseRedirect('/task/home/')
        else:
            return view_func(request, *args, **kwargs)
    return _wrapped_view_func


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/user/login/')


class SignUp(View):

    @method_decorator(redirect)
    def get(self, request):
        signup_form = SignUpForm()
        return render(request, 'authentication/signup.html', {'signup': signup_form})

    @method_decorator(redirect)
    def post(self, request):
        signup_form = SignUpForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            login_form = LoginForm()
            return render(request, 'authentication/login.html', {'login': login_form})
        else:
            signup_form = SignUpForm(request.POST)
            return render(request, 'authentication/signup.html', {'signup': signup_form})


class Login(View):

    @method_decorator(redirect)
    def get(self, request):
        login_form = LoginForm()
        return render(request, 'authentication/login.html', {'login': login_form})

    @method_decorator(redirect)
    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user = login_form.cleaned_data
            login(request, user)
            return HttpResponseRedirect('/task/home/')
        else:
            login_form = LoginForm(request.POST)
            return render(request, 'authentication/login.html', {'login': login_form})
