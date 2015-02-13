from django import forms
from django.forms.widgets import PasswordInput, TextInput
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(forms.Form):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    re_password = forms.CharField(label='', widget=forms.PasswordInput(attrs=
                                                                       {'placeholder': 'Re-Password'}))

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        re_password = self.cleaned_data.get('re_password')
        print username, password, re_password
        if (not username) and (not password) and (not re_password):
            raise forms.ValidationError("All the fields are required")
        elif password != re_password:
            raise forms.ValidationError("Passwords Do not match")
        user_count = User.objects.filter(username=username).count()
        if user_count:
            raise forms.ValidationError('User already exist')
        user = User.objects.create_user(username=username, password=password)
        user.is_active = True
        user.save()
        user = authenticate(username=username, password=password)
        return user


class LoginForm(forms.Form):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Username'}))

    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username is None or password is None:
            raise forms.ValidationError("Both fields are required")
        user = authenticate(username=username, password=password)
        if not user:
            raise forms.ValidationError('Invalid user or password')
        if not user.is_active:
            raise forms.ValidationError('User not active')
        return user