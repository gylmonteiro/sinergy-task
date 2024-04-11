from django import forms
from .models import VoluntaryUser

class VoluntaryUserForm(forms.ModelForm):
    
    class Meta:
        model = VoluntaryUser
        fields = ('username', 'password')
