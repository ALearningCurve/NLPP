from django import forms
from . import models


class PostForm(forms.ModelForm):
    class Meta:
        fields = ("name", "description", "body_text", "due_date")
        model = models.Post

    def __init__(self, *args, **kwargs):
        pass

        # user = kwargs.pop("user", None)
        # super().__init__(*args, **kwargs)
        # if user is not None:
        #     self.fields["group"].queryset = (
        #         models.Group.objects.filter(
        #             pk__in=user.groups.values_list("group__pk")
        #         )
        #     )
