from django.db import models

from django.conf import settings

from django.urls import reverse
from django.db import models

class Prop(models.Model):
    Prop_Color = models.CharField(max_length=200)
    Prop_Daily_Rent = models.IntegerField()
    #Prop_Images = models.ForeignKey(List_Of_Images, on_delete=models.CASCADE)
    Prop_Making_Year = models.DateField(auto_now_add=True)
    Prop_Modification_Allowed = models.BooleanField(max_length=200)
    Prop_Ownership_Status = models.BooleanField()
    Prop_ID = models.IntegerField()
    Prop_Make = models.CharField(max_length=200)
    Prop_Type = models.CharField(max_length=200)
    Prop_Weekly_Rent = models.IntegerField()
    Prop_Creator = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='Prop',on_delete=models.CASCADE, null=True)
    Prop_Modified_Date = models.DateField(auto_now_add=True)
    Prop_Created_Date = models.DateField(auto_now_add=True)

    # Create your models here.

    def __str__(self):
        return self.Prop_ID

    def get_absolute_url(self):
        return reverse('Prop_details', args=[str(self.id)])


# Create Props Comments here.


class Comment(models.Model):

    Prop_Comment = models.CharField(max_length=150, null=False)
    Comment_Prop = models.ForeignKey(Prop, null=False, on_delete=models.CASCADE)
    Prop_Comment_Author = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='commentProp', on_delete=models.CASCADE)

    # Prop_Comment_Created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Prop_Comment_Author

    def get_absolute_url(self):
        return reverse('Prop_list')
