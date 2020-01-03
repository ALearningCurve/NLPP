from django.contrib.auth import get_user_model, forms

class UserCreateForm(forms.UserCreationForm):
    class Meta:
        fields = ("username", 'first_name', 'last_name', "email", "password1", "password2")
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Display name and Log in Username"
        self.fields["email"].label = "Email address"
