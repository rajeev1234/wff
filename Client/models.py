# Create your models here.
from django.db import models

from django.conf import settings

from django.urls import reverse

# Create your client here.


class Client(models.Model):
    Client_Contact_Person = models.CharField(max_length=100,unique=True)
    Client_Contact_Person_Designation = models.CharField(max_length=100)
    Client_Contact_Person_Email = models.CharField(max_length=100)
    Client_Contact_Person_Number = models.CharField(max_length=100)
    #previous_work = models.ForeignKey(previous_works, related_name='clients', on_delete=models.CASCADE)
    Client_Production_House_City_Address = models.CharField(max_length=100)
    Client_Production_House_Name = models.CharField(max_length=100)
    Client_Production_House_Street_Addrerss = models.CharField(max_length=100)
    #creator = models.ForeignKey(User, related_name='clients',on_delete=models.CASCADE)
    Client_Modified_Date = models.DateTimeField(auto_now_add=True)
    Client_Created_Date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.Client_Contact_Person

    def get_absolute_url(self):
        return reverse('client_details', args=[str(self.id)])


# Create client Comments here.


class Comment(models.Model):

    Client_Comment = models.CharField(max_length=150, null=False)
    Comment_Client = models.ForeignKey(Client, null=False,related_name="client", on_delete=models.CASCADE)
    Client_Comment_Author = models.ForeignKey(settings.AUTH_USER_MODEL,related_name="client_Comment",on_delete=models.CASCADE)

    # client_Comment_Created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Client_Comment

    def get_absolute_url(self):
        return reverse('client_list')

