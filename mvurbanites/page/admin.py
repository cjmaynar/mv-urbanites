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

    text = forms.CharField(required=False, widget=forms.Textarea(attrs={'cols': 80, 'rows': 10, 'class': 'text'}))
    image = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={'class': 'image'}))
    link = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'image'}))
    alternate_text = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'image'}))
    side = forms.ChoiceField(required=False, widget=forms.Select(attrs={'class': 'image'}), choices=POSITIONS)

    ctype = forms.ChoiceField(label="Component Type", widget=forms.RadioSelect(), choices=CHOICES)

class ComponentInline(admin.StackedInline):
    model = Component
    form = ComponentForm
    extra = 0

class PageAdmin(admin.ModelAdmin):
    inlines = [ComponentInline,]

    class Media:
        js = (
            '/static/js/jquery-1.9.1.min.js',
            '/static/js/jquery-ui-1.10.2.custom.min.js',
            '/static/js/admin.js',
        )

admin.site.register(Page, PageAdmin)
