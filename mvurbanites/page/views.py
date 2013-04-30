from random import choice

from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.views.generic import View

from .models import Page, Component
from .forms import ContactForm

class SearchView(View):
    template_name = 'page/other/search.html'

    def get(self, request,  *args, **kwargs):
        qstring = self.request.GET.get('q', '').strip()

        if qstring:
            searched = True
            results  = Component.objects.filter(
                Q(text__icontains=qstring)
            )
        else:
            searched = False

        return render(self.request, self.template_name, vars())


class SectionView(View):
    def get(self, request, *args, **kwargs):
        section = get_object_or_404(Page, slug=self.kwargs['slug'], published=True)
        try:
            page = section.children.reverse()[0]
        except IndexError:
            raise Http404

        return redirect('page', section=section.slug, slug=page.slug)



class PageView(View):
    SPONSORS = (
        ('cazbar.png', 'Cazbar' 'http://cazbar.pro/cazbar/cazbar.html'),
        ('centerstage.png', 'Center Stage', 'http://centerstage.org/'),
        ('homeslyce.png', 'Home Slyce', 'http://www.slycethebar.com/'),
        ('minato.png', 'Minato', 'http://www.minatosushibar.com/'),
        ('plates.png', 'Plates', 'http://www.platesbaltimore.com/'),
        ('redmaple.png', 'Red Maple', 'http://www.930redmaple.com/'),
    )


    def get(self, request, *args, **kwargs):
        sponsor = choice(self.SPONSORS)

        if 'slug' not in self.kwargs:
            page = get_object_or_404(Page, id=1, published=True)
        else:
            page = get_object_or_404(Page, slug=self.kwargs['slug'], published=True)

        template_name = 'page/%s' % page.template

        if page.template == 'contact_us.html':
            form = ContactForm()
        elif page.template == 'home.html':
            from settings import MEETUP_KEY
            import requests, datetime
            from blog.models import Blog
            from feature.models import Feature

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

        return render(self.request, template_name, vars())

    def post(self, request,  *args, **kwargs):
        sponsor = choice(self.SPONSORS)

        page = Page.objects.get(slug=self.kwargs['slug'])
        template_name = 'page/%s' % page.template

        if page.template == 'contact_us.html':
            form = ContactForm(request.POST)
            if form.is_valid():
                from django.core.mail import send_mail

                #TODO: Uncomment this
                #send_mail("Contact from mvurbanites.com", request.POST.get('message'), request.POST.get('your_email'), [request.POST.get('to')])

                messages.add_message(self.request, messages.SUCCESS, 'Email Sent!')
            else:
                messages.add_message(self.request, messages.ERROR, 'Invalid Form!')

        return render(self.request, template_name, vars())

