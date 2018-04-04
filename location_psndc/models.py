from django.db import models

from django.conf import settings

from django.urls import reverse

# Create your location_psndcs here.


class LocationPSnDC(models.Model):
    LocationPSnDC_Dc_Office = models.CharField(max_length=100)
    LocationPSnDC_Dcp_Office = models.CharField(max_length=100)
    LocationPSnDC_Location_Id = models.CharField(max_length=100)
    LocationPSnDC_Police_Station = models.CharField(max_length=100)

    LocationPSnDC_Modified_Date = models.DateField(auto_now_add=True)
    LocationPSnDC_Created_Date = models.DateField(auto_now_add=True)

    LocationPSnDC_Message = models.CharField(max_length=280)
    LocationPSnDC_Author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='location_psndcs', on_delete=models.CASCADE)


    def __str__(self):
        return self.LocationPSnDC_Message

    def get_absolute_url(self):
        return reverse('location_psndc_details', args=[str(self.id)])


# Create location_psndcs Comments here.


class Comment(models.Model):

    location_psndc_Comment = models.CharField(max_length=150, null=False)
    Comment_location_psndc = models.ForeignKey(LocationPSnDC, null=False, on_delete=models.CASCADE)
    # location_psndc_Comment_Author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # location_psndc_Comment_Created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.location_psndc_Comment

    def get_absolute_url(self):
        return reverse('location_psndc_list')
