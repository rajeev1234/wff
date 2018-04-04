from django.conf import settings

from django.urls import reverse

# Create your childartists here.
from django.db import models

class ChildArtist(models.Model):

    ChildArtist_Body_Type = models.TextField(max_length=100)
    ChildArtist_Child_Artist_Id =  models.CharField(max_length=100,unique=True)
    #comment = models.ForeignKey(comments, related_name='childartists', on_delete=models.CASCADE)
    ChildArtist_Daily_Charges = models.CharField(max_length=100)
    ChildArtist_Date_Of_Birth = models.DateTimeField(auto_now_add=True)
    ChildArtist_Description = models.CharField(max_length=100)
    ChildArtist_Ethnicity = models.TextField(max_length=100)
    ChildArtist_Eye_Color= models.TextField(max_length=100)
    ChildArtist_Financial_Available = models.BooleanField(default=False)
    ChildArtist_Gender = models.CharField(max_length=100)
    ChildArtist_Height = models.CharField(max_length=100)
    #language = models.ForeignKey(languages, related_name='childartists', on_delete=models.CASCADE)
    #portfolio =models.ForeignKey(portfolios, related_name='childartists',on_delete=models.CASCADE)
    #profileproject = models.ForeignKey(profileprojects, related_name='childartists', on_delete=models.CASCADE)
    #rating = models.ForeignKey(ratings, related_name='childartists', on_delete=models.CASCADE)
    ChildArtist_Relation_With_Artist = models.CharField(max_length=100)
    ChildArtist_Skin_Color = models.TextField(max_length=100)
    ChildArtist_Special_Skills = models.TextField(max_length=100)
    #video = models.ForeignKey(videos, related_name='childartists', on_delete=models.CASCADE)
    ChildArtist_Weight = models.CharField(max_length=100)
    #creator = models.ForeignKey(User,related_name='childartists',on_delete=models.CASCADE)
    ChildArtist_Modified_Date = models.DateTimeField(auto_now_add=True)
    ChildArtist_Created_Date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Body_Type

    def get_absolute_url(self):
        return reverse('childartist_details', args=[str(self.id)])


# Create childartists Comments here.


class Comment(models.Model):

    Child_Artist_Comment = models.CharField(max_length=150, null=False)
    Comment_Child_Artist = models.ForeignKey(ChildArtist, null=False,related_name="child",on_delete=models.CASCADE)
    Child_Artist_Comment_Author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="childartists",on_delete=models.CASCADE)

    # childartist_Comment_Created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Child_Artist_Comment

    def get_absolute_url(self):
        return reverse('childartist_list')

