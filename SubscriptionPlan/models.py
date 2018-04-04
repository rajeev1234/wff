from django.db import models
from django.conf import settings
from django.urls import reverse


class SubscriptionPlan(models.Model):
    SubscriptionPlan_Amount = models.IntegerField()
    SubscriptionPlan_End_Date = models.DateField()
    SubscriptionPlan_FOR_FILM_COIN = models.IntegerField()
    SubscriptionPlan_Location_Allowed = models.BooleanField()
    SubscriptionPlan_Openings_Allowed = models.BooleanField()
    SubscriptionPlan_Pitch_Allowed = models.BooleanField()
    SubscriptionPlan_Pitch_Box_Capacity_Image_per_pitch = models.IntegerField()
    SubscriptionPlan_Start_Date = models.DateField(auto_now_add=True,editable=False)
    SubscriptionPlan_Type = models.CharField(max_length=200)
    SubscriptionPlan_User_ID = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse('SubscriptionPlan_details', args=[str(self.id)])



# Create SubscriptionPlan Comments here.


class Comment(models.Model):
    SubscriptionPlan_Comment = models.CharField(max_length=150, null=False)
    Comment_SubscriptionPlan = models.ForeignKey(SubscriptionPlan, null=False,related_name='commentsSubscriptionPlan', on_delete=models.CASCADE)
    SubscriptionPlan_Comment_Author = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='CommentssSubscriptionPlan', on_delete=models.CASCADE)
    SubscriptionPlan_Comment_Created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.SubscriptionPlan_Comment

    def get_absolute_url(self):
        return reverse('SubscriptionPlan_list')
