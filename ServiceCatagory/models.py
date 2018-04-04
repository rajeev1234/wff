from django.db import models
from django.conf import settings
from django.urls import reverse


class ServiceCatagory(models.Model):
    ServiceCatagory_Icon_Number = models.IntegerField()
    ServiceCatagory_Image = models.ImageField(null=True,blank=True)
    ServiceCatagory_Responsibilities = models.CharField(max_length=200)
    ServiceCatagory_Service_Category = models.CharField(max_length=200)
    # ServiceCatagory_Service_Subcategory = models.ForeignKey(List_Of_Service_Subcategories, on_delete=models.CASCADE)
    ServiceCatagory_Users = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ServiceCatagory_What_Do_You_Do = models.CharField(max_length=200)
    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse('ServiceCatagory_details', args=[str(self.id)])



# Create ServiceCatagorys Comments here.


class Comment(models.Model):

    ServiceCatagory_Comment = models.CharField(max_length=150, null=False)
    Comment_ServiceCatagory = models.ForeignKey(ServiceCatagory, null=False,related_name='commentsServiceCatagory', on_delete=models.CASCADE)
    ServiceCatagory_Comment_Author = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='CommentssServiceCatagory', on_delete=models.CASCADE)

    # ServiceCatagory_Comment_Created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ServiceCatagory_Comment

    def get_absolute_url(self):
        return reverse('ServiceCatagory_list')
