'''
The Views.py file to create the User views display on the frontend.
'''
from django.shortcuts import render
from django.views import View
# from django.http import HttpResponseRedirect
# from django.contrib.auth.models import User
from .forms import BookingForm, ContactForm


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
            # forms valid - need to check availability
            # if BookingForm.table

            booking.save()

    # def double_booking(self, table, date, start_time, end_time):
    #     double_booking = BookingForm.objects.all()
    #     if double_booking == BookingForm(table, date, start_time, end_time):
    #         raise BookingForm.ValidationError(f'{table} is already booked.
    # Please select another.')
    #     return HttpResponseRedirect('bookingform.html')

        return render(request, 'index.html',)


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
