from django.test import TestCase,SimpleTestCase
from django.urls import reverse,reverse_lazy
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils import timezone
from Client.models import Client



#  Test Class for Client Application

class ClientTest(TestCase):

########################## Model Testing ############################
  

    # Client object with dummy data 
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password = 'test'
        )

        self.Client =  Client.objects.create(# Fields according to defined in Model    
Client_Contact_Person='Client_Contact_Person',
Client_Contact_Person_Designation='Client_Contact_Person_Designation',
Client_Contact_Person_Email='Client_Contact_Person_Email',
Client_Contact_Person_Number='Client_Contact_Person_Number',
Client_Production_House_City_Address='Client_Production_House_City_Address',
Client_Production_House_Name='Client_Production_House_Name',
Client_Production_House_Street_Addrerss='Client_Production_House_Street_Addrerss',
        )

#
    #Check redirection URL
    def test_get_absolute_url(self):
        # Redirection goes to Client details
        self.assertEquals(self.Client.get_absolute_url(), '/client/1')

# #-----------------------------------------------------------------------------------------#

#     # Check Conent of Client object
    def test_Client_content(self):
        self.assertEqual(str(self.Client.Client_Contact_Person),'Client_Contact_Person')
        self.assertEqual(str(self.Client.Client_Contact_Person_Designation), 'Client_Contact_Person_Designation')
        self.assertEqual(str(self.Client.Client_Contact_Person_Email), 'Client_Contact_Person_Email')
        self.assertEqual(str(self.Client.Client_Contact_Person_Number), 'Client_Contact_Person_Number')
        self.assertEqual(str(self.Client.Client_Production_House_City_Address), 'Client_Production_House_City_Address')
        self.assertEqual(str(self.Client.Client_Production_House_Name), 'Client_Production_House_Name')
        self.assertEqual(str(self.Client.Client_Production_House_Street_Addrerss), 'Client_Production_House_Street_Addrerss')

# # #############################   Model Test End   ###########################################







# ###############################    Views Test       ########################################

    
#     # Test Client List View
    
    def test_ClientList_view(self):
        # Get respomse from defined URL namespace
        response = self.client.get(reverse('client_list'))
        self.assertEqual(response.status_code, 200)

        # Check Content of List View
        #self.assertContains(response,self.user.username)
        # Check for Correct template used in template/Clients
        self.assertTemplateUsed(response, 'client/client_list.html')

# #--------------------------------------------------------------------------------------------#
    

#     # Test Client Detail View

    def test_ClientDetail_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test')
        
        # Find primary key of table
        Client_pk = Client.objects.get(Client_Contact_Person='Client_Contact_Person').pk
        
        # Get response
        response = self.client.get(reverse_lazy('client_details',kwargs={'pk':Client_pk}))

        # Check for any invalid value
        no_response = self.client.get(reverse_lazy('client_details',kwargs={'pk':10000}))

        # 202 for valid and 404 for invalid
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)

        # check for content of Detail Page
        self.assertContains(response, 'Client_Contact_Person')
        self.assertContains(response, 'Client_Contact_Person_Designation')
        self.assertContains(response, 'Client_Contact_Person_Email')
        self.assertContains(response, 'Client_Contact_Person_Number')
        self.assertContains(response, 'Client_Production_House_City_Address')
        self.assertContains(response, 'Client_Production_House_Name')
        self.assertContains(response, 'Client_Production_House_Street_Addrerss')

        # Check for Correct template used in template/Clients
        self.assertTemplateUsed(response, 'client/client_detail.html')

# #-------------------------------------------------------------------------------------------#    


#     # Test Client Create View
    
    def test_ClientCreate_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test') 

        # Generate response after creating an view using Http post method
        response = self.client.post('/client/new/',{
'Client_Contact_Person':'Client_Contact_Person',
'Client_Contact_Person_Designation':'Client_Contact_Person_Designation',
'Client_Contact_Person_Email':'Client_Contact_Person_Email',
'Client_Contact_Person_Number':'Client_Contact_Person_Number',
'Client_Production_House_City_Address':'Client_Production_House_City_Address',
'Client_Production_House_Name':'Client_Production_House_Name',
'Client_Production_House_Street_Addrerss':'lient_Production_House_Street_Addrerss',
        })

        # Check for successful response
        self.assertEqual(response.status_code, 200)

        # Check response values
        self.assertContains(response, 'Client_Contact_Person')
        self.assertContains(response, 'Client_Contact_Person_Designation')
        self.assertContains(response, 'Client_Contact_Person_Email')
        self.assertContains(response, 'Client_Contact_Person_Number')
        self.assertContains(response, 'Client_Production_House_City_Address')
        self.assertContains(response, 'Client_Production_House_Name')
        self.assertContains(response, 'Client_Production_House_City_Address')
         # Same as defined in SetUp
         # Same as defined in SetUp

        # Check for correct template used in template/Clients
        self.assertTemplateUsed(response, 'client/client_new.html')

# #---------------------------------------------------------------------------------------#


#     # Test Client Update view 

    def test_Clientupdate_view(self):
        # Login the user
        self.client.login(username='testuser', password='test')
        
        # Find primary key of table
        Client_pk = Client.objects.get(Client_Contact_Person='Client_Contact_Person').pk
        
        # Get response using pk on details view
        response = self.client.get(reverse_lazy('client_details',kwargs={'pk':Client_pk}), {
'Client_Contact_Person':'Client_Contact_Person',
'Client_Contact_Person_Designation':'Client_Contact_Person_Designation',
'Client_Contact_Person_Email':'Client_Contact_Person_Email',
'Client_Contact_Person_Number':'Client_Contact_Person_Number',
'Client_Production_House_City_Address':'Client_Production_House_City_Address',
'Client_Production_House_Name':'Client_Production_House_Name',
'Client_Production_House_Street_Addrerss':'lient_Production_House_Street_Addrerss',
        })
        # Check for successful response
        self.assertEqual(response.status_code, 200)
