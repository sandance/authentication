__author__ = 'nazmul'

from django import forms


class LoginForm(forms.Form):
    """
    This Form will be used to authenticate users against the database
    """
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)



