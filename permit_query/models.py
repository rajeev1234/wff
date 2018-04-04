from django.db import models

from django.conf import settings

from django.urls import reverse

# Create your permit_querys here.


class PermitQuery(models.Model):
    # PermitQuery_Address_Components = models.ForeignKey(List_of_Authority_identification_call_address_components,
    #                                       on_delete=models.CASCADE)
    PermitQuery_API_Address = models.CharField(max_length=200)
    PermitQuery_City_State_Country = models.CharField(max_length=200)
    PermitQuery_Latitude = models.IntegerField(default=0)
    # PermitQuery_List_Long_name = models.ForeignKey(List_Of_Texts, on_delete=models.CASCADE)
    # PermitQuery_List_Short_Name = models.ForeignKey(List_Of_Texts, on_delete=models.CASCADE)
    # PermitQuery_List_Type = models.ForeignKey(List_Of_Texts, on_delete=models.CASCADE)
    PermitQuery_Location = models.CharField(max_length=200)
    PermitQuery_Longitude = models.IntegerField(default=0)
    PermitQuery_Map_Address = models.CharField(max_length=100)
    Permit_Query_Number = models.IntegerField(default=0)
    PermitQuery_Query_Mode = models.CharField(max_length=200)
    PermitQuery_Street_Address = models.CharField(max_length=200)

    # PermitQuery_Message = models.CharField(max_length=280)
    PermitQuery_Author = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='permit_query', on_delete=models.CASCADE)
    PermitQuery_Created_Date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.PermitQuery_City_State_Country

    def get_absolute_url(self):
        return reverse('permit_query_details', args=[str(self.id)])


# Create permit_querys Comments here.


class Comment(models.Model):

    permit_query_Comment = models.CharField(max_length=150, null=False)
    # Comment_permit_query = models.ForeignKey(permit_query, null=False, on_delete=models.CASCADE)
    permit_query_Comment_Author = models.ForeignKey(PermitQuery, on_delete=models.CASCADE)

    # permit_query_Comment_Created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.permit_query_Comment

    def get_absolute_url(self):
        return reverse('permit_query_list')
