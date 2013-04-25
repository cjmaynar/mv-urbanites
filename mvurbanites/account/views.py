from django.contrib import auth, messages
from django.shortcuts import render, redirect
from django.views.generic import View
from django.views.generic.edit import FormView

from .forms import LoginForm

class AccountView(View):
    template_name = 'account/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, vars())


class LogoutView(View):
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated():
            auth.logout(self.request)

        return redirect('/')


class LoginView(FormView):
    template_name = "account/login.html"
    form_class = LoginForm

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated():
            return redirect('/')

        return super(LoginView, self).get(*args, **kwargs)

    def form_valid(self, form):
        auth.login(self.request, form.user)
        expire = 60*60*24*365*10 if form.cleaned_data.get("remember") else 0
        self.request.session.set_expiry(expire)
        
        return redirect('/')

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, 'Invalid Form!')
        return super(LoginView, self).form_invalid(form)


class JoinView(View):
    template_name = "account/join.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, vars())
