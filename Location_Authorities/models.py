from django.db import models

from django.conf import settings

from django.urls import reverse

# Create your Locations here.


from django.db import models

from django.db import models

from django.db import models

class LocationAuthority(models.Model):
    Location_Authority_Detail = models.CharField(max_length=100)
    Location_Authority_Email = models.EmailField()
    Location_Authority_Google_Address = models.EmailField(default=0)
    Location_Authority_Latitude = models.IntegerField()
    Location_Authority_Longitude = models.IntegerField()
    Location_Authority_Name = models.CharField(max_length=100)
    Location_Authority_Postal_Address = models.CharField(max_length=100)
    Location_Authority_Contact_Number = models.IntegerField()
    Location_Authority_Contact_Name = models.CharField(max_length=100)
    #Location_Authoritie_Contact_Officer = models.ForeignKey(contact_officers, related_name='location_authorities', on_delete=models.CASCADE)
    Location_Authority_Locality_City_State = models.CharField(max_length=100)
    Location_Authority_Location_ID = models.IntegerField()
    Location_Authority_Office_Charges = models.IntegerField()
    Location_Authority_Street_Address = models.CharField(max_length=100)
    Location_Authority_Creator = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='locationauthorities', on_delete=models.CASCADE,null=True)
    Location_Authority_Modified_Date = models.DateField(auto_now_add=True)
    Location_Authority_Created_Date = models.DateField(auto_now_add=True)



    def __str__(self):
        return self.Location_Authority_Email

    def get_absolute_url(self):
        return reverse('Location_Authorities_details', args=[str(self.id)])


# Create Locations Comments here.


class Comment(models.Model):
    Location_Authority_Comment = models.CharField(max_length=150, null=False)
    Comment_Location_Authority = models.ForeignKey(LocationAuthority, null=False, on_delete=models.CASCADE)
    Location_Authority_Comment_Author = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='commentLocation_Authorities', on_delete=models.CASCADE,null=True)

    # Location_Comment_Created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Location_Authority_Comment_Author

    def get_absolute_url(self):
        return reverse('Location_Authorities_list')
