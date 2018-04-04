from django.db import models

from django.conf import settings

from django.urls import reverse

# Create your messagess here.


class Messages(models.Model):

    Messages_Subject = models.CharField(max_length=900)

    Messages_Message = models.CharField(max_length=280)
    Messages_Author = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='messages', on_delete=models.CASCADE)
    Messages_Created_Date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Messages_Message

    def get_absolute_url(self):
        return reverse('messages_details', args=[str(self.id)])


# Create messagess Comments here.


class Comment(models.Model):

    messages_Comment = models.CharField(max_length=150, null=False)
    # Comment_messages = models.ForeignKey(messages,related_name='comment', null=False, on_delete=models.CASCADE)
    messages_Comment_Author = models.ForeignKey(Messages, related_name='comment', on_delete=models.CASCADE)

    # messages_Comment_Created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.messages_Comment

    def get_absolute_url(self):
        return reverse('messages_list')
