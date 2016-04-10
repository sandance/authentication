__author__ = 'nazmul'

from django import forms


class LoginForm(forms.Form):
    """
    This Form will be used to authenticate users against the database
    """
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


from django.contrib.auth.models import User

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password',widget=forms.PasswordInput)

    password2 = forms.CharField(label='Repeat password',widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username','first_name','email')

    def clean_password2(self):
        cd = self.clean_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords dont match.')
        return cd['password2']




