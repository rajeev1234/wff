from django.test import TestCase,SimpleTestCase
from django.urls import reverse,reverse_lazy
from .models import ContactMessages
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils import timezone



#  Test Class for ContactMessages Application

class ContactMessagesTest(TestCase):

########################## Model Testing ############################
  

    # ContactMessages object with dummy data 
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password = 'test'
        )

        self.ContactMessages =  ContactMessages.objects.create(# Fields according to defined in Model    
        ContactMessages_Address='ContactMessages_Address',
ContactMessages_Camera_Model='ContactMessages_Camera_Model',
ContactMessages_City_State_Country='ContactMessages_City_State_Country',
ContactMessages_Company_Name='ContactMessages_Company_Name',
ContactMessages_Email='abc@abc.com',
ContactMessages_From_Page='ContactMessages_From_Page',
ContactMessages_From_Resource='ContactMessages_From_Resource',
ContactMessages_Full_Name='ContactMessages_Full_Name',
ContactMessages_Message='ContactMessages_Message',
ContactMessages_Phone_Number=111,
ContactMessages_Profile='ContactMessages_Profile'
        )

#
    #Check redirection URL
    def test_get_absolute_url(self):
        # Redirection goes to ContactMessages details
        self.assertEquals(self.ContactMessages.get_absolute_url(), '/contactmessages/1')

# #-----------------------------------------------------------------------------------------#

#     # Check Conent of ContactMessages object
    def test_ContactMessages_content(self):
        self.assertEqual(str(self.ContactMessages.ContactMessages_Address),'ContactMessages_Address')
        self.assertEqual(str(self.ContactMessages.ContactMessages_Camera_Model), 'ContactMessages_Camera_Model')
        self.assertEqual(str(self.ContactMessages.ContactMessages_City_State_Country), 'ContactMessages_City_State_Country')
        self.assertEqual(str(self.ContactMessages.ContactMessages_Company_Name), 'ContactMessages_Company_Name')
        self.assertEqual(str(self.ContactMessages.ContactMessages_Email), 'abc@abc.com')
        self.assertEqual(str(self.ContactMessages.ContactMessages_From_Page), 'ContactMessages_From_Page')
        self.assertEqual(str(self.ContactMessages.ContactMessages_From_Resource),'ContactMessages_From_Resource')
        self.assertEqual(str(self.ContactMessages.ContactMessages_Full_Name), 'ContactMessages_Full_Name')
        self.assertEqual(str(self.ContactMessages.ContactMessages_Message),'ContactMessages_Message')
        self.assertEqual(int(str(self.ContactMessages.ContactMessages_Phone_Number)),111)
        self.assertEqual(str(self.ContactMessages.ContactMessages_Profile),'ContactMessages_Profile') 
# #--------------------------------------------------------------------------------------------#

# # #############################   Model Test End   ###########################################







# ###############################    Views Test       ########################################

    
    # Test ContactMessages List View
    
    def test_ContactMessagesList_view(self):
        # Get respomse from defined URL namespace
        response = self.client.get(reverse('contactmessages_list'))
        self.assertEqual(response.status_code, 200)

        # Check Content of List View
        #self.assertContains(response,self.user.username)
        # Check for Correct template used in template/ContactMessagess
        self.assertTemplateUsed(response, 'contactmessages/contactmessages_list.html')

