from django import forms
from django.contrib import auth

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput(render_value=False))
    remember = forms.BooleanField(required=False, label="Remember Me")
    user = None

    def clean(self):
        if self._errors:
            return

        user = auth.authenticate(**self.user_credentials())
        if user:
            self.user = user
        else:
            raise forms.ValidationError("Incorrect login")

        return self.cleaned_data

    def user_credentials(self):
        return {
            "username": self.cleaned_data["username"],
            "password": self.cleaned_data["password"],
        }
