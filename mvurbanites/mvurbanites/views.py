import requests

from django.shortcuts import render
from django.views.generic.base import View
from django.core.exceptions import ObjectDoesNotExist

from settings import MEETUP_KEY
from feature.models import Feature
from blog.models import Blog


class Home(View):
    def get(self, request, *args, **kwargs):
        api = 'https://api.meetup.com/2/events?'
        key = 'key=%s' % (MEETUP_KEY)
        query = '&sign=true&group_urlname=20s-30sMountVernonUrbanites'
        events = requests.get('%s%s%s' % (api, key, query))

        try:
            blog = Blog.objects.latest()
        except ObjectDoesNotExist:
            blog = {}
        
        try:
            feature = Feature.objects.order_by('?')[0]
        except IndexError:
            feature = {}

        return render(request, 'home.html', {'events': events.json(), 'feature': feature, 'blog': blog})
