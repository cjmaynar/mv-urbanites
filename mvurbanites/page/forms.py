from django import forms

class ContactForm(forms.Form):
    EMAILS = (
        ('john@mvurbanites.com', 'John Kernan - Organizer'),
        ('dan@mvurbanites.com', 'Dan Rohn - Counsel'),
    )
    to = forms.ChoiceField(
        choices=EMAILS,
        help_text="Pick an officer to email",
    )
    your_email = forms.EmailField(
        help_text="Please provide a valid email address",
        label="Your Email",
    )
    message = forms.CharField(
        widget=forms.widgets.Textarea()
    )
