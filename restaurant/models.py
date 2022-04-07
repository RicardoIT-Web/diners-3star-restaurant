'''
The Restaurant app models required for adminand User functionality.
'''
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from cloudinary.models import CloudinaryField


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
    '''
    This booking model is to allow for User and Admin to create bookings
    '''
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    group_size = models.PositiveIntegerField()
    date = models.DateField(blank=False)
    start_time = models.TimeField(auto_now_add=False, blank=False)
    end_time = models.TimeField(auto_now_add=False, blank=False)
    comment = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.table}. Booked by {self.user} for {self.group_size} people, for the {self.date} at {self.start_time}.'


class Contact(models.Model):
    '''
    This Contact model is to allow Users to reach out to the Restaurant to
    raise any questions or provide any suggests of improvement
    '''
    name = models.CharField(max_length=150)
    email = models.EmailField(null=False)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+9999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(
        validators=[phone_regex], max_length=17, blank=True)
    comment = models.CharField(blank=True, max_length=250)
    actioned = models.BooleanField(default=False)
