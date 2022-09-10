from dataclasses import fields
from django import forms
from .models import Quiz 
from django.core.exceptions import ValidationError

class Quizform(forms.ModelForm):
    class Meta:
        model=Quiz
        fields='__all__'


