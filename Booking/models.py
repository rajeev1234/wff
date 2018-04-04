from django.db import models

from django.conf import settings

from django.urls import reverse

# Create your bookings here.


class Booking(models.Model):
    #booking_from = models.ForeignKey(User,related_name='bookings', on_delete=models.CASCADE)
    #date = models.ForeignKey(dates, related_name='bookings', on_delete=models.CASCADE)
    Booking_Status = models.TextField(max_length=100,unique=True)
    #creator = models.ForeignKey(User, related_name='bookings', on_delete=models.CASCADE)
    Booking_Modified_Date = models.DateTimeField(auto_now_add=True)
    Booking_Created_Date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Booking_Status

    def get_absolute_url(self):
        return reverse('booking_details', args=[str(self.id)])


# Create bookings Comments here.


class Comment(models.Model):

    Booking_Comment = models.CharField(max_length=150, null=False)
    Comment_Booking = models.ForeignKey(Booking, null=False,related_name="Comment_Bookingnew", on_delete=models.CASCADE)
    Booking_Comment_Author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name="booking_comment")

    # booking_Comment_Created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Booking_Comment

    def get_absolute_url(self):
        return reverse('booking_list')

