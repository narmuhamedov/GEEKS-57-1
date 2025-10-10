from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm


GENDER = (
        ('m', 'm'),
        ('f', 'f')
    )

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.IntegerField(required=True)
    gender = forms.ChoiceField(choices=GENDER, required=True)

    class Meta:
        model = models.CustomUser
        fields = (
            'username',
            'email',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'gender'
        )
    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
