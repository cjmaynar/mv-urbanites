import requests
import datetime
import pprint

from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.views.generic.base import View

from blog.models import Blog
from feature.models import Feature
from page.models import Page
from settings import MEETUP_KEY

class Home(View):
    def get(self, request, *args, **kwargs):
        api = 'https://api.meetup.com/2/events?'
        key = 'key=%s' % (MEETUP_KEY)
        query = '&sign=true&group_urlname=20s-30sMountVernonUrbanites'
        page = Page.objects.get(id=1)

        tmp_event = []
        events = requests.get('%s%s%s' % (api, key, query)).json()
        for event in events['results']:
            d = datetime.datetime.fromtimestamp(event['time'] / 1e3)
            event['date'] = "%d/%d/%d" % (d.month, d.day, d.year)
            tmp_event.append(event)
        events = tmp_event

        try:
            blog = Blog.objects.latest()
        except ObjectDoesNotExist:
            blog = {}
        
        try:
            feature = Feature.objects.order_by('?')[0]
        except IndexError:
            feature = {}

        return render(request, 'home.html', vars())
