from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Booking, Table



@admin.register(Booking)
class BookingAdmin(SummernoteModelAdmin):

    list_display = ('user', 'table', 'group_size', 'date', 'start_time', 'end_time', 'comment', 'created_on', 'approved')
    search_fields = ('user', 'date', 'table', 'group_size', 'start_time')
    list_filter = ('table', 'approved', 'created_on')
    summernote_fields = ('comment')
    actions = ['approved_bookings']

    def approved_bookings(self, request, queryset):
        queryset.update(approved=True)


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):

    list_filter = ('location', 'status')
    list_display = ('number', 'location', 'capacity', 'status')
