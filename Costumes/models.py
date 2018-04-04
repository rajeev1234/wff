from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils import timezone


# Base Model for costumes app
class Costume(models.Model):
    Costume_Color = models.CharField(max_length=100)
    Costume_Category = models.CharField(max_length=100)
    Costume_Style = models.CharField(max_length=100)
    Costume_Description = models.CharField(max_length=100)
    Costume_Type = models.CharField(max_length=100)
    # Costume_Image = models.ForeignKey(images, related_name='Costumes', on_delete=models.CASCADE)
    Costume_Modification_Allowed = models.BooleanField()
    Costume_Trend_Year = models.DateField()
    Costume_Weekly_Rent = models.IntegerField()
    Costume_Creator = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='Costumes', on_delete=models.CASCADE)
    Costume_Modified_Date = models.DateField(auto_now_add=True,editable=True)
    Costume_Created_Date = models.DateField(auto_now_add=True,editable=True)

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse('Costume_details', args=[str(self.id)])

# Comment 
class Comment(models.Model):

    Costume_Comment = models.CharField(max_length=150, null=False)
    Comment_Costume = models.ForeignKey(Costume,related_name='Comment', null=False, on_delete=models.CASCADE)
    Costume_Comment_Author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'Comments', on_delete=models.CASCADE)
    Costume_Comment_Created_On = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Costume_Comment

    def get_absolute_url(self):
        return reverse('Costume_list')



