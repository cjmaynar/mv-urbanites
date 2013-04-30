from django import forms

class ContactForm(forms.Form):
    EMAILS = (
        ('tina@mvurbanites.com', 'Tina Dudley - Founder'),
        ('john@mvurbanites.com', 'John Kernan - Finance'),
        ('dan@mvurbanites.com', 'Dan Rohn - Counsel'),
    )
    to = forms.ChoiceField(choices=EMAILS, help_text="Pick someone to email")
    your_email = forms.EmailField(help_text="Please provide a valid email address")
    message = forms.CharField(widget=forms.widgets.Textarea())
