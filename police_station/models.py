from django.db import models

from django.conf import settings

from django.urls import reverse

# Create your police_stations here.


class PoliceStation(models.Model):
    PoliceStation_Area_Police_Station = models.CharField(max_length=200)
    PoliceStation_DCP = models.CharField(max_length=200)
    PoliceStation_Station_Name = models.CharField(max_length=200)

    # PoliceStation_Message = models.CharField(max_length=280)
    PoliceStation_Author = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='police_station', on_delete=models.CASCADE)
    PoliceStation_Created_Date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.PoliceStation_Station_Name

    def get_absolute_url(self):
        return reverse('police_station_details', args=[str(self.id)])


# Create police_stations Comments here.


class Comment(models.Model):

    police_station_Comment = models.CharField(max_length=150, null=False)
    # Comment_police_station = models.ForeignKey(police_station, null=False, on_delete=models.CASCADE)
    police_station_Comment_Author = models.ForeignKey(PoliceStation, on_delete=models.CASCADE)

    # police_station_Comment_Created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.police_station_Comment

    def get_absolute_url(self):
        return reverse('police_station_list')
