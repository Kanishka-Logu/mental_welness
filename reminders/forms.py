from django import forms
from .models import Reminder

class ReminderForm(forms.ModelForm):
    class Meta:
        model = Reminder
        fields = ['title', 'time', 'is_active']
        widgets = {
            'time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Morning Meditation'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
