from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
import re


# from django.contrib.auth.models import User
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ["username", "email", "address", "password1", "password2"]
        widgets = {
            "username": forms.TextInput(
                attrs={
                    "class": "form-input",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "form-input",
                }
            ),
            "address": forms.TextInput(
                attrs={
                    "class": "form-input",
                    "placeholder": "Enter your address",
                }
            ),
            "password1": forms.PasswordInput(
                attrs={
                    "class": "form-input",
                }
            ),
            "password2": forms.PasswordInput(
                attrs={
                    "class": "form-input",
                }
            ),
        }


class LoginForm(forms.Form):
    username = forms.CharField(
        label="Username:",
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        ),
    )
    password = forms.CharField(
        label="Password:",
        # min_length=8,
        widget=forms.PasswordInput(
            attrs={
                "class": "toggle",
            }
        ),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({"placeholder": "enter username"})
        self.fields["password"].widget.attrs.update({"placeholder": "enter password"})

    def clean_username(self):
        username = self.cleaned_data["username"]
        regex_pattern = r"^[A-Za-z_][A-Za-z0-9_]{2,}$"
        if not re.match(regex_pattern, username):
            raise forms.ValidationError("Invalid username !!!")
        return username
