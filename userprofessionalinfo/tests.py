from django.test import TestCase,SimpleTestCase
from django.urls import reverse,reverse_lazy
from .models import UserProfessionalInfo
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils import timezone



#  Test Class for UserProfessionalInfo Application

class UserProfessionalInfoTest(TestCase):

########################## Model Testing ############################
  

    # UserProfessionalInfo object with dummy data 
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password = 'test'
        )

        self.UserProfessionalInfo =  UserProfessionalInfo.objects.create(# Fields according to defined in Model    
        UserProfessionalInfo_Account_Name='UserProfessionalInfo_Account_Name',
UserProfessionalInfo_Account_Number=125,
UserProfessionalInfo_Bank_Name='UserProfessionalInfo_Bank_Name',
UserProfessionalInfo_Bank_Account='UserProfessionalInfo_Bank_Account',
UserProfessionalInfo_Charges_Negotiation=125,
UserProfessionalInfo_Daily_Charges=125,
UserProfessionalInfo_Expirienced=True,
UserProfessionalInfo_Hometown=125.0,
UserProfessionalInfo_IFSI_CODE='UserProfessionalInfo_IFSI_CODE',
UserProfessionalInfo_Monthly_Charges=125,
UserProfessionalInfo_Rates_Avialability=True,
UserProfessionalInfo_User_Proffessional_Category='UserProfessionalInfo_User_Proffessional_Category',
UserProfessionalInfo_Weekly_Charges=125,
UserProfessionalInfo_Writtable_Language='UserProfessionalInfo_Writtable_Language',
UserProfessionalInfo_Years_Of_Experience=125
        )

#
    #Check redirection URL
    def test_get_absolute_url(self):
        # Redirection goes to UserProfessionalInfo details
        self.assertEquals(self.UserProfessionalInfo.get_absolute_url(), '/userprofessionalinfo/1')

# #-----------------------------------------------------------------------------------------#

#     # Check Conent of UserProfessionalInfo object
    def test_UserProfessionalInfo_content(self):
        self.assertEqual(str(self.UserProfessionalInfo.UserProfessionalInfo_Account_Name),'UserProfessionalInfo_Account_Name')
        self.assertEqual(int(str(self.UserProfessionalInfo.UserProfessionalInfo_Account_Number)),125)
        self.assertEqual(str(self.UserProfessionalInfo.UserProfessionalInfo_Bank_Name), 'UserProfessionalInfo_Bank_Name')
        self.assertEqual(str(self.UserProfessionalInfo.UserProfessionalInfo_Bank_Account), 'UserProfessionalInfo_Bank_Account')
        self.assertEqual(int(str(self.UserProfessionalInfo.UserProfessionalInfo_Charges_Negotiation)),125)
        self.assertEqual(int(str(self.UserProfessionalInfo.UserProfessionalInfo_Daily_Charges)),125)
        self.assertEqual(bool(str(self.UserProfessionalInfo.UserProfessionalInfo_Expirienced)),True)
        self.assertEqual(float(str(self.UserProfessionalInfo.UserProfessionalInfo_Hometown)),125.0)
        self.assertEqual(str(self.UserProfessionalInfo.UserProfessionalInfo_IFSI_CODE),'UserProfessionalInfo_IFSI_CODE')
        self.assertEqual(int(str(self.UserProfessionalInfo.UserProfessionalInfo_Monthly_Charges)),125)
        self.assertEqual(bool(str(self.UserProfessionalInfo.UserProfessionalInfo_Rates_Avialability)),True) # Defined in SetUp
        self.assertEqual(str(self.UserProfessionalInfo.UserProfessionalInfo_User_Proffessional_Category),'UserProfessionalInfo_User_Proffessional_Category')
        self.assertEqual(int(str(self.UserProfessionalInfo.UserProfessionalInfo_Weekly_Charges)),125)
        self.assertEqual(str(self.UserProfessionalInfo.UserProfessionalInfo_Writtable_Language),'UserProfessionalInfo_Writtable_Language') # Defined in SetUp
        self.assertEqual(int(str(self.UserProfessionalInfo.UserProfessionalInfo_Years_Of_Experience)),125)
# # #--------------------------------------------------------------------------------------------#

# # # #############################   Model Test End   ###########################################







# # ###############################    Views Test       ########################################

    
#     # Test UserProfessionalInfo List View
    
    def test_UserProfessionalInfoList_view(self):
        # Get respomse from defined URL namespace
        response = self.client.get(reverse('userprofessionalinfo_list'))
        self.assertEqual(response.status_code, 200)

        # Check Content of List View
        #self.assertContains(response,self.user.username)
        # Check for Correct template used in template/UserProfessionalInfos
        self.assertTemplateUsed(response, 'userprofessionalinfo/userprofessionalinfo_list.html')

# #--------------------------------------------------------------------------------------------#
    

