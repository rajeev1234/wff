from django.db import models
from django.conf import settings
from django.urls import reverse


class TalentProfile(models.Model):
    # TalentProfile_Actor = models.ForeignKey(Actor,on_delete=models.CASCADE)
    # TalentProfile_Child_Artist = models.ForeignKey(Child_Artist,on_delete=models.CASCADE)
    # TalentProfile_Dancer = models.ForeignKey(Dancer,on_delete=models.CASCADE)
    # TalentProfile_Mimicry_Artist= models.ForeignKey(Mimicry_Artist,on_delete=models.CASCADE)
    # TalentProfile_Model=models.ForeignKey(Model,on_delete=models.CASCADE)
    # TalentProfile_Musician = models.ForeignKey(Musician,on_delete=models.CASCADE)
    # TalentProfile_Profile_Talent = models.CharField(max_length=200)
    # TalentProfile_Singer = models.ForeignKey(Singer,on_delete=models.CASCADE)
    # TalentProfile_Special_Art = models.ForeignKey(Special_Art,on_delete=models.CASCADE)
    # TalentProfile_Theater_Artist = models.ForeignKey(Theater_Artist,on_delete=models.CASCADE)
    # TalentProfile_Voice_Over_Artist = models.ForeignKey(Voice_Over_Artist,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse('TalentProfile_details', args=[str(self.id)])



# Create TalentProfile Comments here.


class Comment(models.Model):
    TalentProfile_Comment = models.CharField(max_length=150, null=False)
    Comment_TalentProfile = models.ForeignKey(TalentProfile, null=False,related_name='commentsTalentProfile', on_delete=models.CASCADE)
    TalentProfile_Comment_Author = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='CommentssTalentProfile', on_delete=models.CASCADE)
    TalentProfile_Comment_Created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.TalentProfile_Comment

    def get_absolute_url(self):
        return reverse('TalentProfile_list')
