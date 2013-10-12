from django.forms import ModelForm, CharField, RegexField, PasswordInput
from django.contrib.auth import *

class UserForm(ModelForm):
    password = CharField(widget=PasswordInput, label="Password")
    password2 = CharField(widget=PasswordInput, label="Password (again)")
                            
    phone = RegexField(regex=r'^((\(\d{3}\) ?)|(\d{3}-))?\d{3}-\d{4}$', max_length=14, label="Phone number")


    class Meta:
        model = get_user_model()
        fields = ['email', 'first_name','last_name','phone','password',
                  'password2']
        exclude = ['is_staff', 'is_active','date_joined','is_superuser',
        'groups','last_login', 'user_permissions']
    
   
        
    def clean(self):
        """
        Verifiy that the values entered into the two password fields
        match. Note that an error here will end up in
        ``non_field_errors()`` because it doesn't apply to a single
        field.
        
        """
        self.cleaned_data=super(UserForm, self).clean()
        
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError("The two password fields didn't match.")
        return self.cleaned_data
   
    def save(self, commit=True):
        # Save the provided password in a hased format.
        # Without this the pass word is save as plaintext and login fails.
        user = super(UserForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
