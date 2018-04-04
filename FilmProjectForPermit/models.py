from django.db import models
from django.conf import settings
from django.urls import reverse


class FilmProjectForPermit(models.Model):
    # FilmProjectForPermit_Cast = models.ForeignKey(casts, related_name='filmprojectforpermits', on_delete=models.CASCADE)
    FilmProjectForPermit_Category = models.CharField(max_length=100)
    # FilmProjectForPermit_Client = models.ForeignKey()
    FilmProjectForPermit_Crew_Size = models.CharField(max_length=100)
    # FilmProjectForPermit_Listoflocation_schedule = models.ForeignKey()
    # FilmProjectForPermit_PermitLocationList = models.ForeignKey(permitlocationlists, related_name='filmprojectforpermits', on_delete=models.CASCADE)
    FilmProjectForPermit_Project_Name = models.CharField(max_length=100)
    FilmProjectForPermit_ScriptasFile = models.FileField()
    FilmProjectForPermit_Synopsis = models.CharField(max_length=100)
    FilmProjectForPermit_Title = models.CharField(max_length=100)
    FilmProjectForPermit_Creator = models.ForeignKey(settings.AUTH_USER_MODEL ,related_name='filmprojectforpermits', on_delete=models.CASCADE)
    FilmProjectForPermit_Modified_Date = models.DateField(auto_now_add=True,editable=True)
    FilmProjectForPermit_Created_Date = models.DateField(auto_now_add=True,editable=False)


    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse('FilmProjectForPermit_details', args=[str(self.id)])



# Create FilmProjectForPermits Comments here.


class Comment(models.Model):

    FilmProjectForPermit_Comment = models.CharField(max_length=150, null=False)
    Comment_FilmProjectForPermit = models.ForeignKey(FilmProjectForPermit, null=False,related_name='commentsFilmProjectForPermit', on_delete=models.CASCADE)
    FilmProjectForPermit_Comment_Author = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='CommentssFilmProjectForPermit', on_delete=models.CASCADE)

    # FilmProjectForPermit_Comment_Created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.FilmProjectForPermit_Comment

    def get_absolute_url(self):
        return reverse('FilmProjectForPermit_list')
