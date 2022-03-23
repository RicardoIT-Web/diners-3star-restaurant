from django.shortcuts import render, get_object_or_404
from django.views import generic, View
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
            'booking_form': BookingForm
        }
        return render(request, 'bookingform.html', context)


class BookingList(generic.View):
    model = Booking
    template_name = 'adminbookings.html'
    paginate_by = 3



