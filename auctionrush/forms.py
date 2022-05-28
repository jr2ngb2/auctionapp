from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class UserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')
    #error_messages={'invalidUCI':'Kindly enter a UCI email address to sign up' , 'password_mismatch':'Kindly enter email and password in correct format'}
    phone = forms.CharField(label='Phone')
    error_messages={'invalidUCI':'Kindly enter a UCI email address to sign up'}
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.phone = self.cleaned_data["phone"]
        if commit:
            user.save()
        return user
    def clean_email(self):
        email = self.cleaned_data['email']
        if email[-8:] != "@uci.edu":
            raise ValidationError(self.error_messages['invalidUCI'])
        # if password1 != password2:
        #     raise ValidationError(self.error_messages['password_mismatch'])
        return email    