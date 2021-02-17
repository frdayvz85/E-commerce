from django.forms import ModelForm, TextInput, Textarea, EmailInput, PasswordInput
from django.contrib.auth.models import User
from django import forms

from .models import UserProfile
 




class UserProfileForm(ModelForm):

    class Meta:
        model = UserProfile
        fields = ['phone','address','city', 'country', 'image']
        widgets = {
            'country':    TextInput(attrs={'class': 'input', 'placeholder': 'Country'}),          
        }