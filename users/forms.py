from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(
        required=True,
        label='Username',
        widget=forms.TextInput()
        )
        
    password = forms.CharField(
        required=True,
        label='Password',
        widget=forms.PasswordInput()
        )