'''
The admin.py file to create the view layouts and fuctionality
visible to the administrator
'''
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Booking, Table, Contact


@admin.register(Booking)
class BookingAdmin(SummernoteModelAdmin):
    '''
    The booking feature for the admin view
    '''
    list_display = ('user', 'table', 'group_size', 'date', 'start_time',
                    'end_time', 'comment', 'created_on', 'approved')
    search_fields = ('user', 'date', 'table', 'group_size', 'start_time')
    list_filter = ('table', 'approved', 'created_on')
    summernote_fields = ('comment')
    actions = ['approved_bookings']

    def approved_bookings(self, queryset):
        '''
        function to allow admin to approve
        '''
        queryset.update(approved=True)


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    '''
    The table feature for the admin view
    '''
    list_filter = ('location', 'status')
    list_display = ('number', 'location', 'capacity', 'status')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    '''
    The contact feature for the admin view
    '''
    list_display = ('name', 'email', 'phone_number', 'comment', 'actioned')
    search_fields = ('name', 'email', 'number', 'actioned')
