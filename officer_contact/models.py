from django.db import models

from django.conf import settings

from django.urls import reverse

# Create your officer_contacts here.


class OfficerContact(models.Model):
    # OfficerContact_Authority = models.ForeignKey(Location_Authorities, on_delete=models.CASCADE)
    OfficerContact_CONTACT_NUMBER = models.CharField(max_length=200)
    OfficerContact_DEPARTMENT = models.CharField(max_length=200)
    OfficerContact_DESIGNATIONS = models.CharField(max_length=200)
    OfficerContact_E_Mail = models.EmailField(max_length=200)
    OfficerContact_Name = models.CharField(max_length=200)
    # OfficerContact_Officer = models.ForeignKey(District, on_delete=models.CASCADE)

    # OfficerContact_Message = models.CharField(max_length=280)
    OfficerContact_Author = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='officer_contact', on_delete=models.CASCADE)
    OfficerContact_Created_Date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.OfficerContact_Name

    def get_absolute_url(self):
        return reverse('officer_contact_details', args=[str(self.id)])


# Create officer_contacts Comments here.


class Comment(models.Model):

    officer_contact_Comment = models.CharField(max_length=150, null=False)
    # Comment_officer_contact = models.ForeignKey(officer_contact, null=False, on_delete=models.CASCADE)
    officer_contact_Comment_Author = models.ForeignKey(OfficerContact, on_delete=models.CASCADE)

    # officer_contact_Comment_Created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.officer_contact_Comment

    def get_absolute_url(self):
        return reverse('officer_contact_list')
