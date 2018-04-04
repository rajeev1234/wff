from django.db import models

from django.conf import settings

from django.urls import reverse
from django.db import models

class Location_Category(models.Model):
    Location_Category_No = models.IntegerField(max_length=100)
    Location_Category_Name = models.CharField(max_length=100)
    Location_Category_Creator = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='location_categorys', on_delete=models.CASCADE,null=True)
    Location_Category_Modified_Date = models.DateField(auto_now_add=True)
    Location_Category_Created_Date = models.DateField(auto_now_add=True)



# Create your models here.

    def __str__(self):
        return self.Location_Category_Name

    def get_absolute_url(self):
        return reverse('Location_Category_details', args=[str(self.id)])


# Create Locations Comments here.


class Comment(models.Model):
    Location_Category_Comment = models.CharField(max_length=150, null=False)
    Comment_Location_Category = models.ForeignKey(Location_Category, null=False, on_delete=models.CASCADE)
    Location_Category_Comment_Author = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='commentlocation_category', on_delete=models.CASCADE,null=True)

    # Location_Comment_Created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Location_Category_Comment_Author

    def get_absolute_url(self):
        return reverse('location_category_list')
