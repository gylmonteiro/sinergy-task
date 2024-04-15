from django import forms
from .models import VoluntaryUser

class VoluntaryUserForm(forms.ModelForm):
    
    class Meta:
        model = VoluntaryUser
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'})
        }
