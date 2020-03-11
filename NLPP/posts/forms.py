from django import forms
from . import models
from tinymce.widgets import TinyMCE


class PostForm(forms.ModelForm):
    class Meta:
        fields = ("name", "description", "body_text", "from_lang", "to_lang", "due_date")
        model = models.Post
        content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    def __init__(self, *args, **kwargs):
        model = models.Post
