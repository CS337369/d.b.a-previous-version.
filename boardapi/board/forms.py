from django import forms
from .models import Board

# class DateInput(forms.DateInput):
#     input_type = 'date'

class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ('b_title', 'b_note')
        # widgets = {
        #     'end_date' : DateInput()
        # }