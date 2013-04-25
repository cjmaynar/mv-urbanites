from django import forms

class ContactForm(forms.Form):
    EMAILS = (
        ('tina@mvurbanites.com', 'Tina Dudley - Founder'),
        ('john@mvurbanites.com', 'John Kernan - Finance'),
        ('dan@mvurbanites.com', 'Dan Rohn - Counsel'),
    )
    to = forms.ChoiceField(choices=EMAILS)
    your_name = forms.CharField()
    your_email = forms.EmailField()
    message = forms.CharField(widget=forms.widgets.Textarea())
