from .models import Booking
from django import forms


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('table', 'group_size', 'date', 'start_time', 'end_time', 'comment', )
