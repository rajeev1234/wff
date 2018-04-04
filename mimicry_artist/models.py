from django.db import models

from django.conf import settings

from django.urls import reverse

# Create your mimicry_artists here.


class MimicryArtist(models.Model):
    # Comments = models.ForeignKey(List_Of_Comments, on_delete=models.CASCADE)
    MimicryArtist_Daily_Financials = models.CharField(max_length=200)
    MimicryArtist_Description = models.CharField(max_length=500)
    MimicryArtist_Financials_Available = models.BooleanField()
    # MimicryArtist_Language = models.ForeignKey(List_Of_Text, on_delete=models.CASCADE)
    # MimicryArtist_ID = models.CharField(max_length=100)
    # MimicryArtist_Description = models.CharField(max_length=200)
    # MimicryArtist_Portfolio = models.ForeignKey(List_Of_Portfolio_Elements, on_delete=models.CASCADE)
    # MimicryArtist_Portfolio_Projects = models.ForeignKey(List_Of_Profile_Projects, on_delete=models.CASCADE)
    # MimicryArtist_Rating = models.ForeignKey(List_Of_Ratings, on_delete=models.CASCADE)
    # MimicryArtist_Video = models.ForeignKey(List_Of_files, on_delete=models.CASCADE)
    MimicryArtist_Voices = models.CharField(max_length=200)

    # MimicryArtist_Message = models.CharField(max_length=280)
    MimicryArtist_Author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    MimicryArtist_Created_Date = models.DateTimeField(auto_now_add=True,editable=True)

    def __str__(self):
        return self.MimicryArtist_Description

    def get_absolute_url(self):
        return reverse('mimicry_artist_details', args=[str(self.id)])


# Create mimicry_artists Comments here.


class Comment(models.Model):

    mimicry_artist_Comment = models.CharField(max_length=150, null=False)
    Comment_mimicry_artist = models.ForeignKey(MimicryArtist, null=False, on_delete=models.CASCADE)
    # mimicry_artist_Comment_Author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # mimicry_artist_Comment_Created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.mimicry_artist_Comment

    def get_absolute_url(self):
        return reverse('mimicry_artist_list')
