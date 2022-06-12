from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *

INTEGER_CHOICES= [tuple([x,x]) for x in range(1,10)]

class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class UploadForm(forms.ModelForm):
    class Meta:
        model = Projects
        exclude =['name','profile']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        design= forms.IntegerField(label="Design Rates")
        usability = forms.IntegerField(label="Usability Rates")
        content = forms.IntegerField(label="Content Rates")
        creativity = forms.IntegerField(label="Creativity Rates")
        location = forms.CharField(label="Location")
                
        widget=forms.Select(choices=INTEGER_CHOICES)
        exclude =['project','user']

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2']


        widgets = {
           'username' : forms.TextInput(attrs={'class': 'form-control','placeholder':'Username'}),
           'email' :forms.EmailInput(attrs={'class': 'form-control','placeholder':'Email Address'}),
           'password1' : forms.TextInput(attrs={'class': 'form-control','placeholder':'password'}),
           'password2' :forms.TextInput(attrs={'class': 'form-control','placeholder':'Confirm Password'}),
    
        }
