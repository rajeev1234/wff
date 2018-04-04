from django.db import models

from django.conf import settings

from django.urls import reverse

# Create your circleinvites here.


class CircleInvite(models.Model):
    CircleInvite_Accepted = models.CharField(max_length=100,unique=True)
    #from_ = models.ForeignKey(User, related_name='circleinvites', on_delete=models.CASCADE)
    #to = models.ForeignKey(User, related_name='circleinvites', on_delete=models.CASCADE)
    #Creator = models.ForeignKey(User, related_name='circleinvites', on_delete=models.CASCADE)
    CircleInvite_Modified_Date = models.DateTimeField(auto_now_add=True)
    CircleInvite_Created_Date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Accepted

    def get_absolute_url(self):
        return reverse('circleinvite_details', args=[str(self.id)])


# Create circleinvites Comments here.


class Comment(models.Model):

    CircleInvite_Comment = models.CharField(max_length=150, null=False)
    Comment_CircleInvite = models.ForeignKey(CircleInvite, related_name= "circleinvite_comments",null=False, on_delete=models.CASCADE)
    CircleInvite_Comment_Author = models.ForeignKey(settings.AUTH_USER_MODEL,related_name="circleinvite", on_delete=models.CASCADE)

    # circleinvite_Comment_Created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.CircleInvite_Comment

    def get_absolute_url(self):
        return reverse('circleinvite_list')

