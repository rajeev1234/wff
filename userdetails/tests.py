from django.test import TestCase,SimpleTestCase
from django.urls import reverse,reverse_lazy
from .models import UserDetails
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils import timezone



#  Test Class for UserDetails Application

class UserDetailsTest(TestCase):

########################## Model Testing ############################
  

    # UserDetails object with dummy data 
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password = 'test'
        )

        self.UserDetails =  UserDetails.objects.create(# Fields according to defined in Model    
        UserDetails_UserDetails_Message='UserDetails_UserDetails_Message',
UserDetails_Address='UserDetails_Address',
UserDetails_City='UserDetails_City',
UserDetails_Completed=True,
UserDetails_Country='UserDetails_Country',
UserDetails_Date_Of_Birth='2018-03-03',
UserDetails_First_Name='UserDetails_First_Name',
UserDetails_Gender='UserDetails_Gender',
UserDetails_Last_Name='UserDetails_Last_Name',
UserDetails_Phone=123,
UserDetails_Pin_Code=201301,
UserDetails_User_Description='UserDetails_User_Description',
UserDetails_User_ID=123,
        )

#
    #Check redirection URL
    def test_get_absolute_url(self):
        # Redirection goes to UserDetails details
        self.assertEquals(self.UserDetails.get_absolute_url(), '/userdetails/1')

# #-----------------------------------------------------------------------------------------#

#     # Check Conent of UserDetails object
    def test_UserDetails_content(self):
        self.assertEqual(str(self.UserDetails.UserDetails_UserDetails_Message),'UserDetails_UserDetails_Message')
        self.assertEqual(str(self.UserDetails.UserDetails_Address), 'UserDetails_Address')
        self.assertEqual(str(self.UserDetails.UserDetails_City), 'UserDetails_City')
        self.assertEqual(bool(str(self.UserDetails.UserDetails_Completed)), True)
        self.assertEqual(str(self.UserDetails.UserDetails_Country), 'UserDetails_Country')
        self.assertEqual(str(self.UserDetails.UserDetails_Date_Of_Birth), '2018-03-03')
        self.assertEqual(str(self.UserDetails.UserDetails_First_Name),'UserDetails_First_Name')
        self.assertEqual(str(self.UserDetails.UserDetails_Gender), 'UserDetails_Gender')
        self.assertEqual(str(self.UserDetails.UserDetails_Last_Name),'UserDetails_Last_Name')
        self.assertEqual(int(str(self.UserDetails.UserDetails_Phone)),123)
        self.assertEqual(int(str(self.UserDetails.UserDetails_Pin_Code)),201301) # Defined in SetUp
        self.assertEqual(str(self.UserDetails.UserDetails_User_Description),'UserDetails_User_Description')
        self.assertEqual(int((self.UserDetails.UserDetails_User_ID)),123)
# #--------------------------------------------------------------------------------------------#

# # #############################   Model Test End   ###########################################







# ###############################    Views Test       ########################################

    
    # Test UserDetails List View
    
    def test_UserDetailsList_view(self):
        # Get respomse from defined URL namespace
        response = self.client.get(reverse('userdetails_list'))
        self.assertEqual(response.status_code, 200)

        # Check Content of List View
        #self.assertContains(response,self.user.username)
        # Check for Correct template used in template/UserDetailss
        self.assertTemplateUsed(response, 'userdetails/userdetails_list.html')

#--------------------------------------------------------------------------------------------#
    

    # Test UserDetails Detail View

    def test_UserDetailsDetail_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test')
        
        # Find primary key of table
        UserDetails_pk = UserDetails.objects.get(UserDetails_UserDetails_Message='UserDetails_UserDetails_Message').pk
        
        # Get response
        response = self.client.get(reverse_lazy('userdetails_details',kwargs={'pk':UserDetails_pk}))

        # Check for any invalid value
        no_response = self.client.get(reverse_lazy('userdetails_details',kwargs={'pk':10000}))

        # 202 for valid and 404 for invalid
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)

        # check for content of Detail Page
        self.assertContains(response, 'UserDetails_UserDetails_Message')

        # Check for Correct template used in template/UserDetailss
        self.assertTemplateUsed(response, 'userdetails/userdetails_detail.html')

#-------------------------------------------------------------------------------------------#    


    # Test UserDetails Create View
    
    def test_UserDetailsCreate_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test') 

        # Generate response after creating an view using Http post method
        response = self.client.post('/userdetails/new/',{
'UserDetails_UserDetails_Message':'UserDetails_UserDetails_Message',
'UserDetails_Address':'UserDetails_Address',
'UserDetails_City':'UserDetails_City',
'UserDetails_Completed':True,
'UserDetails_Country':'UserDetails_Country',
'UserDetails_Date_Of_Birth':'2018-03-03',
'UserDetails_First_Name':'UserDetails_First_Name',
'UserDetails_Gender':'UserDetails_Gender',
'UserDetails_Last_Name':'UserDetails_Last_Name',
'UserDetails_Phone':123,
'UserDetails_Pin_Code':201301,
'UserDetails_User_Description':'UserDetails_User_Description',
'UserDetails_User_ID':123,
        })

        # Check for successful response
        self.assertEqual(response.status_code, 200)

        # Check response values
        self.assertContains(response, 'UserDetails_UserDetails_Message')
        self.assertContains(response, 'UserDetails_Address')
        self.assertContains(response, 'UserDetails_City')
        self.assertContains(response, 'checked')
        self.assertContains(response, 'UserDetails_Country')
        self.assertContains(response, '2018-03-03')
        self.assertContains(response, 'UserDetails_First_Name')
        self.assertContains(response, 'UserDetails_Gender')
        self.assertContains(response, 'UserDetails_Last_Name')
        self.assertContains(response, 123)
        self.assertContains(response, 201301)
        self.assertContains(response, 'UserDetails_User_Description')
        self.assertContains(response, 123)
         # Same as defined in SetUp
         # Same as defined in SetUp

        # Check for correct template used in template/UserDetailss
        self.assertTemplateUsed(response, 'userdetails/userdetails_new.html')

#---------------------------------------------------------------------------------------#


    # Test UserDetails Update view 

    def test_UserDetailsupdate_view(self):
        # Login the user
        self.client.login(username='testuser', password='test')
        
        # Find primary key of table
        UserDetails_pk = UserDetails.objects.get(UserDetails_UserDetails_Message='UserDetails_UserDetails_Message').pk
        
        # Get response using pk on details view
        response = self.client.get(reverse_lazy('userdetails_details',kwargs={'pk':UserDetails_pk}), {
'UserDetails_UserDetails_Message':'UserDetails_UserDetails_Message',
'UserDetails_Address':'UserDetails_Address',
'UserDetails_City':'UserDetails_City',
'UserDetails_Completed':True,
'UserDetails_Country':'UserDetails_Country',
'UserDetails_Date_Of_Birth':'2018-03-03',
'UserDetails_First_Name':'UserDetails_First_Name',
'UserDetails_Gender':'UserDetails_Gender',
'UserDetails_Last_Name':'UserDetails_Last_Name',
'UserDetails_Phone':123,
'UserDetails_Pin_Code':201301,
'UserDetails_User_Description':'UserDetails_User_Description',
'UserDetails_User_ID':123,})
        # Check for successful response
        self.assertEqual(response.status_code, 200)
