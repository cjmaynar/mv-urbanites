from django import forms

class ContactForm(forms.Form):
    name = forms.CharField()
    your_email = forms.EmailField()
    message = forms.CharField(widget=forms.widgets.Textarea())
