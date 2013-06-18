from django import forms
from django.contrib.auth.models import User
from django.contrib.localflavor.us.forms import USPhoneNumberField
from django.contrib.auth import authenticate

from models import Userprofile

from utils.tools import USPhoneNumberMultiWidget

class Userform(forms.ModelForm):

        
    class Meta:
        model = Userprofile
        exclude = ('user',)
        
    def __init__(self, *args, **kwargs):
        super(Userform, self).__init__(*args, **kwargs)
        self.fields.keyOrder = [
            'username',
            'firstname',
            'lastname',
            'email',
            'telephone',
            'password']
        
    username = forms.CharField(min_length=5)
    firstname = forms.CharField()
    lastname = forms.CharField()
    telephone = USPhoneNumberField(label="Phone", widget=USPhoneNumberMultiWidget())
    email = forms.EmailField()
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)
    
    def clean_username(self):
        cd = self.cleaned_data
        users = User.objects.filter(username__iexact=cd['username'])
        if users.count() > 0:
            raise forms.ValidationError("username is not unique")
        return cd['username']
    
    
    def save(self):
        cd = self.cleaned_data
        print cd['username']
        user = User.objects.create_user(cd['username'], password=cd['password'], email=cd['email'])
        user.save()
        user = authenticate(username=cd['username'], password=cd['password'])
        userprofile = Userprofile(
                                  user=user,
                                  telephone=cd['telephone'],
                                  )
        userprofile.save()
        return userprofile
        