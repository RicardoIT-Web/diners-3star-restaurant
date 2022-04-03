from django.urls import path
from . import views


urlpatterns = [
    path("booking/", views.BookingFormView.as_view(), name="bookingform"),
    path("menu/", views.Menu.as_view(), name="menu"),
    path("contacts/", views.ContactFormView.as_view(), name="contacts"),
]
