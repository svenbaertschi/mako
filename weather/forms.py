
from django import forms
 
class PostForm(forms.Form):
    location = forms.CharField(max_length=256)