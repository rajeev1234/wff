from django.db import models

from django.conf import settings

from django.urls import reverse

# Create your contactmessagess here.


class ContactMessages(models.Model):

    ContactMessages_Address = models.CharField(max_length=100,unique=True)
    ContactMessages_Camera_Model = models.CharField(max_length=100)
    ContactMessages_City_State_Country = models.CharField(max_length=100)
    ContactMessages_Company_Name = models.CharField(max_length=100)
    ContactMessages_Email = models.EmailField(max_length=100)
    ContactMessages_From_Page = models.CharField(max_length=100)
    ContactMessages_From_Resource = models.CharField(max_length=100)
    ContactMessages_Full_Name = models.CharField(max_length=100)
    ContactMessages_Message = models.CharField(max_length=100)
    ContactMessages_Phone_Number = models.IntegerField(default=-1)
    ContactMessages_Profile =  models.CharField(max_length=100)
    #creator = models.ForeignKey(User, related_name='contactmessages', on_delete=models.CASCADE)
    ContactMessages_Modified_Date = models.DateTimeField(auto_now_add=True)
    ContactMessages_Created_Date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ContactMessages_Address

    def get_absolute_url(self):
        return reverse('contactmessages_details', args=[str(self.id)])


# Create contactmessagess Comments here.


class Comment(models.Model):

    ContactMessages_Comment = models.CharField(max_length=150, null=False)
    Comment_ContactMessages = models.ForeignKey(ContactMessages, null=False,related_name="Comment_ContactMessages", on_delete=models.CASCADE)
    ContactMessages_Comment_Author = models.ForeignKey(settings.AUTH_USER_MODEL,related_name="contactmessages", on_delete=models.CASCADE)

    # contactmessages_Comment_Created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ContactMessages_Comment

    def get_absolute_url(self):
        return reverse('contactmessages_list')

