from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Booking


class Home(View):

    def get(self, request):
        return render(request, 'index.html')


class Menu(View):

    def get(self, request):
        return render(request, 'menu.html')


class BookingList(generic.View):
    model = Booking
    template_name = 'bookings.html'
    paginate_by = 3
