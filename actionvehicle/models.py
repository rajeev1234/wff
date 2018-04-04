



# Create your models here.
from django.db import models

from django.conf import settings

from django.urls import reverse
# from image.models import images

# Create your actionvehicles here.


class ActionVehicle(models.Model):
    ActionVehicle_Action_Vehicle_Id = models.CharField(max_length=100, unique=True)
    ActionVehicle_Color = models.TextField(max_length=100,null=True,blank=True)
    ActionVehicle_Company = models.TextField(max_length=100)
    ActionVehicle_Daily_Rent = models.CharField(max_length=100)
    ActionVehicle_Description = models.TextField(max_length=100)
    # image = models.ForeignKey(images,related_names = 'actionvechiles',on_delete=models.CASCADE )
    ActionVehicle_Make = models.DateTimeField(auto_now_add=True,editable=False)
    ActionVehicle_Model = models.TextField(max_length=100)
    ActionVehicle_Modification = models.BooleanField(default=False)
    ActionVehicle_Monthly_Rent = models.CharField(max_length=100)
    ActionVehicle_Ownership = models.BooleanField(default=False)
    # ownership_proof =models.ForeignKey(ownershipproofs, related_name='actionvechicles', on_delete=models.CASCADE)
    ActionVehicle_Registration_Number = models.TextField(max_length=100)
    ActionVehicle_Rigging = models.BooleanField(default=False)
    ActionVehicle_Weekly_Rent = models.CharField(max_length=50)
    # creator =models.ForeignKey(settings.AUTH_USER_MODEL, related_name='actionvechicles', on_delete=models.CASCADE)
    ActionVehicle_Modified_Date=models.DateTimeField(auto_now_add=True,editable=True)
    ActionVehicle_Created_Date=models.DateTimeField(auto_now_add=True,editable=True)

    def __str__(self):
        return self.ActionVehicle_Action_Vehicle_Id

    def get_absolute_url(self):
        return reverse('actionvehicle_details', args=[str(self.id)])


# Create actionvehicles Comments here.


class Comment(models.Model):

    ActionVehicle_Action_Vehicle_Comment = models.CharField(max_length=150, null=False)
    Comment_Action_Vehicle = models.ForeignKey(ActionVehicle, null=False, related_name="action",on_delete=models.CASCADE)
    ActionVehicle_Comment_Author = models.ForeignKey(settings.AUTH_USER_MODEL,related_name="actionvehicle",on_delete=models.CASCADE)

    # actionvehicle_Comment_Created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ActionVehicle_Action_Vehicle_Comment

    def get_absolute_url(self):
        return reverse('actionvehicle_list')
