from django.db import models
from django.conf import settings
from django.urls import reverse


class FilmRecceRoute(models.Model):
    FilmRecceRoute_Distance = models.CharField(max_length=100)
    # FilmRecceRoute_Film_Location = models.ForeignKey()
    FilmRecceRoute_Filmrecce_Name = models.CharField(max_length=100)
    FilmRecceRoute_Route_Name = models.CharField(max_length=100)
    FilmRecceRoute_Travel_Time = models.CharField(max_length=100)
    FilmRecceRoute_Creator = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='FilmRecceRoutes', on_delete=models.CASCADE)
    FilmRecceRoute_Modified_Date = models.DateField(auto_now_add=True,editable=True)
    FilmRecceRoute_Created_Date = models.DateField(auto_now_add=True,editable=False)
    def __str__(self):
        return self.FilmRecceRoute_Distance

    def get_absolute_url(self):
        return reverse('FilmRecceRoute_details', args=[str(self.id)])



# Create FilmRecceRoutes Comments here.


class Comment(models.Model):

    FilmRecceRoute_Comment = models.CharField(max_length=150, null=False)
    Comment_FilmRecceRoute = models.ForeignKey(FilmRecceRoute, null=False,related_name='commentsFilmRecceRoute', on_delete=models.CASCADE)
    FilmRecceRoute_Comment_Author = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='CommentssFilmRecceRoute', on_delete=models.CASCADE)

    # FilmRecceRoute_Comment_Created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.FilmRecceRoute_Comment

    def get_absolute_url(self):
        return reverse('FilmRecceRoute_list')
