from django.test import TestCase,SimpleTestCase
from django.urls import reverse,reverse_lazy
from .models import CircleInvite
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils import timezone



#  Test Class for CircleInvite Application

class CircleInviteTest(TestCase):

########################## Model Testing ############################
  

    # CircleInvite object with dummy data 
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password = 'test'
        )

        self.CircleInvite =  CircleInvite.objects.create(# Fields according to defined in Model    
        CircleInvite_Accepted='CircleInvite_Accepted',
        )

#
    #Check redirection URL
    def test_get_absolute_url(self):
        # Redirection goes to CircleInvite details
        self.assertEquals(self.CircleInvite.get_absolute_url(), '/circleinvite/1')

# #-----------------------------------------------------------------------------------------#

#     # Check Conent of CircleInvite object
    def test_CircleInvite_content(self):
        self.assertEqual(str(self.CircleInvite.CircleInvite_Accepted),'CircleInvite_Accepted')
# #--------------------------------------------------------------------------------------------#

# # #############################   Model Test End   ###########################################







# ###############################    Views Test       ########################################

    
    # Test CircleInvite List View
    
    def test_CircleInviteList_view(self):
        # Get respomse from defined URL namespace
        response = self.client.get(reverse('circleinvite_list'))
        self.assertEqual(response.status_code, 200)

        # Check Content of List View
        #self.assertContains(response,self.user.username)
        # Check for Correct template used in template/CircleInvites
        self.assertTemplateUsed(response, 'circleinvite/circleinvite_list.html')

#--------------------------------------------------------------------------------------------#
    

    # Test CircleInvite Detail View

    def test_CircleInviteDetail_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test')
        
        # Find primary key of table
        CircleInvite_pk = CircleInvite.objects.get(CircleInvite_Accepted='CircleInvite_Accepted').pk
        
        # Get response
        response = self.client.get(reverse_lazy('circleinvite_details',kwargs={'pk':CircleInvite_pk}))

        # Check for any invalid value
        no_response = self.client.get(reverse_lazy('circleinvite_details',kwargs={'pk':10000}))

        # 202 for valid and 404 for invalid
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)

        # check for content of Detail Page
        print(response.content)
        self.assertContains(response,'CircleInvite_Accepted')

        # Check for Correct template used in template/CircleInvites
        self.assertTemplateUsed(response, 'circleinvite/circleinvite_detail.html')

#-------------------------------------------------------------------------------------------#    


    # Test CircleInvite Create View
    
    def test_CircleInviteCreate_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test') 

        # Generate response after creating an view using Http post method
        response = self.client.post('/circleinvite/new/',{
            'CircleInvite_Accepted':'CircleInvite_Accepted',
        })

        # Check for successful response
        print(response.content)
        self.assertEqual(response.status_code, 200)

        # Check response values
        self.assertContains(response,'CircleInvite_Accepted')
         # Same as defined in SetUp
         # Same as defined in SetUp

        # Check for correct template used in template/CircleInvites
        self.assertTemplateUsed(response,'circleinvite/circleinvite_new.html')

#---------------------------------------------------------------------------------------#


    # Test CircleInvite Update view 

    def test_CircleInviteupdate_view(self):
        # Login the user
        self.client.login(username='testuser', password='test')
        
        # Find primary key of table
        #print("mbkj,ns")
        CircleInvite_pk = CircleInvite.objects.get(CircleInvite_Accepted='CircleInvite_Accepted').pk
        
        # Get response using pk on details view
        response = self.client.get(reverse_lazy('circleinvite_details',kwargs={'pk':CircleInvite_pk}), {
        'CircleInvite_Accepted':'CircleInvite_Accepted',
        })
        # Check for successful response
        self.assertEqual(response.status_code, 200)
