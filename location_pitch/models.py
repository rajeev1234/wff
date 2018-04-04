from django.db import models

from django.conf import settings

from django.urls import reverse

# Create your location_pitchs here.


class LocationPitch(models.Model):
    LocationPitch_By_User = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='location_pitchs', on_delete=models.CASCADE)
    LocationPitch_Location_Required = models.CharField(max_length=100)
    # pitch_locationlist = models.ForeignKey(locations, related_name='location_Pitchs', on_delete=models.CASCADE)
    LocationPitch_Submitted = models.BooleanField(default=False)

    LocationPitch_Modified_Date = models.DateField(auto_now_add=True)


    LocationPitch_Message = models.CharField(max_length=280)
    location_pitch_Author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    LocationPitch_Created_Date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.LocationPitch_Message

    def get_absolute_url(self):
        return reverse('location_pitch_details', args=[str(self.id)])


# Create location_pitchs Comments here.


class Comment(models.Model):

    location_pitch_Comment = models.CharField(max_length=150, null=False)
    Comment_location_pitch = models.ForeignKey(LocationPitch, null=False, on_delete=models.CASCADE)
    # location_pitch_Comment_Author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # location_pitch_Comment_Created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.location_pitch_Comment

    def get_absolute_url(self):
        return reverse('location_pitch_list')
