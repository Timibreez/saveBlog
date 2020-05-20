from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget = forms.TextInput(attrs = {'type':'text', 'placeholder':'Username'}) )
    password = forms.CharField(widget = forms.PasswordInput(attrs = {'type':'password', 'placeholder':'Password'}))

class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget = forms.EmailInput(attrs= {'type':'email', 'name':'email', 'placeholder':'Email'}))
    f_name = forms.CharField(max_length = 20, widget = forms.TextInput(attrs= {'type':'text',  'placeholder':'First Name'}) )
    l_name = forms.CharField(max_length = 20, widget = forms.TextInput(attrs= {'type':'text', 'placeholder':'Last Name'}) )
    username = forms.CharField(widget = forms.TextInput(attrs = {'type':'text', 'placeholder':'Username'}) )
    password1 = forms.CharField(widget = forms.PasswordInput(attrs = {'type':'password', 'placeholder':'Password'}))
    password2 = forms.CharField(widget = forms.PasswordInput(attrs = {'type':'password', 'placeholder':'Retype Password'}))
    class Meta:
        model = User
        fields = ('username','f_name','l_name','email','password1','password2')


    def save(self,commit = True):
        user = super(SignUpForm,self).save(commit=False)
        user.f_name = self.cleaned_data['f_name']
        user.l_name = self.cleaned_data['l_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
        return user