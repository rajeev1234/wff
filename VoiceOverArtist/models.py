from django.db import models

from django.conf import settings

from django.urls import reverse

# Create your voiceoverartists here.


class VoiceOverArtist(models.Model):
    VoiceOverArtist_Voice_Over_Artist=models.CharField(max_length=200)
    VoiceOverArtist_Charges_Available=models.BooleanField(max_length=200)
    #Comments = models.ForeignKey(List__of_Comments,on_delete=models.CASCADE)
    VoiceOverArtist_Daily_Charges = models.IntegerField(default=-1)
    VoiceOverArtist_Description = models.CharField(max_length=200)
    VoiceOverArtist_Language = models.CharField(max_length=200)
    #Portfolio= models.ForeignKey(List_of_Portfolio_Elements,on_delete=models.CASCADE)
    #Profile_projects = models.ForeignKey(List_of_Profile_projects,on_delete=models.CASCADE)
    #Ratings = models.ForeignKey(List_of_Ratings,on_delete=models.CASCADE)
    #Video = models.ForeignKey(List_of_files,on_delete=models.CASCADE)
    VoiceOverArtist_Voice_Over_Artist_ID = models.IntegerField(default=-1)
    VoiceOverArtist_Voice_Scale = models.CharField(max_length=200)
    VoiceOverArtist_Voice_Over_Artist_Message = models.CharField(max_length=280)
    #voiceoverartist_Author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    VoiceOverArtist_Created_Date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.VoiceOverArtist_Voice_Over_Artist_Message

    def get_absolute_url(self):
        return reverse('voiceoverartist_details', args=[str(self.id)])


# Create voiceoverartists Comments here.


class Comment(models.Model):

    VoiceOverArtist_Comment = models.CharField(max_length=150, null=False)
    Comment_VoiceOverArtist = models.ForeignKey(VoiceOverArtist,related_name="voiceoverartist", null=False, on_delete=models.CASCADE)
    VoiceOverArtist_Comment_Author = models.ForeignKey(settings.AUTH_USER_MODEL,related_name="voiceoverartist_Comment", on_delete=models.CASCADE)

    # voiceoverartist_Comment_Created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.VoiceOverArtist_Comment

    def get_absolute_url(self):
        return reverse('voiceoverartist_list')










