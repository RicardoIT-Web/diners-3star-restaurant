from .models import Booking
from django import forms


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
            attrs={'type': ''})
        self.fields['start_time'].widget = forms.widgets.TimeInput(
             attrs={'type': 'time'})
        self.fields['end_time'].widget = forms.widgets.TimeInput(
             attrs={'type': 'time'})


        # def check_table_availability(self, table):
        #     available_tables = []
        #     bookings = Booking.objects.filter(table=table, date=date, start_time=start_time, end_time=end_time)
        #     for bookings in Booking:
        #         if bookings.date and bookings.start_time > Bookings.end_time:
        #             available_tables.append(True)
        #         elif bookings.date and bookings.start_time < Bookings.end_time:
        #             available_tables.append(True)
        #         else:
        #             available_tables.append(False)
        #     return all(available_tables)
