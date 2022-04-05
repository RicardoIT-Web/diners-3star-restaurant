'''
The forms.py file used to create the structure of the forms
which will be used by Admin and Users for data creation and extraction
'''
from django import forms
# from django.http import HttpResponseRedirect
from .models import Booking, Contact
# from django.forms import ValidationError


class DateInput(forms.DateInput):
    '''
    This class method is nesessary to assist with providing
    the widgets of the date field in the booking form with a
    calendar view for the User
    '''
    input_type = 'date'


class BookingForm(forms.ModelForm):
    '''
    The booking form which connects to the views and provides the User with
    the required fields to be displayed at frontend
    '''
    class Meta:
        '''
        Class meta to define which model to pull data from
        '''
        model = Booking
        fields = (
            'table', 'group_size', 'date', 'start_time', 'end_time', 'comment',
            )
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


class ContactForm(forms.ModelForm):
    '''
    The contact form which connects to the views and provides the User with
    the required fields to be displayed at frontend
    '''
    class Meta:
        '''
        Calss meta to define which model to pull data from
        '''
        model = Contact
        fields = ('name', 'email', 'phone_number', 'comment', )
