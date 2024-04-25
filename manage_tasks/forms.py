from django import forms
from .models import Task


class TaskModelForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'expected_date', 'prevision_hours']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'expected_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'prevision_hours': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
        }
