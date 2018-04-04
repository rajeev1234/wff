from django.db import models
from django.conf import settings
from django.urls import reverse


class FilmLocationFromGuidedWithSerial(models.Model):
    FilmLocationFromGuidedWithSerial_Arrival_Time = models.DateField()
    FilmLocationFromGuidedWithSerial_Departure_Time= models.CharField(max_length=100)
    FilmLocationFromGuidedWithSerial_Location_From_Guideno = models.CharField(max_length=100)
    FilmLocationFromGuidedWithSerial_Location = models.CharField(max_length=100)
    # FilmLocationFromGuidedWithSerial_Tourguide = models.ForeignKey()
    FilmLocationFromGuidedWithSerial_Creator= models.ForeignKey(settings.AUTH_USER_MODEL, related_name='filmlocationfromguideds', on_delete=models.CASCADE)
    FilmLocationFromGuidedWithSerial_Modified_Date = models.DateField(auto_now_add = True , editable=True)
    FilmLocationFromGuidedWithSerial_Created_Date = models.DateField(auto_now_add = True , editable=False)
    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse('FilmLocationFromGuidedWithSerial_details', args=[str(self.id)])



# Create FilmLocationFromGuidedWithSerials Comments here.


class Comment(models.Model):

    FilmLocationFromGuidedWithSerial_Comment = models.CharField(max_length=150, null=False)
    Comment_FilmLocationFromGuidedWithSerial = models.ForeignKey(FilmLocationFromGuidedWithSerial, null=False,related_name='commentsFilmLocationFromGuidedWithSerial', on_delete=models.CASCADE)
    FilmLocationFromGuidedWithSerial_Comment_Author = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='CommentssFilmLocationFromGuidedWithSerial', on_delete=models.CASCADE)

    # FilmLocationFromGuidedWithSerial_Comment_Created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.FilmLocationFromGuidedWithSerial_Comment

    def get_absolute_url(self):
        return reverse('FilmLocationFromGuidedWithSerial_list')
