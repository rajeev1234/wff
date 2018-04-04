from django.db import models

from django.conf import settings

from django.urls import reverse

# Create your Locations here.


from django.db import models


from django.db import models

class Location(models.Model):
    Location_Area = models.CharField(max_length=100)
    Location_Authorities_Involved = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='locationss', on_delete=models.CASCADE,null=True)
    Location_Budget= models.IntegerField()
    Location_City = models.CharField(max_length=100)
    #Location_Comment = models.ForeignKey(comments, related_name='locations', on_delete=models.CASCADE)
    Location_Description = models.CharField(max_length=100)
    Location_District = models.CharField(max_length=100)
    #Location_Images = models.ForeignKey(images, related_name='locations', on_delete=models.CASCADE)
    Location_Locality = models.CharField(max_length=100)
    Location_Name = models.CharField(max_length=100)
    Location_Postal_Address = models.CharField(max_length=100)
    #Location_Category = models.ForeignKey(location_categorys, related_name='locations', on_delete=models.CASCADE)
    Location_Creator = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='crlocations', on_delete=models.CASCADE,null=True)
    Location_Financial = models.CharField(max_length=100)
    Location_Id = models.IntegerField()
    Location_Latitude = models.IntegerField()
    Location_Longitude = models.IntegerField()
    Location_Subcategory = models.CharField(max_length=100)
    Location_Modifications_Allowed = models.CharField(max_length=100)
    Location_Ownership_Status = models.CharField(max_length=100)
    Location_Pincode = models.IntegerField()
    #Location_Profile_Project = models.ForeignKey(profileprojects , related_name='locations', on_delete=models.CASCADE)
    #Location_Rating = models.ForeignKey(ratings, related_name='locations', on_delete=models.CASCADE)
    Location_Restrictions = models.CharField(max_length=100)
    #Location_Shooting_Amminities = models.ForeignKey()
    Location_State = models.CharField(max_length=100)
    Location_Street_Address = models.CharField(max_length=100)
    Location_Surrounding = models.CharField(max_length=100)
    #Location_Video = models.ForeignKey(videos, related_name='locations', on_delete=models.CASCADE)
    Location_Modified_Date =models.DateField(auto_now_add=True)
    Location_Created_Date = models.DateField(auto_now_add=True)


# Create your models here.





    def __str__(self):
        return self.Location_Area

    def get_absolute_url(self):
        return reverse('Location_details', args=[str(self.id)])


# Create Locations Comments here.


class Comment(models.Model):

    Location_Comment = models.CharField(max_length=150, null=False)
    Comment_Location = models.ForeignKey(Location, null=False, on_delete=models.CASCADE)
    Location_Comment_Author = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='commentlocation', on_delete=models.CASCADE)

    # Location_Comment_Created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Location_Comment_Author

    def get_absolute_url(self):
        return reverse('Location_list')
