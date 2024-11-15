from django import forms
from .models import UseContactEmail

class UseContactEmailForm(forms.ModelForm):
    class Meta:
        model = UseContactEmail
        fields = ['uid', 'emailaddresses']  # Fields you want to expose in the form
