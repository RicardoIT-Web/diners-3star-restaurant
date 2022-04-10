'''
App urls bringing the MVT architecture together.
'''
from django.urls import path
from . import views
from .views import BookingAmend, BookingDelete


urlpatterns = [
    path("booking/", views.BookingFormView.as_view(), name="bookingform"),
    path("menu/", views.Menu.as_view(), name="menu"),
    path("contacts/", views.ContactFormView.as_view(), name="contacts"),
    path("booking_list/", views.BookingList.as_view(), name="user_booking"),
    path("<pk>/amend/", BookingAmend.as_view(), name="booking_amend"),
    path("<pk>/delete/", BookingDelete.as_view(), name="booking_delete"),
]
