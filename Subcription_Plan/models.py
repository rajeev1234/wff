from django.db import models

from django.conf import settings

from django.urls import reverse

# Create your subcription_plans here.


class subcription_plan(models.Model):
    Amount = models.IntegerField(default=0)
    End_Date = models.DateField(auto_now_add=True)
    FOR_FILM_COIN = models.IntegerField(default=0)
    Location_Allowed = models.IntegerField(default=0)
    Openings_Allowed = models.IntegerField(default=0)
    Pitch_Allowed = models.IntegerField(default=0)
    Pitch_Box_Capacity_Image_per_pitch = models.IntegerField(default=0)
    Start_Date = models.DateField(auto_now_add=True)
    Type = models.CharField(max_length=200)
    # User_ID = models.ForeignKey(User, on_delete=models.CASCADE)

    subcription_plan_Message = models.CharField(max_length=280)
    subcription_plan_Author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='subcription_plan',on_delete=models.CASCADE)
    Created_Date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subcription_plan_Message

    def get_absolute_url(self):
        return reverse('subcription_plan_details', args=[str(self.id)])


# Create subcription_plans Comments here.


class Comment(models.Model):

    subcription_plan_Comment = models.CharField(max_length=150, null=False)
    # Comment_subcription_plan = models.ForeignKey(subcription_plan, null=False, on_delete=models.CASCADE)
    subcription_plan_Comment_Author = models.ForeignKey(subcription_plan, on_delete=models.CASCADE)

    # subcription_plan_Comment_Created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subcription_plan_Comment

    def get_absolute_url(self):
        return reverse('subcription_plan_list')