#--------------------------------------------------------------------------------------------#
    

    # Test ContactMessages Detail View

    def test_ContactMessagesDetail_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test')
        
        # Find primary key of table
        ContactMessages_pk = ContactMessages.objects.get(ContactMessages_Company_Name='ContactMessages_Company_Name').pk
        
        # Get response
        response = self.client.get(reverse_lazy('contactmessages_details',kwargs={'pk':ContactMessages_pk}))

        # Check for any invalid value
        no_response = self.client.get(reverse_lazy('contactmessages_details',kwargs={'pk':10000}))

        # 202 for valid and 404 for invalid
        # print(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)

        # check for content of Detail Page
        self.assertContains(response, 'ContactMessages_Address')
        self.assertContains(response, 'ContactMessages_Camera_Model')
        self.assertContains(response, 'ContactMessages_City_State_Country')
        self.assertContains(response, 'ContactMessages_Company_Name')
        self.assertContains(response, 'ContactMessages_Email')
        self.assertContains(response, 'ContactMessages_Address')
        self.assertContains(response, 'ContactMessages_From_Page')
        self.assertContains(response, 'ContactMessages_From_Resource')
        self.assertContains(response, 'ContactMessages_Full_Name')
        self.assertContains(response, 'ContactMessages_Message')
        self.assertContains(response, 'ContactMessages_Phone_Number')
        self.assertContains(response, 'ContactMessages_Profile')
        # Check for Correct template used in template/ContactMessagess
        self.assertTemplateUsed(response, 'contactmessages/contactmessages_detail.html')

#-------------------------------------------------------------------------------------------#    


    # Test ContactMessages Create View
    
    def test_ContactMessagesCreate_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test') 

        # Generate response after creating an view using Http post method
        response = self.client.post('/contactmessages/new/',{
'ContactMessages_Address':'ContactMessages_Address',
'ContactMessages_Camera_Model':'ContactMessages_Camera_Model',
'ContactMessages_City_State_Country':'ContactMessages_City_State_Country',
'ContactMessages_Company_Name':'ContactMessages_Company_Name',
'ContactMessages_Email':'abc@abc.com',
'ContactMessages_From_Page':'ContactMessages_From_Page',
'ContactMessages_From_Resource':'ContactMessages_From_Resource',
'ContactMessages_Full_Name':'ContactMessages_Full_Name',
'ContactMessages_Message':'ContactMessages_Message',
'ContactMessages_Phone_Number=':111,
'ContactMessages_Profile':'ContactMessages_Profile'
        })

        # Check for successful response
        self.assertEqual(response.status_code, 200)

        # Check response values
        self.assertContains(response, 'ContactMessages_Address')
        self.assertContains(response, 'ContactMessages_Camera_Model')
        self.assertContains(response, 'ContactMessages_City_State_Country')
        self.assertContains(response, 'ContactMessages_Company_Name')
        self.assertContains(response, 'abc@abc.com')
        self.assertContains(response, 'ContactMessages_From_Page')
        self.assertContains(response, 'ContactMessages_From_Resource')
        self.assertContains(response, 'ContactMessages_Full_Name')
        self.assertContains(response, 'ContactMessages_Message')
        self.assertContains(response, 'ContactMessages_Phone_Number')
        self.assertContains(response, 'ContactMessages_Profile')
         # Same as defined in SetUp
         # Same as defined in SetUp

        # Check for correct template used in template/ContactMessagess
        self.assertTemplateUsed(response, 'contactmessages/contactmessages_new.html')

#---------------------------------------------------------------------------------------#


    # Test ContactMessages Update view 

    def test_ContactMessagesupdate_view(self):
        # Login the user
        self.client.login(username='testuser', password='test')
        
        # Find primary key of table
        ContactMessages_pk = ContactMessages.objects.get(ContactMessages_Address='ContactMessages_Address').pk
        
        # Get response using pk on details view
        response = self.client.get(reverse_lazy('contactmessages_details',kwargs={'pk':ContactMessages_pk}), {
'ContactMessages_Address':'ContactMessages_Address',
'ContactMessages_Camera_Model':'ContactMessages_Camera_Model',
'ContactMessages_City_State_Country':'ContactMessages_City_State_Country',
'ContactMessages_Company_Name':'ContactMessages_Company_Name',
'ContactMessages_Email':'abc@abc.com',
'ContactMessages_From_Page':'ContactMessages_From_Page',
'ContactMessages_From_Resource':'ContactMessages_From_Resource',
'ContactMessages_Full_Name':'ContactMessages_Full_Name',
'ContactMessages_Message':'ContactMessages_Message',
'ContactMessages_Phone_Number=':111,
'ContactMessages_Profile':'ContactMessages_Profile'
        })
        # Check for successful response
        self.assertEqual(response.status_code, 200)
