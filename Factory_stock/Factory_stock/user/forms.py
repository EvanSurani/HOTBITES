from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm





class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    address = forms.CharField(max_length=50)
    number = forms.CharField(help_text='Contact phone number')

    class Meta:
        model = User
        fields = [
            'username',
            'number',
            'email',
            'address',
            'password1',           
            'password2',
        ]

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    address = forms.CharField(max_length=50)
    number = forms.CharField(help_text='Contact phone number')

    class Meta:
        model = User
        fields = [
            'username',
            'number',
            'email',
            'address',
         ]
         
    # def save(self, commit = True):
    #     user = super(RegistrationForm,self).save(commit=False)
    #     user.first_name = cleaned_data ['first_name']
    #     user.last_name = cleaned_data ['last_name']
    #     user.email = cleaned_data ['email']

        # if commit:
        #     user.save()

        # return user 

