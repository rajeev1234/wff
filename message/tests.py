from django.test import TestCase,SimpleTestCase
from django.urls import reverse,reverse_lazy
from .models import Messages
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.forms.models import model_to_dict


#  Test Class for Costume Application

class MessagesTest(TestCase):

########################## Model Testing ############################


    # Costume object with dummy data
    def setUp(self):
        # User for login
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password = 'test'
        )

        self.Messages =  Messages.objects.create(

        # Fields according to defined in Model
        Messages_Subject = 'Messages_Subject', #Defined above in get_user_model
        Messages_Message = 'Messages_Message',
        Messages_Author = self.user,
        Messages_Created_Date = timezone.now(),
        )

#-----------------------------------------------------------------------------------------#

    # Check redirection URL
    def test_get_absolute_url(self):
        # Redirection goes to costume details
        self.assertEquals(self.Messages.get_absolute_url(), '/message/1')

#-----------------------------------------------------------------------------------------#

    # Check Conent of costume object created by create object query set
    def test_Messages_content(self):
        # Verify for each field
        self.assertEqual(f'{self.Messages.Messages_Subject}', 'Messages_Subject')
        self.assertEqual(f'{self.Messages.Messages_Message}', 'Messages_Message')
        self.assertEqual(f'{self.Messages.Messages_Author}', self.user.username)   #Defined in SetUp

#--------------------------------------------------------------------------------------------#

# #############################   Model Test End   ###########################################







# ###############################    Views Test       ########################################


    # Test Costume List View

    def test_MessagesList_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test')

        # Get respomse from defined URL namespace
        response = self.client.get(reverse('messages_list'))
        self.assertEqual(response.status_code, 200)

        # Check Content of List View
        self.assertContains(response,self.user.username)
        # Check for Correct template used in template/Costumes
        self.assertTemplateUsed(response, 'messages/messages_list.html')

#--------------------------------------------------------------------------------------------#


    # Test LocationFinancial Detail View

    def test_MessagesDetail_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test')

        # Find primary key of table
        Messages_pk = Messages.objects.get(Messages_Subject = 'Messages_Subject').pk

        # Get response
        response = self.client.get(reverse_lazy('messages_details',kwargs={'pk':Messages_pk}))

        # Check for any invalid value
        no_response = self.client.get(reverse_lazy('messages_details',kwargs={'pk':10000}))

        # 202 for valid and 404 for invalid
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)

        # check for content of Detail Page
        self.assertContains(response, 'Messages_Subject')

        # Check for Correct template used in template/LocationFinancials
        self.assertTemplateUsed(response, 'messages/messages_detail.html')

#-------------------------------------------------------------------------------------------#


    # Test Costume Create View

    def test_MessagesCreate_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test')

        # Generate response after creating an view using Http post method
        response = self.client.post('/message/new/', {
        'Messages_Subject':'Messages_Subject',
        'Messages_Message':'Messages_Message',
        'Messages_Author':self.user,       #defined in setup
        'Messages_Created_Date':timezone.now(),
        },follow = True)

        # Check for successful response
        self.assertEqual(response.status_code, 200)

        # Check response values
        self.assertContains(response, 'Messages_Subject')
        self.assertContains(response, 'Messages_Message')
        self.assertContains(response, self.user.username)    # Same as defined in SetUp

        # Check for correct template used in template/message
        self.assertTemplateUsed(response, 'messages/messages_detail.html')

#---------------------------------------------------------------------------------------#


    # Test Messages_Subject Update view

    def test_Messagesupdate_view(self):
        # Login the user
        self.client.login(username='testuser', password='test')

        # Find primary key of table
        Messages_pk = Messages.objects.get(Messages_Subject='Messages_Subject').pk

        # Get response using pk on details view
        response = self.client.get(reverse_lazy('messages_details',kwargs={'pk':Messages_pk}), {
        'Messages_Subject':'Messages_Subject',   #defined in setup
        'Messages_Message':'Messages_Message',
        'Messages_Author':self.user,
        'Messages_Created_Date':timezone.now(),
        },follow = True)
        #Check for successful response
        self.assertEqual(response.status_code, 200)

        # Check for correct templates
        self.assertTemplateUsed(response,'messages/messages_detail.html')


#--------------------------------------------------------------------------------------------#


# Test Delete View of message views

    def test_Messagesdelete_view(self):
        # Login the user
        self.client.login(username='testuser', password='test')

        # Find primary key of table
        Messages_pk = Messages.objects.get(Messages_Subject='Messages_Subject').pk

        # Get response to delete

        response = self.client.get(reverse_lazy('messages_delete',kwargs={'pk':Messages_pk}))
        self.assertContains(response, 'Are you sure you want to delete') # THIS PART WORKS

        # Check deleted value , returns false i.e.302
        post_response = self.client.post(reverse_lazy('messages_delete',kwargs={'pk':Messages_pk}))

        # self.assertRedirects(post_response, reverse_lazy('Costume_delete',kwargs={'pk':Costume_pk}), status_code=302)


        self.assertEqual(response.status_code, 200)

        # check for Correct Template Used
        self.assertTemplateUsed(response, 'messages/messages_delete.html')




# ################################     View Testing End   #################################################



# ################################     Testing the URLs       ##############################################

class PagesTests(SimpleTestCase):

    # Check URL for list/ Home
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

# #-----------------------------------------------------------------------------------------------------#

#     # URL for new
#     def test_new_page_status_code(self):
#         # Login the user defined in SetUp
#         # self.client.login(username='testuser', password='test')

#         # Get response
#         response = self.client.get('/costumes/1/')

#         self.assertEqual(response.status_code, 200)


#------------------------------------------------------------------------------------------------------#


#     # def test_update_page_status_code(self):
#     #     # url = reverse('CostumeListView')
#     #     response = self.client.get('/costumes/1/')
#     #     self.assertEqual(response.status_code, 200)

#-------------------------------------------------------------------------------------------------------#

#     # def test_detail_page_status_code(self):
#     #     response = self.client.get('/{1}/')
#     #     self.assertEqual(response.status_code, 200)

#-------------------------------------------------------------------------------------------------------#

#     # def test_delete_page_status_code(self):
#     #     response = self.client.get('/{1}/delete/')
#     #     self.assertEqual(response.status_code, 200)
