from django.db import models
from django.conf import settings
from django.urls import reverse


class District(models.Model):
    District_Code = models.CharField(max_length=100)
    District_Complete = models.BooleanField()
    # District_Contact_Number = models.ForeignKey(contact_numbers , related_name='districts', on_delete=models.CASCADE)
    District_Name = models.CharField(max_length=100)
    District_Email = models.CharField(max_length=100)
    District_Headquater = models.CharField(max_length=100)
    # District_Office_Contrat = models.ForeignKey(officecontrats, related_name='districts', on_delete=models.CASCADE)
    District_Phq = models.CharField(max_length=100)
    District_Phq_Email = models.CharField(max_length=100)
    District_Phq_Postal_Address = models.CharField(max_length=100)
    District_Phq_Web = models.CharField(max_length=100)
    District_Police_Hqaddress = models.CharField(max_length=100)
    District_Postal_Address = models.CharField(max_length=100)
    District_State = models.CharField(max_length=100)
    District_Web_Address = models.CharField(max_length=100)
    District_Creator = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='districts', on_delete=models.CASCADE)
    District_Modified_Date = models.DateField(auto_now_add=True,editable=True)
    District_Created_Date = models.DateField(auto_now_add=True,editable=True)


    def __str__(self):
        return self.District_Name

    def get_absolute_url(self):
        return reverse('District_details', args=[str(self.id)])



class Comment(models.Model):

    District_Comment = models.CharField(max_length=150, null=False)
    Comment_District = models.ForeignKey(District, related_name="Comments" ,null=False, on_delete=models.CASCADE)
    District_Comment_Author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="comments_comment", on_delete=models.CASCADE)

    # District_Comment_Created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.District_Comment

    def get_absolute_url(self):
        return reverse('District_list')