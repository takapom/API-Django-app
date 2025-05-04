from django import forms
from django.contrib.auth.models import User

# sqliteのauth_userに格納される！
class UserForm(forms.ModelForm):

    class Meta():
        model = User
        fields = ('username', 'email', 'password')
        widgets = {
            'password': forms.PasswordInput
        }