from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView

from feature.models import Restraunt

class FeatureList(ListView):
    model = Restraunt

class FeatureDetail(DetailView):
    def get_queryset(self):
        list = get_object_or_404(Restraunt, id__iexact=self.kwargs['pk'])
        return Restraunt.objects.all()

    def get_context_data(self, **kwargs):
        context = super(FeatureDetail, self).get_context_data(**kwargs)
        context['feature'] = Restraunt.objects.get(id=self.kwargs['pk'])
        return context
