from django.db import models

from django.conf import settings

from django.urls import reverse

# Create your userprofessionalinfos here.


class UserProfessionalInfo(models.Model):

	UserProfessionalInfo_Account_Name = models.CharField(max_length=200,unique=True)
	UserProfessionalInfo_Account_Number = models.IntegerField(default=-1)
	UserProfessionalInfo_Bank_Name = models.CharField(max_length=200)
	UserProfessionalInfo_Bank_Account = models.CharField(max_length=200)
	UserProfessionalInfo_Charges_Negotiation = models.IntegerField(default=-1)
	UserProfessionalInfo_Daily_Charges = models.IntegerField(default=-1)
	 #Department = models.ForeignKey(List_Of_Service_Catagories,on_delete=models.CASCADE)
	 #Designation = models.ForeignKey(List_Of_Service_Subcatagorys,on_delete=models.CASCADE)
	UserProfessionalInfo_Expirienced = models.BooleanField(default=True)
	UserProfessionalInfo_Hometown = models.FloatField(max_length=200)
	UserProfessionalInfo_IFSI_CODE = models.CharField(max_length=200)
	UserProfessionalInfo_Monthly_Charges = models.IntegerField(default=-1)
	 #Projects = models.ForeignKey(List_of_Projects,on_delete=models.CASCADE)
	UserProfessionalInfo_Rates_Avialability = models.BooleanField(max_length=200)
	 #Spoken_Languages = models.ForeignKey(List_OF_Texts,on_delete=models.CASCADE)
	 #Understandable_Knowledge = models.ForeignKey(List_OF_Text,on_delete=models.CASCADE)
	 #User_Education = models.ForeignKey(List_OF_Educationinfo,on_delete=models.CASCADE)
	UserProfessionalInfo_User_Proffessional_Category= models.CharField(max_length=200)
	UserProfessionalInfo_Weekly_Charges = models.IntegerField(default=-1)
	UserProfessionalInfo_Writtable_Language= models.CharField(max_length=200)
	UserProfessionalInfo_Years_Of_Experience = models.IntegerField(default=-1)
	def __str__(self):
		return self.UserProfessionalInfo_Account_Name

	def get_absolute_url(self):
		return reverse('userprofessionalinfo_details',args=[str(self.id)])
# Create userprofessionalinfos Comments here.


class Comment(models.Model):

    UserProfessionalInfo_Comment = models.CharField(max_length=150, null=False)
    Comment_UserProfessionalInfo = models.ForeignKey(UserProfessionalInfo,related_name="userprofessionalinfo_details", null=False, on_delete=models.CASCADE)
    #UserProfessionalInfo_Comment_Author = models.ForeignKey(settings.AUTH_USER_MODEL,related_name="userprofessionalinfo_Comment" ,on_delete=models.CASCADE)

    # userprofessionalinfo_Comment_Created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.UserProfessionalInfo_Comment

    def get_absolute_url(self):
        return reverse('userprofessionalinfo_list')




