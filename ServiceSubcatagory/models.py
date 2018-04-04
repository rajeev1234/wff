from django.db import models
from django.conf import settings
from django.urls import reverse


class ServiceSubcatagory(models.Model):
    Service_Subcatagory_Name = models.CharField(max_length=200)
    
    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse('ServiceSubcatagory_details', args=[str(self.id)])



# Create ServiceSubcatagorys Comments here.


class Comment(models.Model):

    ServiceSubcatagory_Comment = models.CharField(max_length=150, null=False)
    Comment_ServiceSubcatagory = models.ForeignKey(ServiceSubcatagory, null=False,related_name='commentsServiceSubcatagory', on_delete=models.CASCADE)
    ServiceSubcatagory_Comment_Author = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='CommentssServiceSubcatagory', on_delete=models.CASCADE)
    ServiceSubcatagory_Comment_Created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ServiceSubcatagory_Comment

    def get_absolute_url(self):
        return reverse('ServiceSubcatagory_list') 
