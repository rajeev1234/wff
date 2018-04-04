from django.db import models
from django.conf import settings
from django.urls import reverse


class Singer(models.Model):
    # Singer_Comments= models.ForeignKey(Comments, on_delete=models.CASCADE)
    Singer_Daily_Charges = models.IntegerField()
    Singer_Description = models.CharField(max_length=200)
    Singer_Financials_Available = models.BooleanField(max_length=200)
    Singer_Genre = models.CharField(max_length=200)
    # Singer_Languages= models.ForeignKey(List_Of_Texts, on_delete=models.CASCADE)
    # Singer_Portfolio= models.ForeignKey(List_Of_Portfolio_Elements, on_delete=models.CASCADE)
    # Singer_Profile_Projects= models.ForeignKey(List_Of_projects, on_delete=models.CASCADE)
    # Singer_Ratings= models.ForeignKey(List_Of_Ratings, on_delete=models.CASCADE)
    # Singer_Scale_Rate = models.CharField(max_length=200)
    
    # Singing_Style = models.ForeignKey(List_Of_Text, on_delete=models.CASCADE)
    # Singer_Video = models.ForeignKey(List_Of_Files, on_delete=models.CASCADE)

    def __str__(self):
        return self.Singer_Description

    def get_absolute_url(self):
        return reverse('Singer_details', args=[str(self.id)])



# Create Singers Comments here.


class Comment(models.Model):

    Singer_Comment = models.CharField(max_length=150, null=False)
    Comment_Singer = models.ForeignKey(Singer, null=False,related_name='commentsSinger', on_delete=models.CASCADE)
    Singer_Comment_Author = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='CommentssSinger', on_delete=models.CASCADE)

    Singer_Comment_Created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Singer_Comment

    def get_absolute_url(self):
        return reverse('Singer_list')
