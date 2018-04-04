
from django.conf import settings

from django.urls import reverse

# Create your Quick_Requirementss here.


from django.db import models

class Quick_Requirements(models.Model):
    #Quick_Requirements_Category = models.ForeignKey(List_Of_Quick_Requirementss, on_delete=models.CASCADE)
    Quick_Requirements_Crew_Size = models.IntegerField()
    Quick_Requirements_From_User = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='User_Requirements', on_delete=models.CASCADE,null=True)
    Quick_Requirements_New_Requirement = models.BooleanField()
    #Quick_Requirements_Pitch_List = models.ForeignKey(List_Of_Quick_Requirements_Pitches, on_delete=models.CASCADE)
    Quick_Requirements_Recipient = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='Recipent', on_delete=models.CASCADE,null=True)
    Quick_Requirements_Requirement_Description = models.CharField(max_length=200)
    Quick_Requirements_Shoot_Category = models.CharField(max_length=200)
    Quick_Requirements_Shooting_Region = models.CharField(max_length=200)
    #Quick_Requirements_SUB_CATEGORY = models.ForeignKey(List_Of_Quick_Requirements_Sub_Catagorys, on_delete=models.CASCADE)
    Quick_Requirements_Tentative_Dates = models.DateField(auto_now_add=False,editable=True,null=True)
    Quick_Requirements_Creator = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='Quick_Requirements_Creator',on_delete=models.CASCADE,null=True)
    Quick_Requirements_Created_Date  = models.DateTimeField(auto_now_add=True)
    Quick_Requirements_Modified_Date = models.DateTimeField(auto_now_add=True)


# Create your models here.

    def __str__(self):
        return self.Quick_Requirements_Requirement_Description

    def get_absolute_url(self):
        return reverse('Quick_Requirements_details', args=[str(self.id)])


# Create Quick_Requirementss Comments here.


class Comment(models.Model):

    Quick_Requirements_Comment = models.CharField(max_length=150, null=False)
    Comment_Quick_Requirements = models.ForeignKey(settings.AUTH_USER_MODEL, null=False,related_name='commentQuick_Requirements', on_delete=models.CASCADE)
    Quick_Requirements_Comment_Author = models.ForeignKey(Quick_Requirements,related_name='AuthorQuick_Requirements', on_delete=models.CASCADE)

    # Quick_Requirements_Comment_Created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Quick_Requirements_Comment_Author

    def get_absolute_url(self):
        return reverse('Quick_Requirements_list')
