from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.views.generic import DetailView, View

from .models import Page
from .forms import ContactForm

class PageView(View):
    def get(self, request, *args, **kwargs):
        page = Page.objects.get(slug=self.kwargs['slug'])
        template_name = 'page/%s' % page.template

        if page.template == 'contact_us.html':
            form = ContactForm()

        return render(request, template_name, vars())

    def post(self, request, *args, **kwargs):
        page = Page.objects.get(slug=self.kwargs['slug'])
        template_name = 'page/%s' % page.template

        print request.POST

        if page.template == 'contact_us.html':
            form = ContactForm(request.POST)
            if form.is_valid():
                from django.core.mail import send_mail

                #TODO: Uncomment this
                #send_mail("Contact from mvurbanites.com", request.POST.get('message'), request.POST.get('your_email'), ['me@coreymaynard.com'])

                messages.add_message(request, messages.SUCCESS, 'Email Sent!')
            else:
                messages.add_message(request, messages.ERROR, 'Invalid Form!')

        return render(request, template_name, vars())

