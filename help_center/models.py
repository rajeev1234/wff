from django.db import models

from django.conf import settings

from django.urls import reverse

# Create your helpcenters here.


class HelpCenter(models.Model):
    #helpcenter = models.ForeignKey(helpcatagorys , related_name='helpcenters', on_delete=models.CASCADE)
    Help_Center_Help_Name = models.CharField(max_length=100)
    Help_Center_Help_Id = models.IntegerField()
    Help_Center_Creator = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='creator',on_delete= models.CASCADE,null=False)
    Help_Center_Modified_Date = models.DateField(auto_now_add=True)
    Help_Center_Created_Date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.Help_Center_Help_Name

    def get_absolute_url(self):
        return reverse('helpcenter_details', args=[str(self.id)])


# Create helpcenters Comments here.


class Comment(models.Model):

    Help_Center_Comment = models.CharField(max_length=150, null=False)
    Comment_Help_Center = models.ForeignKey(HelpCenter, null=False, on_delete=models.CASCADE)
    Help_Center_Comment_Author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='helpcenter_Comment_Author', on_delete=models.CASCADE,null=True)

    # helpcenter_Comment_Created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Help_Center_Comment_Author

    def get_absolute_url(self):
        return reverse('helpcenter_list')
