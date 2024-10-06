from django import forms
from . import models

class CreateForm(forms.ModelForm):
    class Mets:
        model = models.Post
        fields = ['title','body','slug','banner']
        