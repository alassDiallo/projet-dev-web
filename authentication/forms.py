from django import forms

class Auth(forms.Form):
    email= forms.EmailField(max_length=30)
    password = forms.CharField(max_length=20)

