from django.db import models

from django.conf import settings

from django.urls import reverse

# Create your location_subcategorys here.


class LocationSubCategory(models.Model):
    LocationSubCategory_Location_Category = models.CharField(max_length=100)
    Location_Subcategory = models.CharField(max_length=100)
    LocationSubCategory_Subcategory_No = models.CharField(max_length=100)

    LocationSubCategory_Modified_Date = models.DateField(auto_now_add=True)


    LocationSubCategory_Message = models.CharField(max_length=280)
    LocationSubCategory_Author = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='location_subcategory', on_delete=models.CASCADE)
    LocationSubCategory_Created_Date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.LocationSubCategory_Message

    def get_absolute_url(self):
        return reverse('location_subcategory_details', args=[str(self.id)])


# Create location_subcategorys Comments here.


class Comment(models.Model):

    location_subcategory_Comment = models.CharField(max_length=150, null=False)
    Comment_location_subcategory = models.ForeignKey(LocationSubCategory, null=False, on_delete=models.CASCADE)
    # location_subcategory_Comment_Author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # location_subcategory_Comment_Created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.location_subcategory_Comment

    def get_absolute_url(self):
        return reverse('location_subcategory_list')
