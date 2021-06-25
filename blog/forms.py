from django import forms

from .models import Blog

class BlogForm(forms.Form):
    title = forms.CharField(label="This is My title: ", widget=forms.TextInput(attrs={"class": "form-control"}))
    content = forms.CharField(required=False, widget=forms.Textarea(attrs={"class": "form-control", "rows": 3}))
    image = forms.ImageField(required=False)
    
class BlogModelForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content']