from django import forms
from frontend.models import *
from django.core import validators
from django.db.migrations.state import get_related_models_tuples
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.forms import(PasswordResetForm, SetPasswordForm, UserChangeForm, UserCreationForm)


class SubscribeForm(forms.ModelForm):
    email = forms.EmailField(label='', widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Email'}))
    class Meta:
        model = SubscribeModel
        fields = ['email']

class ContactForm(forms.ModelForm):
    first_name = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Name'}))
    email = forms.EmailField(label='Email :',
                             widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'E-mail'}))
    subject = forms.CharField(label='Subject :', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Subject'}))
    
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Message',
        'id': 'message',
        'rows': '10',
        'cols':'30'
    }))
    
    class Meta():
     model = Contact
     fields = ['first_name', 'email', 'subject', 'message']

class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(label='Old Password', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Old Password'}))
    new_password1 = forms.CharField(label='New Password', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'New Password'}))
    new_password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Confirm Password'}))
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

class EditUserForm(forms.ModelForm):
    username = forms.CharField( widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder': 'Username' }))

    first_name = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': ' FirstName'}))

    last_name = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': ' lastName'}))
    
    email = forms.EmailField(required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Email'}))

    image = forms.FileField(required=False)
    

    class Meta():
        model = User
        fields = ['username',  'first_name', 'last_name', 'email', 'image']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['username']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.image = self.cleaned_data['image']
    
        if commit:
            user.save()
            return user
     