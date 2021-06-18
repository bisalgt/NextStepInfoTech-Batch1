from django import forms


class BlogForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    content = forms.CharField(required=False, widget=forms.Textarea(attrs={"class": "form-control", "rows": 3, "randomAttribue": "Muyna me is bishal"}))
    
