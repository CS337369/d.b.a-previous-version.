import os
from django import forms
from .models import Board, Comment

class BoardForm(forms.ModelForm):
    pass


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'c_note'
        ]





