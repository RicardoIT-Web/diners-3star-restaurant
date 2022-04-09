'''
The Views.py file to create the User views display on the frontend.
'''
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from .forms import BookingForm, ContactForm
from .models import Booking


class Home(View):
    '''
    The home view is to indicate which html
    template to be used as the landing page for this application
    '''
    def get(self, request):
        '''
        Rendering the index.html template as the landing page
        '''
        return render(request, 'index.html',)


class Menu(View):
    '''
        The meu view is to indicate which html
        template to be used as the Menu page for this application
    '''
    def get(self, request):
        '''
        Rendering the menu.html template as the landing page
        '''
        return render(request, 'menu.html',)


class BookingList(TemplateView):

    template_name = 'user_booking.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(
            bookings=self.request.user.booking_set.all(),
            **kwargs
        )


class BookingFormView(View):
    '''
    The Booking form view pulling data from the booking form in forms.py
    This will allow for the booking form to be viewable in the frontend.
    '''

    def get(self, request):
        '''
        This gets the form data from the booking form and displays it
        '''
        context = {
            'booking_form': BookingForm()
        }
        return render(request, 'bookingform.html', context)

    def post(self, request):
        '''
        This posts the User data input to the database
        '''
        booking_form = BookingForm(data=request.POST)
        if booking_form.is_valid():
            booking = booking_form.save(commit=False)
            booking.user = request.user
            if Booking.objects.filter(
                    table=booking.table, date=booking.date,
                    start_time=booking.start_time,
                    approved=booking.approved is True
                    ).exists():
                return render(request, 'booking_not_avail.html',)
            else:
                booking.save()
            return render(request, 'booking_successful.html',)


class ContactFormView(View):
    '''
    This form is to display the contacts form in the frontend
    for the User to be able to view it
    '''

    def get(self, request):
        '''
        This gets the required data from the contactform
        '''
        context = {
            'contact_form': ContactForm()
        }
        return render(request, 'contacts.html', context)

    def post(self, request):
        '''
        This posts the User data from the frontend
        and sends that data to the backend
        '''
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            contact = contact_form.save(commit=False)
            contact.save()

        return render(request, 'index.html',)
