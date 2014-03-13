from django.http import request
from accounts_manager.models import MainUser, ActorProfile, ProductionProfile
from django import forms

__author__ = 'holl'



class UserForm(forms.ModelForm):
    class Meta(object):
        model = MainUser
        fields = ["username","email","password"]
        widgets = {
            "password": forms.PasswordInput
        }


class SignupForm(UserForm):
    confirm_password = forms.CharField(
        widget=forms.PasswordInput
    )

    def clean(self):
        password = self.cleaned_data.get("password")
        password_conf = self.cleaned_data.get("confirm_password")
        if password is not None and password != password_conf:
            raise forms.ValidationError(
                "Password confirmation does not match password"
            )

        return self.cleaned_data


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(
        widget=forms.PasswordInput
    )


class ProfileForm(forms.ModelForm):
    class Meta(object):
        model = ActorProfile

        fields = ["first_name", "last_name",
                  "bio", "headshot", "highlight_reel",
                  "phone", "gender", "tag", "age",]

class ProductionProfileForm(forms.ModelForm):

    class Meta(object):

        model = ProductionProfile

        fields = ["name", "bio",
                  "bio", "company_pic",]
