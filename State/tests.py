from django.test import TestCase,SimpleTestCase
from django.urls import reverse,reverse_lazy
from .models import State
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.core.files.uploadedfile import SimpleUploadedFile


#  Test Class for State Application

class StateTest(TestCase):

########################## Model Testing ############################
  

    # State object with dummy data 
    def setUp(self):

        # dummy user for login 
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password = 'test'
        )

        self.State =  State.objects.create(

        # Fields according to defined in Model    
        States = 'New State',
        )

#-----------------------------------------------------------------------------------------#

    # Check redirection URL
    def test_get_absolute_url(self):
        # Redirection goes to State details
        self.assertEquals(self.State.get_absolute_url(), '/states/1')

#-----------------------------------------------------------------------------------------#

    # Check Conent of State object created by create object query set
    def test_State_content(self):
        # Verify for each field  
        self.assertEqual(f'{self.State.States}', 'New State')
#--------------------------------------------------------------------------------------------#

# #############################   Model Test End   ###########################################







# ###############################    Views Test       ########################################

    
    # Test State List View
    
    def test_StateList_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test')

        # Get respomse from defined URL namespace
        response = self.client.get(reverse('State_list'))
        self.assertEqual(response.status_code, 200)

        # Check Content of List View
        self.assertContains(response,self.user.username)
        # Check for Correct template used in template/States
        self.assertTemplateUsed(response, 'States/State_list.html')

#--------------------------------------------------------------------------------------------#
    

    # Test State Detail View

    def test_StateDetail_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test')
        
        # Find primary key of table
        State_pk = State.objects.get(States='New State').pk
        
        # Get response
        response = self.client.get(reverse_lazy('State_details',kwargs={'pk':State_pk}))

        # Check for any invalid value
        no_response = self.client.get(reverse_lazy('State_details',kwargs={'pk':10000}))

        # 202 for valid and 404 for invalid
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)

        # check for content of Detail Page
        self.assertContains(response,self.user.username)

        # Check for Correct template used in template/States
        self.assertTemplateUsed(response, 'States/State_details.html')

#-------------------------------------------------------------------------------------------#    


    # Test State Create View
    
    def test_StateCreate_view(self):
        # Login the user defined in SetUps
        self.client.login(username='testuser', password='test') 

        # Generate response after creating an view using Http post method
        response = self.client.post('/states/new/', {
        'States' : 'New State',
        },follow = True)

        # print(response.content)
        # Check for successful response
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'New State')

        # # Check for correct template used in template/States
        # self.assertTemplateUsed(response, 'State/State_details.html')

#---------------------------------------------------------------------------------------#


    # Test State Update view 

    def test_Stateupdate_view(self):
        # Login the user
        self.client.login(username='testuser', password='test')
        
        # Find primary key of table
        State_pk = State.objects.get(States='New State').pk
        
        # Get response using pk on details view
        response = self.client.get(reverse_lazy('State_details',kwargs={'pk':State_pk}), {
        'States' : 'New State',
        })
        # Check for successful response
        self.assertEqual(response.status_code, 200)

        # Check for correct templates
        self.assertTemplateUsed(response,'States/State_details.html')


#--------------------------------------------------------------------------------------------#


# Test Delete View of State views

    def test_Statedelete_view(self):
        # Login the user
        self.client.login(username='testuser', password='test')

        #Find primary key of table
        State_pk = State.objects.get(States='New State').pk
        
        # Get response to delete 

        response = self.client.get(reverse_lazy('State_delete',kwargs={'pk':State_pk}))
        # self.assertContains(response, 'Are you sure you want to delete') # THIS PART WORKS

        # Check deleted value , returns false i.e.302
        post_response = self.client.post(reverse_lazy('State_delete',kwargs={'pk':State_pk}))
        
        # self.assertRedirects(post_response, reverse_lazy('State_delete',kwargs={'pk':State_pk}), status_code=302)


        self.assertEqual(response.status_code, 200)

        # check for Correct Template Used
        self.assertTemplateUsed(response, 'States/State_delete.html')




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
#         response = self.client.get('/States/1/')

#         self.assertEqual(response.status_code, 200)


#------------------------------------------------------------------------------------------------------#
    
        
#     # def test_update_page_status_code(self):
#     #     # url = reverse('StateListView')
#     #     response = self.client.get('/States/1/')
#     #     self.assertEqual(response.status_code, 200)

#-------------------------------------------------------------------------------------------------------#

#     # def test_detail_page_status_code(self):
#     #     response = self.client.get('/{1}/')
#     #     self.assertEqual(response.status_code, 200)

#-------------------------------------------------------------------------------------------------------#

#     # def test_delete_page_status_code(self):
#     #     response = self.client.get('/{1}/delete/')
#     #     self.assertEqual(response.status_code, 200)