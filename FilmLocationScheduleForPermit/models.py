from django.db import models
from django.conf import settings
from django.urls import reverse



class FilmLocationScheduleForPermit(models.Model):
    FilmLocationScheduleForPermit_Location =  models.CharField(max_length=100)
    # FilmLocationScheduleForPermit_ProjectID= models.ForeignKey()
    FilmLocationScheduleForPermit_SNo = models.CharField(max_length=100)
    # FilmLocationScheduleForPermit_Shooting_Date = models.ForeignKey(shooting_dates,related_name='filmlocationscheduleforpermits', on_delete=models.CASCADE)
    FilmLocationScheduleForPermit_Creator = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='filmlocationscheduleforpermits', on_delete=models.CASCADE)
    FilmLocationScheduleForPermit_Modified_Date = models.DateField(auto_now_add=True,editable=True)
    FilmLocationScheduleForPermit_Created_Date = models.DateField(auto_now_add=True,editable=False)
    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse('FilmLocationScheduleForPermit_details', args=[str(self.id)])



# Create FilmLocationScheduleForPermits Comments here.


class Comment(models.Model):

    FilmLocationScheduleForPermit_Comment = models.CharField(max_length=150, null=False)
    Comment_FilmLocationScheduleForPermit = models.ForeignKey(FilmLocationScheduleForPermit, null=False,related_name='commentsFilmLocationScheduleForPermit', on_delete=models.CASCADE)
    FilmLocationScheduleForPermit_Comment_Author = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='CommentssFilmLocationScheduleForPermit', on_delete=models.CASCADE)

    FilmLocationScheduleForPermit_Comment_Created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.FilmLocationScheduleForPermit_Comment

    def get_absolute_url(self):
        return reverse('FilmLocationScheduleForPermit_list')
