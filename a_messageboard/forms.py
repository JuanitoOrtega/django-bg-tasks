from django.forms import ModelForm
from django import forms
from .models import MessageBoard, Message


class MessageCreateForm(ModelForm):
    class Meta:
        model = Message
        fields = ['body']
        widgets = {
            'body': forms.TextInput(attrs={'placeholder': 'Escribe un mensaje...', 'class': 'p-4 text-black', 'maxlength': 2000}),
        }