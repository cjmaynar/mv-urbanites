from django.views.generic import View
from django.shortcuts import render

class AccountView(View):
    def get(self, request, *args, **kwargs):
        template_name = 'account/index.html'

        return render(request, template_name, vars())
