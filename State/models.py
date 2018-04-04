from django.db import models
from django.conf import settings
from django.urls import reverse


class State(models.Model):
    States = models.CharField(max_length=200)

    def __str__(self):
        return self.States

    def get_absolute_url(self):
        return reverse('State_details', args=[str(self.id)])



# Create States Comments here.


class Comment(models.Model):

    State_Comment = models.CharField(max_length=150, null=False)
    Comment_State = models.ForeignKey(State, null=False,related_name='commentsState', on_delete=models.CASCADE)
    State_Comment_Author = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='CommentssState', on_delete=models.CASCADE)

    # State_Comment_Created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.State_Comment

    def get_absolute_url(self):
        return reverse('State_list')
