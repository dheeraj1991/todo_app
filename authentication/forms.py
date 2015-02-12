from django import forms
from django.forms.widgets import PasswordInput
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        widgets = {
            'password': PasswordInput(),
        }


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', widget=forms.TextInput)

    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username is None or password is None:
            raise forms.ValidationError("Both fields are required")
        user = authenticate(username=username, password=password)
        if not user:
            raise forms.ValidationError('Invalid user')
        if not user.is_active:
            raise forms.ValidationError('User not active')
        return user