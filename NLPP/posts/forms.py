from django import forms
from . import models


class PostForm(forms.ModelForm):
    class Meta:
        fields = ("name", "description", "body_text", "from_lang", "to_lang", "due_date")
        model = models.Post

    def __init__(self, *args, **kwargs):
        model = models.Post
