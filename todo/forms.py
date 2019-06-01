from django.forms import ModelForm

from .models import ToDoItem

class ToDoItemForm(ModelForm):
    class Meta:
        model = ToDoItem
        fields = ['text']