#     # Test UserProfessionalInfo Detail View

    def test_UserProfessionalInfoDetail_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test')
        
        # Find primary key of table
        UserProfessionalInfo_pk = UserProfessionalInfo.objects.get(UserProfessionalInfo_Account_Name='UserProfessionalInfo_Account_Name').pk
        
        # Get response
        response = self.client.get(reverse_lazy('userprofessionalinfo_details',kwargs={'pk':UserProfessionalInfo_pk}))

        # Check for any invalid value
        no_response = self.client.get(reverse_lazy('userprofessionalinfo_details',kwargs={'pk':10000}))

        # 202 for valid and 404 for invalid
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)

        # check for content of Detail Page
        self.assertContains(response, 'UserProfessionalInfo_Account_Name')

        # Check for Correct template used in template/UserProfessionalInfos
        self.assertTemplateUsed(response, 'userprofessionalinfo/userprofessionalinfo_detail.html')

# #-------------------------------------------------------------------------------------------#    


#     # Test UserProfessionalInfo Create View
    
    def test_UserProfessionalInfoCreate_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test') 

        # Generate response after creating an view using Http post method
        response = self.client.post('/userprofessionalinfo/new/',{
        'UserProfessionalInfo_Account_Name':'UserProfessionalInfo_Account_Name',
'UserProfessionalInfo_Account_Number':125,
'UserProfessionalInfo_Bank_Name':'UserProfessionalInfo_Bank_Name',
'UserProfessionalInfo_Bank_Account':'UserProfessionalInfo_Bank_Account',
'UserProfessionalInfo_Charges_Negotiation':125,
'UserProfessionalInfo_Daily_Charges':125,
'UserProfessionalInfo_Expirienced':True,
'UserProfessionalInfo_Hometown':125.0,
'UserProfessionalInfo_IFSI_CODE':'UserProfessionalInfo_IFSI_CODE',
'UserProfessionalInfo_Monthly_Charges':125,
'UserProfessionalInfo_Rates_Avialability':True,
'UserProfessionalInfo_User_Proffessional_Category':'UserProfessionalInfo_User_Proffessional_Category',
'UserProfessionalInfo_Weekly_Charges':125,
'UserProfessionalInfo_Writtable_Language':'UserProfessionalInfo_Writtable_Language',
'UserProfessionalInfo_Years_Of_Experience':125
        })

        # Check for successful response
        self.assertEqual(response.status_code, 200)

        # Check response values
        self.assertContains(response, 'UserProfessionalInfo_Account_Name')
        self.assertContains(response, 125)
        self.assertContains(response, 'UserProfessionalInfo_Bank_Name')
        self.assertContains(response, 'UserProfessionalInfo_Bank_Account')
        self.assertContains(response, 125)
        self.assertContains(response, 125)
        self.assertContains(response, 'checked')
        self.assertContains(response, 125.0)
        self.assertContains(response, 'UserProfessionalInfo_IFSI_CODE')
        self.assertContains(response, 125)
        self.assertContains(response, 'checked')
        self.assertContains(response, 'UserProfessionalInfo_User_Proffessional_Category')
        self.assertContains(response, 125)
        self.assertContains(response, 'UserProfessionalInfo_Writtable_Language')
        self.assertContains(response, 125)
         # Same as defined in SetUp
         # Same as defined in SetUp

        # Check for correct template used in template/UserProfessionalInfos
        self.assertTemplateUsed(response, 'userprofessionalinfo/userprofessionalinfo_new.html')

#---------------------------------------------------------------------------------------#


    # Test UserProfessionalInfo Update view 

    def test_UserProfessionalInfoupdate_view(self):
        # Login the user
        self.client.login(username='testuser', password='test')
        
        # Find primary key of table
        UserProfessionalInfo_pk = UserProfessionalInfo.objects.get(UserProfessionalInfo_Account_Name='UserProfessionalInfo_Account_Name').pk
        
        # Get response using pk on details view
        response = self.client.get(reverse_lazy('userprofessionalinfo_details',kwargs={'pk':UserProfessionalInfo_pk}), {
'UserProfessionalInfo_Account_Name':'UserProfessionalInfo_Account_Name',
'UserProfessionalInfo_Account_Number':125,
'UserProfessionalInfo_Bank_Name':'UserProfessionalInfo_Bank_Name',
'UserProfessionalInfo_Bank_Account':'UserProfessionalInfo_Bank_Account',
'UserProfessionalInfo_Charges_Negotiation':125,
'UserProfessionalInfo_Daily_Charges':125,
'UserProfessionalInfo_Expirienced':True,
'UserProfessionalInfo_Hometown':125.0,
'UserProfessionalInfo_IFSI_CODE':'UserProfessionalInfo_IFSI_CODE',
'UserProfessionalInfo_Monthly_Charges':125,
'UserProfessionalInfo_Rates_Avialability':True,
'UserProfessionalInfo_User_Proffessional_Category':'UserProfessionalInfo_User_Proffessional_Category',
'UserProfessionalInfo_Weekly_Charges':125,
'UserProfessionalInfo_Writtable_Language':'UserProfessionalInfo_Writtable_Language',
'UserProfessionalInfo_Years_Of_Experience':125
        })
        # Check for successful response
        self.assertEqual(response.status_code, 200)
