from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

User = get_user_model()

class SupportForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ''
    text.label = ''

    def clean_text(self):
        data = self.cleaned_data['text']
        if len(data) < 25:
            raise ValidationError("Минимальное количество символов - 10.")

        if len(data) > 500:
            raise ValidationError("Максимальное количество символов - 500.")
        return data

class MyForm(forms.Form):
    id_task = forms.IntegerField(initial=1, min_value=1, max_value=30)


class UserCreationForm(UserCreationForm):
    email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={'autocomplete': 'email'})
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email")

