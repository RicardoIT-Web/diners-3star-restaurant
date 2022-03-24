from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Booking
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
        # context = {
        #     'booking_form': BookingForm()
        # }

        booking_form = BookingForm(data=request.POST)
        if booking_form.is_valid():
            booking = booking_form.save(commit=False)
            booking.user = request.user
            print(booking)

            booking.save()
        else:
            print('Form not valid')
            print(booking_form)

        return render(
            request, 'index.html',)


class BookingList(generic.View):
    model = Booking
    template_name = 'adminbookings.html'
    paginate_by = 3
