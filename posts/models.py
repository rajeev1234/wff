from django.db import models

from django.conf import settings

from django.urls import reverse

# Create your Posts here.


class Post(models.Model):

    Post_Message = models.CharField(max_length=280)
    Post_Author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    Created_Date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Post_Message

    def get_absolute_url(self):
        return reverse('post_details', args=[str(self.id)])


# Create Posts Comments here.


class Comment(models.Model):

    Post_Comment = models.CharField(max_length=150, null=False)
    Comment_Post = models.ForeignKey(Post, null=False, on_delete=models.CASCADE)
    Post_Comment_Author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # Post_Comment_Created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Post_Comment

    def get_absolute_url(self):
        return reverse('post_list')
