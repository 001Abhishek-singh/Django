from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import MyModel

class MyForm(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = ["fullname","surname", "mobile_number"]#ye model ke field name hai
        labels = {'fullname': "Name","surname": "Surname", "mobile_number": "Mobile Number",}#ye label hoga template pe



class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', )