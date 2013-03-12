from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView

from blog.models import Blog

class BlogList(ListView):
    model = Blog

class BlogDetail(DetailView):
    def get_queryset(self):
        list = get_object_or_404(Blog, slug=self.kwargs['slug'])
        return Blog.objects.all()

    def get_context_data(self, **kwargs):
        context = super(BlogDetail, self).get_context_data(**kwargs)
        context['feature'] = Blog.objects.get(slug=self.kwargs['slug'])
        return context
