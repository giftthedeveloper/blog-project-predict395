from django import forms


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), required=False)