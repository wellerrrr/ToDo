from django import forms
from .models import ToDoList


class PostForm(forms.ModelForm):
    class Meta:
        model = ToDoList
        fields = ['title', 'is_complete']
        widgets = {
            'title': forms.Textarea(attrs={'class': 'title-input rounded py-2 px-2 form-control',
                                           'placeholder': 'Title', 'rows': 3}),
            # 'desc': forms.Textarea(attrs={'class': 'rounded py-2 px-2', 'placeholder': 'Description', 'size': 60, 'rows': 6}),
        }