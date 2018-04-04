from django.db import models
from django.conf import settings
from django.urls import reverse


class EducationInfo(models.Model):
    EducationInfo_Course = models.CharField(max_length=100)
    EducationInfo_Course_Detail = models.CharField(max_length=100)
    EducationInfo_Institute = models.CharField(max_length=100)
    EducationInfo_Passing_Year = models.CharField(max_length=100)
    EducationInfo_Creator = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='educationInfos', on_delete=models.CASCADE)
    EducationInfo_Modified_Date = models.DateField(auto_now_add = True,editable= True)
    EducationInfo_Created_Time = models.DateField(auto_now_add = True,editable=False)
    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse('EducationInfo_details', args=[str(self.id)])



# Create EducationInfos Comments here.


class Comment(models.Model):

    EducationInfo_Comment = models.CharField(max_length=150, null=False)
    Comment_EducationInfo = models.ForeignKey(EducationInfo, null=False,related_name='commentsEducationInfo', on_delete=models.CASCADE)
    EducationInfo_Comment_Author = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='CommentssEducationInfo', on_delete=models.CASCADE)

    # EducationInfo_Comment_Created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.EducationInfo_Comment

    def get_absolute_url(self):
        return reverse('EducationInfo_list')
