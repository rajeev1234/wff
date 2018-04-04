from django.test import TestCase,SimpleTestCase
from django.urls import reverse,reverse_lazy
from .models import Conversations
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils import timezone



#  Test Class for Conversations Application

class ConversationsTest(TestCase):

########################## Model Testing ############################
  

    # Conversations object with dummy data 
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password = 'test'
        )

        self.Conversations =  Conversations.objects.create(
Conversations_Message_List="Conversations_Message_List",# Fields according to defined in Model    
        )

#
    #Check redirection URL
    def test_get_absolute_url(self):
        # Redirection goes to Conversations details
        self.assertEquals(self.Conversations.get_absolute_url(), '/conversations/1')

# #-----------------------------------------------------------------------------------------#

#     # Check Conent of Conversations object
    def test_Conversations_content(self):
        self.assertEqual(str(self.Conversations.Conversations_Message_List),'Conversations_Message_List')

# # #--------------------------------------------------------------------------------------------#

# # # #############################   Model Test End   ###########################################







# # ###############################    Views Test       ########################################

    
#     # Test Conversations List View
    
    def test_ConversationsList_view(self):
        # Get respomse from defined URL namespace
        response = self.client.get(reverse('conversations_list'))
        self.assertEqual(response.status_code, 200)

        # Check Content of List View
        #self.assertContains(response,self.user.username)
        # Check for Correct template used in template/Conversationss
        self.assertTemplateUsed(response, 'conversations/conversations_list.html')

# #--------------------------------------------------------------------------------------------#
    

#     # Test Conversations Detail View

    def test_ConversationsDetail_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test')
        
        # Find primary key of table
        Conversations_pk = Conversations.objects.get(Conversations_Message_List='Conversations_Message_List').pk
        
        # Get response
        response = self.client.get(reverse_lazy('conversations_details',kwargs={'pk':Conversations_pk}))

        # Check for any invalid value
        no_response = self.client.get(reverse_lazy('conversations_details',kwargs={'pk':10000}))

        # 202 for valid and 404 for invalid
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)

        # check for content of Detail Page
        self.assertContains(response, 'Conversations_Message_List')

        # Check for Correct template used in template/Conversationss
        self.assertTemplateUsed(response, 'conversations/conversations_detail.html')

# #-------------------------------------------------------------------------------------------#    


#     # Test Conversations Create View
    
    def test_ConversationsCreate_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test') 

        # Generate response after creating an view using Http post method
        response = self.client.post('/conversations/new/',{
        	'Conversations_Message_List':"Conversations_Message_List"
        })

        # Check for successful response
        self.assertEqual(response.status_code, 200)

        # Check response values
        self.assertContains(response, 'Conversations_Message_List')
         # Same as defined in SetUp
         # Same as defined in SetUp

        # Check for correct template used in template/Conversationss
        self.assertTemplateUsed(response, 'conversations/conversations_new.html')

#---------------------------------------------------------------------------------------#


    # Test Conversations Update view 

    def test_Conversationsupdate_view(self):
        # Login the user
        self.client.login(username='testuser', password='test')
        
        # Find primary key of table
        Conversations_pk = Conversations.objects.get(Conversations_Message_List='Conversations_Message_List').pk
        
        # Get response using pk on details view
        response = self.client.get(reverse_lazy('conversations_details',kwargs={'pk':Conversations_pk}), {
        	'Conversations_Message_List':"Conversations_Message_List"})
        # Check for successful response
        self.assertEqual(response.status_code, 200)
