from django.urls import path, include
from . import views


urlpatterns = [
    # path("restaurant/", views.Menu.as_view(), name="menu"),
    # path("restaurant/", views.BookingList.as_view(), name="booklist"),
    path("booking/", views.BookingFormView.as_view(), name="bookingform"),
]
