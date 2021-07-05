from django import forms
import django

from .models import Blog, NewUser

class BlogForm(forms.Form):
    title = forms.CharField(label="This is My title: ", widget=forms.TextInput(attrs={"class": "form-control"}))
    content = forms.CharField(required=False, widget=forms.Textarea(attrs={"class": "form-control", "rows": 3}))
    image = forms.ImageField(required=False)
    
class BlogModelForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content']

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms.models import ModelForm

from django.conf import settings

class CreateUserForm(UserCreationForm):
    username = forms.CharField(label="", widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Username"}))
    first_name = forms.CharField(initial="Unknown", help_text="Enter the first name correctly", label="Enter the First name: ", widget=forms.TextInput(attrs={"class": "form-control"}))
    password1 = forms.CharField(label="Password : ", widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(label="Password Again: ", widget=forms.PasswordInput(attrs={"class": "form-control"}))
    
    class Meta(UserCreationForm):
        model = NewUser
        fields = ['username', 'first_name', 'last_name', 'email', 'contact', 'image', 'user_type',]



class UpdateForm(ModelForm):
    class Meta:
        model = NewUser
        fields = ['first_name', 'last_name', 'email', 'contact', 'image', 'user_type']