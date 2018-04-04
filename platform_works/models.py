from django.db import models

from django.conf import settings

from django.urls import reverse

# Create your platform_workss here.


class PlatformWorks(models.Model):
    # PlatformWorks_Client_Icon = models.ImageField(max_length=200)
    PlatformWorks_Client_Name = models.CharField(max_length=200)
    # PlatformWorks_Location_Manager = models.ForeignKey(User_Details, on_delete=models.CASCADE)
    PlatformWorks_Project_Name = models.CharField(max_length=200)
    PlatformWorks_Project_Details = models.CharField(max_length=200)
    # Project_Image = models.ImageField()

    # PlatformWorks_Message = models.CharField(max_length=280)
    PlatformWorks_Author = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='platform_works', on_delete=models.CASCADE)
    PlatformWorks_Created_Date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.PlatformWorks_Project_Name

    def get_absolute_url(self):
        return reverse('platform_works_details', args=[str(self.id)])


# Create platform_workss Comments here.


class Comment(models.Model):

    platform_works_Comment = models.CharField(max_length=150, null=False)
    # Comment_platform_works = models.ForeignKey(platform_works, null=False, on_delete=models.CASCADE)
    platform_works_Comment_Author = models.ForeignKey(PlatformWorks, on_delete=models.CASCADE)

    # platform_works_Comment_Created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.platform_works_Comment

    def get_absolute_url(self):
        return reverse('platform_works_list')
