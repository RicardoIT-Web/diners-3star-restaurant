from django import forms
from .models import Booking
from django.forms import ValidationError
from django.http import HttpResponseRedirect


class DateInput(forms.DateInput):
    input_type = 'date'


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('table', 'group_size', 'date', 'start_time', 'end_time', 'comment', )
        widgets = {
            'date': DateInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date'].widgets = forms.widgets.DateInput(
            attrs={'type': 'date'})
        self.fields['start_time'].widget = forms.widgets.TimeInput(
             attrs={'type': 'time'})
        self.fields['end_time'].widget = forms.widgets.TimeInput(
             attrs={'type': 'time'})
