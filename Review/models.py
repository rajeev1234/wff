
from django.conf import settings

from django.urls import reverse

# Create your Reviews here.


from django.db import models

class Review(models.Model):
    Review_Rating = models.IntegerField()
    Review_Text = models.CharField(max_length=200)
    Review_Creator = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='Review',on_delete=models.CASCADE,null=True)
    Review_Create_Date = models.DateTimeField(auto_now_add=True)
    Review_Modified_Date = models.DateTimeField(auto_now_add=True)


# Create your models here.

    def __str__(self):
        return self.Review_Rating

    def get_absolute_url(self):
        return reverse('Review_details', args=[str(self.id)])


# Create Reviews Comments here.


class Comment(models.Model):

    Review_Comment = models.CharField(max_length=150, null=False)
    Comment_Review = models.ForeignKey(Review, null=False,related_name='commentReview', on_delete=models.CASCADE)
    Review_Comment_Author = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='AuthorcommentReview', on_delete=models.CASCADE)

    # Review_Comment_Created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Review_Comment_Author

    def get_absolute_url(self):
        return reverse('Review_list')
