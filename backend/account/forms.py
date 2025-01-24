from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *
# from django.utils.translation import ugettext_lazy as _

class CreateUserForm(UserCreationForm):
    # def __init__(self, *args, **kwargs): 
    #     super(ModelForm, self).__init__(*args, **kwargs)
    #     self.css_class = "rule"
    #     self.fields['is_staff'].label = 'Agree to Terms and Conditions '
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        widgets = {
            # 'is_staff' : forms.CheckboxInput(attrs={'checked':'True'}),
            # 'username' : forms.TextInput(attrs={'class': 'form-control'}),
            # 'email' : forms.EmailInput(attrs={'class': 'form-control'}),
            # 'password1' : forms.PasswordInput(attrs={'class': 'form-control', 'type':'password'}),
            # 'password2' : forms.PasswordInput(attrs={'class': 'form-control'}),
        }
    
class CreateCompanyForm(ModelForm):
    class Meta:
        model = CompanyProfile
        fields = ['company_name', 'phone', 'address']
        widgets = {
            'company_name' : forms.TextInput(attrs={'class': 'form-control', 'required':'True'}),
            'phone' : forms.TextInput(attrs={'class': 'form-control'}),
            'address' : forms.TextInput(attrs={'class': 'form-control'}),
            
        }

class StaffPermissionForm(ModelForm):
    class Meta:
        model = StaffPermission
        fields = ['hr', 'qc', 'admin', 'supervisor', 'warehouse', 'cutting', 'packing']

