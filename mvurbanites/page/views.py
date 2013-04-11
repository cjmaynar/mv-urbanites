from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, View
from django.shortcuts import render

from .models import Page

class PageView(View):
    def get(self, request, *args, **kwargs):
        page = Page.objects.get(slug=self.kwargs['slug'])
        template_name = 'page/%s' % page.template

        return render(request, template_name, vars())
