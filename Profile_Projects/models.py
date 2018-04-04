from django.db import models

from django.conf import settings

from django.urls import reverse

# Create your profile_projectss here.


class profile_projects(models.Model):
    Category=models.CharField(max_length=200)
    Director=models.CharField(max_length=200)
    Production_House = models.CharField(max_length=200)
    Title = models.CharField(max_length=200)


    profile_projects_Message = models.CharField(max_length=280)
    profile_projects_Author = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='profile_projects', on_delete=models.CASCADE)
    Created_Date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.profile_projects_Message

    def get_absolute_url(self):
        return reverse('profile_projects_details', args=[str(self.id)])


# Create profile_projectss Comments here.


class Comment(models.Model):

    profile_projects_Comment = models.CharField(max_length=150, null=False)
    # Comment_profile_projects = models.ForeignKey(profile_projects, null=False, on_delete=models.CASCADE)
    profile_projects_Comment_Author = models.ForeignKey(profile_projects, on_delete=models.CASCADE)

    # profile_projects_Comment_Created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.profile_projects_Comment

    def get_absolute_url(self):
        return reverse('profile_projects_list')
