from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.core.validators import RegexValidator


STATUS = ((0, "Available"), (1, "Unavailable"))


class Table(models.Model):
    """
    All tables deemed to be single table seating 2 people each.
    """
    TABLE_LOCATION = (
        ('OUTSIDE', 'OUTSIDE'),
        ('WINDOW', 'WINDOW'),
        ('HALL', 'HALL')
    )
    number = models.IntegerField()
    location = models.CharField(max_length=10, choices=TABLE_LOCATION)
    capacity = models.IntegerField()
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return f'Table {self.number}, {self.location}. Capacity {self.capacity} guests'


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    group_size = models.PositiveIntegerField()
    date = models.DateField(blank=True)
    start_time = models.TimeField(auto_now_add=False, blank=True)
    end_time = models.TimeField(auto_now_add=False, blank=True)
    comment = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.table}. Booked by {self.user} for {self.group_size} people, for the {self.date} at {self.start_time}.'


class Contact(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(null=False)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    comment = models.CharField(blank=True, max_length=250)
    actioned = models.BooleanField(default=False)
