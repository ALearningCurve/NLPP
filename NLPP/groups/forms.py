from django import forms
from .models import Group, GroupMember


class GroupForm(forms.ModelForm):

    class Meta:
        model = Group
        fields = ('name', 'description',)

        widgets = {
            'name': forms.TextInput(attrs={'class': 'textinputclass'}),
            'description': forms.Textarea(attrs={'class': 'textinputclass'}),
        }


class GroupFindForm(forms.Form):
    slug = forms.CharField(label="Group Code:",max_length=50)
