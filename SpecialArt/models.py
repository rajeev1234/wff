from django.db import models
from django.conf import settings
from django.urls import reverse

   
class SpecialArt(models.Model):
    SpecialArt_Charges_Available = models.BooleanField(max_length=200)
    # SpecialArt_Comments = models.ForeignKey(List_of_Comments,on_delete=models.CASCADE)
    SpecialArt_Daily_Charges = models.IntegerField()
    SpecialArt_Description = models.CharField(max_length=500)
    # SpecialArt_Portfolio = models.ForeignKey(List_of_Portfolio_Elements,on_delete=models.CASCADE)
    # SpecialArt_Profile_Projects = models.ForeignKey(List_Of_Projects,on_delete=models.CASCADE)
    # SpecialArt_Ratings = models.ForeignKey(List_Of_Ratings,on_delete=models.CASCADE)
    SpecialArt_Special_Art_ID= models.CharField(max_length=200)
    # SpecialArt_Video = models.ForeignKey(List_Of_Fils,on_delete=models.CASCADE)



    def __str__(self):
        return self.SpecialArt_Description

    def get_absolute_url(self):
        return reverse('SpecialArt_details', args=[str(self.id)])



# Create SpecialArts Comments here.


class Comment(models.Model):

    SpecialArt_Comment = models.CharField(max_length=150, null=False)
    Comment_SpecialArt = models.ForeignKey(SpecialArt, null=False,related_name='commentsSpecialArt', on_delete=models.CASCADE)
    SpecialArt_Comment_Author = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='CommentssSpecialArt', on_delete=models.CASCADE)

    # SpecialArt_Comment_Created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.SpecialArt_Comment

    def get_absolute_url(self):
        return reverse('SpecialArt_list')
