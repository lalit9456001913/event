from django import forms
from event.models import Event,Registration
from django.contrib.auth.models import User
class User_form(forms.ModelForm):
    username=forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control',
                'placeholder':'Enter User Name'}
    ),required=True,max_length=20)
    email = forms.CharField(widget=forms.EmailInput(
        attrs={'class': 'form-control',
               'placeholder': 'Enter Mail Id'}
    ), required=True, max_length=20)
    first_name=forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control',
               'placeholder': 'Enter First Name'}
    ),required=True,max_length=20)
    last_name=forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control',
               'placeholder': 'Enter Lasr Name'}
    ),required=True,max_length=20)
    password = forms.CharField(widget=forms.PasswordInput(), required=True, max_length=20)
    confirm_password=forms.CharField(widget=forms.PasswordInput(),required=True,max_length=20)

    class Meta():
        model=User
        fields="__all__"


class EventForm(forms.ModelForm):
    class Meta():
        model=Event
        fields=('event_name','event_type','no_of_attendees',)

class RegistrationForm(forms.ModelForm):
    class Meta():
        model=Registration
        fields='__all__'

