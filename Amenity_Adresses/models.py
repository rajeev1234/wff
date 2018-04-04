# Create your models here.
from django.db import models

from django.conf import settings

from django.urls import reverse

# Create your amenity_adressess here.


class Amenity_Adresses(models.Model):

    Amenity_Adresses_Car_Parking = models.CharField(max_length=100,blank=True,null=True)
    Amenity_Adresses_Catering_Base = models.CharField(max_length=100,blank=True,null=True)
    Amenity_Adresses_Genset_Parking = models.CharField(max_length=100,blank=True,null=True)
    Amenity_Adresses_Location_Id = models.CharField(max_length=100,unique=True)
    Amenity_Adresses_Truck_Parking = models.CharField(max_length=100,blank=True,null=True)
    Amenity_Adresses_Vanity_Parking = models.CharField(max_length=100,blank=True,null=True)
    #creator =models.ForeignKey(User, related_name='amenity_adressess',on_delete=models.CASCADE)
    Amenity_Adresses_Modified_Date = models.DateTimeField(auto_now_add=True)
    Amenity_Adresses_Created_Date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Amenity_Adresses_Car_Parking

    def get_absolute_url(self):
        return reverse('amenity_adresses_details', args=[str(self.id)])


# Create amenity_adressess Comments here.


class Comment(models.Model):

    Amenity_Adresses_Comment = models.CharField(max_length=150, null=False)
    Comment_Amenity_Adresses = models.ForeignKey(Amenity_Adresses,related_name="amenity_adress", null=False, on_delete=models.CASCADE)
    Amenity_Adresses_Comment_Author = models.ForeignKey(settings.AUTH_USER_MODEL,related_name="amenity_adresses", on_delete=models.CASCADE)

    # amenity_adresses_Comment_Created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Amenity_Adresses_Comment

    def get_absolute_url(self):
        return reverse('amenity_adresses_list')


