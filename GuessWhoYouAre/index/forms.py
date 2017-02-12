from django import forms
from django.core.exceptions import ValidationError

from index.models import Networks


class ContactForm(forms.ModelForm):

    confirm_email = forms.UserField(
        label="Confirm user Name",
        required=True,
    )

    class Meta:
        model = Networks

    def __init__(self, *args, **kwargs):

        if kwargs.get('instance'):
            email = kwargs['instance'].email
            kwargs.setdefault('initial', {})['confirm_email'] = email

        return super(ContactForm, self).__init__(*args, **kwargs)