from django.test import TestCase,SimpleTestCase
from django.urls import reverse,reverse_lazy
from .models import SubscriptionPlan
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils import timezone


#  Test Class for SubscriptionPlan Application

class SubscriptionPlanTest(TestCase):

########################## Model Testing ####   ########################
  

    # SubscriptionPlan object with dummy data 
    def setUp(self):

        # dummy user for login 
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password = 'test'
        )

        self.SubscriptionPlan =  SubscriptionPlan.objects.create(

        # Fields according to defined in Model    
        SubscriptionPlan_Amount = 199,
        SubscriptionPlan_End_Date = timezone.now(),
        SubscriptionPlan_FOR_FILM_COIN = 1000,
        SubscriptionPlan_Openings_Allowed = True,
        SubscriptionPlan_Location_Allowed = True,
        SubscriptionPlan_Pitch_Allowed = True,
        SubscriptionPlan_Pitch_Box_Capacity_Image_per_pitch = 111,
        SubscriptionPlan_Start_Date = timezone.now(),
        SubscriptionPlan_Type = 'SubscriptionPlan_Type',
        SubscriptionPlan_User_ID = self.user,
        )

#-----------------------------------------------------------------------------------------#

    # Check redirection URL
    def test_get_absolute_url(self):
        # Redirection goes to SubscriptionPlan details
        self.assertEquals(self.SubscriptionPlan.get_absolute_url(), '/subscriptionplan/1')

#-----------------------------------------------------------------------------------------#

    # Check Conent of SubscriptionPlan object created by create object query set
    def test_SubscriptionPlan_content(self):
        # Verify for each field  
        self.assertEqual(int(f'{self.SubscriptionPlan.SubscriptionPlan_Amount}'), 199)
        self.assertEqual(int(f'{self.SubscriptionPlan.SubscriptionPlan_FOR_FILM_COIN}'), 1000)
        self.assertEqual(bool(f'{self.SubscriptionPlan.SubscriptionPlan_Openings_Allowed}'), True)
        self.assertEqual(bool(f'{self.SubscriptionPlan.SubscriptionPlan_Location_Allowed}'), True)
        self.assertEqual(bool(f'{self.SubscriptionPlan.SubscriptionPlan_Pitch_Allowed}'), True)
        self.assertEqual(int(f'{self.SubscriptionPlan.SubscriptionPlan_Pitch_Box_Capacity_Image_per_pitch}'), 111)
        self.assertEqual(f'{self.SubscriptionPlan.SubscriptionPlan_Type}', 'SubscriptionPlan_Type')
        self.assertEqual(f'{self.SubscriptionPlan.SubscriptionPlan_User_ID}', self.user.username)
#--------------------------------------------------------------------------------------------#

# #############################   Model Test End   ###########################################







# ###############################    Views Test       ########################################

    
    # Test SubscriptionPlan List View
    
    def test_SubscriptionPlanList_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test')

        # Get respomse from defined URL namespace
        response = self.client.get(reverse('SubscriptionPlan_list'))
        self.assertEqual(response.status_code, 200)

        # Check Content of List View
        self.assertContains(response,199)
        self.assertContains(response,'SubscriptionPlan_Type')
        # Check for Correct template used in template/SubscriptionPlans
        self.assertTemplateUsed(response, 'SubscriptionPlans/SubscriptionPlan_list.html')

#--------------------------------------------------------------------------------------------#
    

    # Test SubscriptionPlan Detail View

    def test_SubscriptionPlanDetail_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test')
        
        # Find primary key of table
        SubscriptionPlan_pk = SubscriptionPlan.objects.get(SubscriptionPlan_Amount=199).pk
        
        # Get response
        response = self.client.get(reverse_lazy('SubscriptionPlan_details',kwargs={'pk':SubscriptionPlan_pk}))

        # Check for any invalid value
        no_response = self.client.get(reverse_lazy('SubscriptionPlan_details',kwargs={'pk':10000}))

        # 202 for valid and 404 for invalid
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)

        # check for content of Detail Page
        self.assertContains(response,self.user.username)

        # Check for Correct template used in template/SubscriptionPlans
        self.assertTemplateUsed(response, 'SubscriptionPlans/SubscriptionPlan_details.html')

