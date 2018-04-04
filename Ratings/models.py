
from django.conf import settings

from django.urls import reverse

# Create your Ratings here.


from django.db import models

class Rating(models.Model):
    Rating = models.IntegerField()
    Rating_User_ID = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='Ratings', on_delete=models.CASCADE,null=True)
    Rating_Creator = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='rate',on_delete=models.CASCADE,null=True)
    Rating_Create_Date = models.DateTimeField(auto_now_add=True)
    Rating_Modified_Date = models.DateTimeField(auto_now_add=True)

# Create your models here.

    def __str__(self):
        return self.Rating_User_ID

    def get_absolute_url(self):
        return reverse('Rating_details', args=[str(self.id)])


# Create Ratings Comments here.


class Comment(models.Model):

    Rating_Comment = models.CharField(max_length=150, null=False)
    Comment_Rating = models.ForeignKey(Rating, null=False,related_name='comment_Ratings', on_delete=models.CASCADE)
    Rating_Comment_Author = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='commentRatings', on_delete=models.CASCADE)

    # Rating_Comment_Created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Rating_Comment_Author

    def get_absolute_url(self):
        return reverse('Ratings_list')
