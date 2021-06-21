from django import forms


class BlogForm(forms.Form):
    title = forms.CharField(label="This is My title: ", widget=forms.TextInput(attrs={"class": "form-control"}))
    content = forms.CharField(required=False, widget=forms.Textarea(attrs={"class": "form-control", "rows": 3}))
    image = forms.ImageField(required=False)
    
