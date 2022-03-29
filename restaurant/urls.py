from django.urls import path, include
from . import views


urlpatterns = [
    path("booking/", views.BookingFormView.as_view(), name="bookingform"),
]
