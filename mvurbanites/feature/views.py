from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView

from feature.models import Feature

class FeatureList(ListView):
    model = Feature

class FeatureDetail(DetailView):
    def get_queryset(self):
        list = get_object_or_404(Feature, slug=self.kwargs['slug'])
        return Feature.objects.all()

    def get_context_data(self, **kwargs):
        context = super(FeatureDetail, self).get_context_data(**kwargs)
        context['feature'] = Feature.objects.get(slug=self.kwargs['slug'])
        return context
