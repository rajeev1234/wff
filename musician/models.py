from django.db import models

from django.conf import settings

from django.urls import reverse

# Create your musicians here.


class Musician(models.Model):
    # Musician_Comments = models.ForeignKey(List_Of_Comments, on_delete=models.CASCADE)
    Musician_Daily_Charges = models.CharField(max_length=200)
    Musician_Description = models.CharField(max_length=500)
    Musician_Financial_Available = models.BooleanField(default=False)
    Musician_Genre = models.CharField(max_length=200)
    # Musician_Instrument = models.ForeignKey(List_Of_Texts, on_delete=models.CASCADE)
    # Musician_ID = models.CharField(max_length=200)
    # Musician_Description_Portfolio = models.ForeignKey(List_Of_Portfolio_Elements, on_delete=models.CASCADE)
    # Musician_Description_Profile_Projects = models.ForeignKey(List_Of_Profile_Projects, on_delete=models.CASCADE)
    # Musician_Description_Ratings = models.ForeignKey(List_Of_Ratings, on_delete=models.CASCADE)
    # Musician_Description_Video = models.ForeignKey(List_Of_files, on_delete=models.CASCADE)


    # musician_Message = models.CharField(max_length=280)
    Musician_Author = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='musician', on_delete=models.CASCADE)
    Musician_Created_Date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Musician_Description

    def get_absolute_url(self):
        return reverse('musician_details', args=[str(self.id)])


# Create musicians Comments here.


class Comment(models.Model):

    musician_Comment = models.CharField(max_length=150, null=False)
    # Comment_musician = models.ForeignKey(musician, null=False, on_delete=models.CASCADE)
    musician_Comment_Author = models.ForeignKey(Musician, on_delete=models.CASCADE)

    # musician_Comment_Created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.musician_Comment

    def get_absolute_url(self):
        return reverse('musician_list')
