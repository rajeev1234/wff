from django.db import models

from django.conf import settings

from django.urls import reverse

from django.contrib.auth.models import User

# Create your location_financials here.


class LocationFinancial(models.Model):
    # LocationFinancial_Authority_Charges = models.ForeignKey(on_delete=models.CASCADE)
    LocationFinancial_Availability = models.BooleanField(default=False)
    LocationFinancial_Discount_On_Crewsize = models.BooleanField(default=False)
    LocationFinancial_Discount_On_Shoot_Length = models.BooleanField(default=False)
    LocationFinancial_Location_Id = models.CharField(max_length=280)
    LocationFinancial_Monthly_Rate_Crewsize1 = models.CharField(max_length=100)
    LocationFinancial_Monthly_Rate_Crewsize2 = models.CharField(max_length=100)
    LocationFinancial_Monthly_Rate_Crewsize3 = models.CharField(max_length=100)
    LocationFinancial_Monthly_Rate_Crewsize4 = models.CharField(max_length=100)
    LocationFinancial_One_Day_Rent_Crewsize1 = models.CharField(max_length=100)
    LocationFinancial_One_Day_Rent_Crewsize2 = models.CharField(max_length=100)
    LocationFinancial_One_Day_Rent_Crewsize3 = models.CharField(max_length=100)
    LocationFinancial_One_Day_Rent_Crewsize4 = models.CharField(max_length=100)
    LocationFinancial_Prices_Available = models.BooleanField(default=False)
    LocationFinancial_Student_Rate = models.CharField(max_length=100)
    LocationFinancial_Weekly_Rate_Crewsize1 = models.CharField(max_length=100)
    LocationFinancial_Weekly_Rate_Crewsize2 = models.CharField(max_length=100)
    LocationFinancial_Weekly_Rate_Crewsize3 = models.CharField(max_length=100)
    LocationFinancial_Weekly_Rate_Crewsize4 = models.CharField(max_length=100)
    LocationFinancial_Modified_Date = models.DateField(auto_now=True)
    LocationFinancial_Creator = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='locationfinancials', on_delete=models.CASCADE)
    LocationFinancial_Created_Date = models.DateField(auto_now=True)


    # LocationFinancial_Message = models.CharField(max_length=280)
    # LocationFinancial_Author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # Created_Date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.LocationFinancial_Location_Id)

    def get_absolute_url(self):
        return reverse('location_financial_details', args=[str(self.id)])


# Create location_financials Comments here.


class Comment(models.Model):

    LocationFinancial_Comment = models.CharField(max_length=150, null=True)
    Comment_LocationFinancial = models.ForeignKey(LocationFinancial, null=True, on_delete=models.CASCADE)
    # location_financial_Comment_Author = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='location_financial_comment', on_delete=models.CASCADE)

    # location_financial_Comment_Created_on = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.LocationFinancial_Comment

    def get_absolute_url(self):
        return reverse('location_financial_list')
