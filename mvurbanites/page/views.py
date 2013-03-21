from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView

from page.models import Page

class PageDetail(DetailView):
    def get_queryset(self):
        list = get_object_or_404(Page, slug=self.kwargs['slug'])
        return Page.objects.all()

    def get_context_data(self, **kwargs):
        context = super(PageDetail, self).get_context_data(**kwargs)
        context['feature'] = Page.objects.get(slug=self.kwargs['slug'])
        return context
