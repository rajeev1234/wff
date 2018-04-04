from django.db import models

from django.conf import settings

from django.urls import reverse

# Create your conversationss here.


class Conversations(models.Model):
    #message_list = models.ForeignKey(message_lists , related_name='conversationss', on_delete=models.CASCADE)
    #recipient = models.ForeignKey(recipients, related_name='conversationss', on_delete=models.CASCADE)
    #creator = models.ForeignKey(User, related_name='conversationss', on_delete=models.CASCADE)
    Conversations_Modified_Date = models.DateTimeField(auto_now_add=True)
    Conversations_Created_Date = models.DateTimeField(auto_now_add=True)
    Conversations_Message_List=models.CharField(max_length=20,blank=True,null=True,unique=True)

    def __str__(self):
        return self.Conversations_Modified_Date

    def get_absolute_url(self):
        return reverse('conversations_details', args=[str(self.id)])


# Create conversationss Comments here.


class Comment(models.Model):

    Conversations_Comment = models.CharField(max_length=150, null=False)
    Comment_Conversations = models.ForeignKey(Conversations, null=False,related_name=
        "comments_conversations",on_delete=models.CASCADE)
    Conversations_Comment_Author = models.ForeignKey(settings.AUTH_USER_MODEL,related_name="conversations", on_delete=models.CASCADE)

    # conversations_Comment_Created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Conversations_Comment

    def get_absolute_url(self):
        return reverse('conversations_list')
