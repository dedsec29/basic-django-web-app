from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    # Using regular expression to validate Indian phone numbers
    contact_number = forms.CharField(max_length=15, validators=[RegexValidator(
        '^(?:(?:\+|0{0,2})91(\s*[\ -]\s*)?|[0]?)?[789]\d{9}|(\d[ -]?){10}\d$', message="Enter a Valid Indian Phone Number")])
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]