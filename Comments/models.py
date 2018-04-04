
from django.db import models

from django.conf import settings

from django.urls import reverse

# Create your commentss here.


class Comments(models.Model):

    Comments_Comment = models.CharField(max_length=100,unique=True)
    #creatorid = models.ForeignKey(User, related_name='commentss', on_delete=models.CASCADE)
    Comments_Helpfull= models.CharField(max_length=100)
    #creator = models.ForeignKey(User, related_name='commentss', on_delete=models.CASCADE)
    Comments_Modified_Date = models.DateTimeField(auto_now_add=True)
    Comments_Created_Date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.Comments_Comment

    def get_absolute_url(self):
        return reverse('comments_details', args=[str(self.id)])


# Create commentss Comments here.


class Comment(models.Model):

    Comments_Comments = models.CharField(max_length=150, null=False)
    Comment_Comments = models.ForeignKey(Comments, null=False,related_name="comments_Comment", on_delete=models.CASCADE)
    Comments_Comment_Author = models.ForeignKey(settings.AUTH_USER_MODEL,related_name="comments", on_delete=models.CASCADE)

    Comments_Comment_Created_On = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Comments_Comments

    def get_absolute_url(self):
        return reverse('comments_list')
