from django import forms
from django.core import validators

class UserRegistrationForm(forms.Form):
    gender=[('male','Male'),('female','Female')]
    firstName=forms.CharField()
    lastName=forms.CharField(required=False)
    email=forms.CharField()
    gen=forms.CharField(widget=forms.Select(choices=gender))
    age=forms.IntegerField()
    password=forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        a=super().clean()
        b=a['firstName']
        if len(b)>20:
            raise forms.ValidationError('The max length of firstname is 20 char')

'''   def clean_email(self):
        inputEmail=self.cleaned_data['email']
        if inputEmail.find('@')==-1:
            return forms.ValidationError('The email should contain @ symbol')
        return inputEmail
'''

