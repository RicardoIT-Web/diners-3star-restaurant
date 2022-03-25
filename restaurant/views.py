from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Booking, Table
from .forms import BookingForm


class Home(View):

    def get(self, request):
        return render(request, 'index.html')


class Menu(View):

    def get(self, request):
        return render(request, 'menu.html')


class BookingFormView(View):

    def get(self, request):
        context = {
            'booking_form': BookingForm()
        }
        return render(request, 'bookingform.html', context)

    def post(self, request):

        booking_form = BookingForm(data=request.POST)
        print(booking_form)
        if booking_form.is_valid():
            # forms valid - need to check availability
            # if ....
            booking = booking_form.save(commit=False)
            booking.user = request.user
            booking.save()
    
    def double_booking(self, table, date, start_time, end_time):
        double_booking = BookingForm.objects.all()
        if double_booking == BookingForm(table, date, start_time, end_time):
            raise BookingForm.ValidationError(f'{table} is already booked. Please select another.')
        return HttpResponseRedirect('bookingform.html')


        return render(request, 'index.html',)


class BookingList(generic.View):
    model = Booking
    template_name = 'adminbookings.html'
    paginate_by = 3