#-------------------------------------------------------------------------------------------#    


    # Test SubscriptionPlan Create View
    
    def test_SubscriptionPlanCreate_view(self):
        # Login the user defined in SetUps
        self.client.login(username='testuser', password='test') 

        # Generate response after creating an view using Http post method
        response = self.client.post('/subscriptionplan/new/', {
        'SubscriptionPlan_Amount' : 199,
        'SubscriptionPlan_End_Date' : timezone.now(),
        'SubscriptionPlan_FOR_FILM_COIN' : 1000,
        'SubscriptionPlan_Openings_Allowed' : True,
        'SubscriptionPlan_Location_Allowed' : True,
        'SubscriptionPlan_Pitch_Allowed' : True,
        'SubscriptionPlan_Pitch_Box_Capacity_Image_per_pitch' : 111,
        'SubscriptionPlan_Start_Date' : timezone.now(),
        'SubscriptionPlan_Type' : 'SubscriptionPlan_Type',
        'SubscriptionPlan_User_ID' : self.user,
        })

        # print(response.content)
        # Check for successful response
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'SubscriptionPlan_Type')
        self.assertContains(response, self.user.username)
        self.assertContains(response, 'checked')
        self.assertContains(response, 111)
        self.assertContains(response, 1000)
        self.assertContains(response, 199)


        # Check for correct template used in template/SubscriptionPlans
        self.assertTemplateUsed(response, 'SubscriptionPlans/SubscriptionPlan_new.html')

#---------------------------------------------------------------------------------------#


    # Test SubscriptionPlan Update view 

    def test_SubscriptionPlanupdate_view(self):
        # Login the user
        self.client.login(username='testuser', password='test')
        
        # Find primary key of table
        SubscriptionPlan_pk = SubscriptionPlan.objects.get(SubscriptionPlan_Type='SubscriptionPlan_Type').pk
        
        # Get response using pk on details view
        response = self.client.get(reverse_lazy('SubscriptionPlan_details',kwargs={'pk':SubscriptionPlan_pk}), {
        'SubscriptionPlan_Amount' : 199,
        'SubscriptionPlan_End_Date' : timezone.now(),
        'SubscriptionPlan_FOR_FILM_COIN' : 1000,
        'SubscriptionPlan_Openings_Allowed' : True,
        'SubscriptionPlan_Location_Allowed' : True,
        'SubscriptionPlan_Pitch_Allowed' : True,
        'SubscriptionPlan_Pitch_Box_Capacity_Image_per_pitch' : 111,
        'SubscriptionPlan_Start_Date' : timezone.now(),
        'SubscriptionPlan_Type' : 'SubscriptionPlan_Type',
        'SubscriptionPlan_User_ID' : self.user,
        })
        # Check for successful response
        self.assertEqual(response.status_code, 200)

        # Check for correct templates
        self.assertTemplateUsed(response,'SubscriptionPlans/SubscriptionPlan_details.html')


#--------------------------------------------------------------------------------------------#


# Test Delete View of SubscriptionPlan views

    def test_SubscriptionPlandelete_view(self):
        # Login the user
        self.client.login(username='testuser', password='test')

        #Find primary key of table
        SubscriptionPlan_pk = SubscriptionPlan.objects.get(SubscriptionPlan_Type='SubscriptionPlan_Type').pk
        
        # Get response to delete 

        response = self.client.get(reverse_lazy('SubscriptionPlan_delete',kwargs={'pk':SubscriptionPlan_pk}))
        # self.assertContains(response, 'Are you sure you want to delete') # THIS PART WORKS

        # Check deleted value , returns false i.e.302
        post_response = self.client.post(reverse_lazy('SubscriptionPlan_delete',kwargs={'pk':SubscriptionPlan_pk}))
        
        # self.assertRedirects(post_response, reverse_lazy('SubscriptionPlan_delete',kwargs={'pk':SubscriptionPlan_pk}), status_code=302)


        self.assertEqual(response.status_code, 200)

        # check for Correct Template Used
        self.assertTemplateUsed(response, 'SubscriptionPlans/SubscriptionPlan_delete.html')




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
#         response = self.client.get('/SubscriptionPlans/1/')

#         self.assertEqual(response.status_code, 200)


#------------------------------------------------------------------------------------------------------#
    
        
#     # def test_update_page_status_code(self):
#     #     # url = reverse('SubscriptionPlanListView')
#     #     response = self.client.get('/SubscriptionPlans/1/')
#     #     self.assertEqual(response.status_code, 200)

#-------------------------------------------------------------------------------------------------------#

#     # def test_detail_page_status_code(self):
#     #     response = self.client.get('/{1}/')
#     #     self.assertEqual(response.status_code, 200)

#-------------------------------------------------------------------------------------------------------#

#     # def test_delete_page_status_code(self):
#     #     response = self.client.get('/{1}/delete/')
#     #     self.assertEqual(response.status_code, 200)