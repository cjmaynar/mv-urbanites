from django.contrib import admin
from django import forms

from page.models import Page, Component

class ComponentForm(forms.ModelForm):
    class Meta():
        model = Component

    CHOICES = (
        ('text', 'Text'),
        ('image', 'Image')
    )

    POSITIONS = (
        ('left', "Left"),
        ('right', "Right"),
        ('center', "Center"),
    )

    text = forms.CharField(required=False, widget=forms.Textarea(attrs={'cols': 80, 'rows': 10, 'class': 'text'}), help_text="Use <a href='http://daringfireball.net/projects/markdown/syntax'>Markdown</a> formatting here")
    image = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={'class': 'image'}))
    title = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'image'}), help_text="The hover text for the image")
    link = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'image'}), help_text="Turn the picture into a clickable URL")
    alternate_text = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'image'}), help_text="A textual description of this picture", label="Alt Text")
    side = forms.ChoiceField(required=False, widget=forms.Select(attrs={'class': 'image'}), choices=POSITIONS, help_text="The position of where this image will show")
    span = forms.ChoiceField(required=False, widget=forms.Select(attrs={'class': 'image'}), choices=[(s,s) for s in range(1,8)], help_text="Controls how large the image is")

    ctype = forms.ChoiceField(label="Component Type", widget=forms.RadioSelect(), choices=CHOICES)

class ComponentInline(admin.StackedInline):
    model = Component
    form = ComponentForm
    extra = 0

class PageForm(forms.ModelForm):
    parent = forms.ModelChoiceField(queryset=Page.objects.filter(parent=None), required=False)

class PageAdmin(admin.ModelAdmin):
    model = Page
    form = PageForm
    inlines = [ComponentInline,]

    class Media:
        js = (
            '/static/js/jquery-1.9.1.min.js',
            '/static/js/jquery-ui-1.10.2.custom.min.js',
            '/static/page/admin.js',
        )

admin.site.register(Page, PageAdmin)
