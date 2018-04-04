from django.db import models

from django.conf import settings

from django.urls import reverse

# Create your userdetailss here.


class UserDetails(models.Model):

    UserDetails_UserDetails_Message = models.CharField(max_length=280)
    #userdetails_Author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    UserDetails_Created_Date = models.DateTimeField(auto_now_add=True)
    UserDetails_Address= models.CharField(max_length=200)
    UserDetails_City = models.CharField(max_length=200)
    UserDetails_Completed = models.BooleanField(default=True)
    UserDetails_Country = models.CharField(max_length=200)
    UserDetails_Date_Of_Birth= models.DateField()
    UserDetails_First_Name = models.CharField(max_length=200)
    UserDetails_Gender = models.CharField(max_length=200)
    UserDetails_Last_Name = models.CharField(max_length=200)
    #Location_List = models.ForeignKey(List_OF_Location,on_delete=models.CASCADE)
    #Office_ID = models.ForeignKey(List_Of_Images,on_delete=models.CASCADE)
    UserDetails_Phone = models.IntegerField(default=-1)
    UserDetails_Pin_Code = models.IntegerField(default=-1)
    #Profile_Picture = models.ImageField(upload_to='userdetails/photos/')
    #Ratings = models.ImageField(upload_to='userdetails/photos/')
    #Requirment_userdetailss = models.ForeignKey(Lis_Of_Quicke_Requirements,on_delete=models.CASCADE)
    UserDetails_Street_Address = models.CharField(max_length=200)
    UserDetails_User_Description = models.CharField(max_length=200)
    #User_Email = models.ForeignKey(User,on_delete=models.CASCADE)
    UserDetails_User_ID = models.IntegerField(default=-1)

    def __str__(self):
        return self.UserDetails_UserDetails_Message

    def get_absolute_url(self):
        return reverse('userdetails_details', args=[str(self.id)])


# Create userdetailss Comments here.


class Comment(models.Model):

    UserDetails_Comment = models.CharField(max_length=150, null=False)
    Comment_UserDetails = models.ForeignKey(UserDetails,related_name="userdetails_Comment", null=False, on_delete=models.CASCADE)
    UserDetails_Comment_Author = models.ForeignKey(settings.AUTH_USER_MODEL,related_name
    ="userdetailss", on_delete=models.CASCADE)

    # userdetails_Comment_Created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.UserDetails_Comment

    def get_absolute_url(self):
        return reverse('userdetails_list')
