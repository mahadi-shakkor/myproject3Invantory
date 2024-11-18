from django import forms
from .models import User, UseContactEmail, UseContactNumber

class  UserSignupForm(forms.Form):
    fname = forms.CharField(label="First Name", max_length=255, required=True)
    mname = forms.CharField(label="Middle Name", max_length=255, required=False)
    lname = forms.CharField(label="Last Name", max_length=255, required=True)
    utype = forms.ChoiceField(label="User Type", choices=[('aggriculturalofficer', 'Aggriculturalofficer'),
                                                          ('farmer', 'Farmer'),
                                                          ('wirehouse manaher', 'Wirehouse Manaher'),
                                                          ('distributor company', 'Distributor Company'),
                                                           ('neutritionist', 'Neutritionist')])
    password = forms.CharField(label="Password", widget=forms.PasswordInput, required=True)
    email_addresses = forms.EmailField(label="Email Address", required=True)
    contact_number = forms.CharField(label="Contact Number", max_length=255, required=True)




class UserLoginForm(forms.Form):
    uid = forms.CharField(label="User ID", required=True)
    password = forms.CharField(label="Password", widget=forms.PasswordInput, required=True)
