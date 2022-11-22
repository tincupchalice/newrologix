from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ("username", "email", 'company',
'address1',
'address2',
'city',
'state',
'zip',
'phone',
'doctor',
'doctor_phone',
'doctor_email',
'contact1',
'contact1_phone',
'contact1_email',
'contact2',
'contact2_phone',
'contact2_email',)

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("username", "email", 'company',
'address1',
'address2',
'city',
'state',
'zip',
'phone',
'doctor',
'doctor_phone',
'doctor_email',
'contact1',
'contact1_phone',
'contact1_email',
'contact2',
'contact2_phone',
'contact2_email',)