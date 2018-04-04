from django.db import models

from django.conf import settings

from django.urls import reverse

# Create your petss here.


class Pets(models.Model):
    Pets_Age = models.IntegerField(default=0)
    Pets_Animal_Type = models.CharField(max_length=200)
    Pets_Breed = models.CharField(max_length=200)
    Pets_Daily_Charges = models.IntegerField(default=0)
    Pets_Description = models.CharField(max_length=500)
    # Pets_Images = models.ForeignKey(List_of_Images, on_delete=models.CASCADE)
    Pets_Ownership_Status = models.BooleanField(default=False)
    # Pets_ID = models.IntegerField(default=0)
    Pets_Weekly_Charges = models.IntegerField(default=0)

    # Pets_Message = models.CharField(max_length=280)
    Pets_Author = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='pets', on_delete=models.CASCADE)
    Pets_Created_Date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Pets_Animal_Type

    def get_absolute_url(self):
        return reverse('pets_details', args=[str(self.id)])


# Create petss Comments here.


class Comment(models.Model):

    pets_Comment = models.CharField(max_length=150, null=False)
    # Comment_pets = models.ForeignKey(pets, null=False, on_delete=models.CASCADE)
    pets_Comment_Author = models.ForeignKey(Pets, on_delete=models.CASCADE)

    # pets_Comment_Created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.pets_Comment

    def get_absolute_url(self):
        return reverse('pets_list')
