from django import forms
from . import models

class CreateSavePost(forms.ModelForm):
    rank = forms.CharField(max_length= 50, widget = forms.TextInput(attrs= {'type':'text', 'placeholder':'Rank'}) )
    f_name = forms.CharField(max_length = 20, widget = forms.TextInput(attrs= {'type':'text', 'placeholder':'First Name'}) )
    l_name = forms.CharField(max_length = 20, widget = forms.TextInput(attrs= {'type':'text', 'placeholder':'Last Name'}) )
    address = forms.Field(widget = forms.TextInput(attrs= {'type':'text', 'placeholder':'Address Information'}))
    thumb = forms.ImageField(widget = forms.FileInput())


    class Meta:
        model = models.SavePost
        fields = ['rank','f_name','l_name', 'address','thumb']