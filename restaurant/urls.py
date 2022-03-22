from . import views
from django.ulrs import path

urlpatterns = [
    path("", views.BookingList.as_view(), name="booklist"),
]