from django.db import models

from django.conf import settings

from django.urls import reverse

# Create your Locations here.


from django.db import models

from django.db import models

class Location_Amenitie(models.Model):
    Location_Amenitie_Carparking = models.BooleanField()
    Location_Amenitie_Carparking_Latitide = models.IntegerField()
    Location_Amenitie_Carparking_Longitude = models.IntegerField()
    Location_Amenitie_Catering_Base = models.BooleanField()
    Location_Amenitie_Catering_Base_Latitude = models.IntegerField()
    Location_Amenitie_Catering_Base_Longitude = models.IntegerField()
    Location_Amenitie_Controlling_Status = models.CharField(max_length=100)
    Location_Amenitie_Genset_Parking = models.BooleanField()
    Location_Amenitie_Genset_Parking_Latitude = models.IntegerField()
    Location_Amenitie_Genset_Parking_Longitude = models.IntegerField()
    Location_Amenitie_Location_Id = models.IntegerField()
    Location_Amenitie_Truck_Parking_Latitude = models.IntegerField()
    Location_Amenitie_Truck_Parking_Longitude = models.IntegerField()
    Location_Amenitie_Vanity_Parking = models.BooleanField()
    Location_Amenitie_Vanity_Parking_Latitude = models.IntegerField()
    Location_Amenitie_Vanity_Parking_Longitude = models.IntegerField()
    Location_Amenitie_Washroom = models.BooleanField()
    Location_Amenitie_Creator = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='locatonamenities',on_delete=models.CASCADE,null=True)
    Location_Amenitie_Modified_Date = models.DateField(auto_now_add=True)
    Location_Amenitie_Created_Date = models.DateField(auto_now_add=True)




# Create your models here.


# Create your models here.





    def __str__(self):
        return self.Location_Amenitie_Carparking

    def get_absolute_url(self):
        return reverse('Location_Amenitie_details', args=[str(self.id)])


# Create Locations Comments here.


class Comment(models.Model):

    Location_Amenitie_Location_Comment = models.CharField(max_length=150, null=False)
    Location_Amenitie_Comment_Location = models.ForeignKey(Location_Amenitie, null=False, on_delete=models.CASCADE)
    Location_Amenitie_Location_Comment_Author = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='commentLocation_Amenitie', on_delete=models.CASCADE,null=True)

    # Location_Comment_Created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Location_Amenitie_Location_Comment_Author

    def get_absolute_url(self):
        return reverse('Location_Amenitie_list')
