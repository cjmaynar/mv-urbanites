from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, View
from django.shortcuts import render

from .models import Page

class PageLanding(View):
    def get(self, request, *args, **kwargs):
        template_name = 'page/%s.html' % (kwargs['slug'])
        children = Page.objects.filter(parent=Page.objects.get(slug=kwargs['slug']))

        return render(request, template_name, vars())


class PageDetail(DetailView):
    def get_queryset(self):
        list = get_object_or_404(Page, slug=self.kwargs['slug'])
        return Page.objects.all()

    def get_context_data(self, **kwargs):
        context = super(PageDetail, self).get_context_data(**kwargs)
        page = Page.objects.get(slug=self.kwargs['slug'])
        context['feature'] = page
        context['section'] = page.parent
        return context
