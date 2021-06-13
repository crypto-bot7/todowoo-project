from django.forms import ModelForm
from django import forms
from .models import Todo


class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime'


class TodoForm(ModelForm):
    class Meta:
        model = Todo
        widgets = {'dueTime': forms.DateTimeInput()}
        fields = ['title', 'memo', 'important', 'dueTime']
