from django.forms import ModelForm, TextInput, Textarea, EmailInput, PasswordInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


 


class SignUpForm(UserCreationForm):
    password1 = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={'class': 'input','placeholder': 'Password'}))
    password2 = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'Password confirm'}))

    class Meta:
        model = User
        fields = ['username','first_name','last_name', 'email', 'password1', 'password2']
        widgets = {
            'username':    TextInput(attrs={'class': 'input', 'placeholder': 'Username'}),
            'first_name':  TextInput(attrs={'class': 'input', 'placeholder': 'First name'}),
            'last_name':   TextInput(attrs={'class': 'input', 'placeholder': 'Last name'}),
            'email':       EmailInput(attrs={'class': 'input', 'placeholder': 'Your email'}),           
        }


""" 
class SignUpForm1(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        widgets = {
            'username':    TextInput(attrs={'class': 'input', 'placeholder': 'Username'}),
            'first_name':  TextInput(attrs={'class': 'input', 'placeholder': 'First name'}),
            'last_name':   TextInput(attrs={'class': 'input', 'placeholder': 'Last name '}),
            'email':       EmailInput(attrs={'class': 'input', 'placeholder': 'Your email'}),
            'password1':   PasswordInput(attrs={'class': 'input', 'placeholder': 'Password'}),
            'password2':   PasswordInput(attrs={'class': 'input', 'placeholder': 'Password confirmation'}),
        }   """


        