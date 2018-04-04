from django.test import TestCase,SimpleTestCase
from django.urls import reverse,reverse_lazy
from .models import FilmLocationFromGuidedWithSerial
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils import timezone


#  Test Class for FilmLocationFromGuidedWithSerial Application

class FilmLocationFromGuidedWithSerialTest(TestCase):

########################## Model Testing ############################
  

    # FilmLocationFromGuidedWithSerial object with dummy data 
    def setUp(self):

        # dummy user for login 
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password = 'test'
        )

        self.FilmLocationFromGuidedWithSerial =  FilmLocationFromGuidedWithSerial.objects.create(

        # Fields according to defined in Model    
        FilmLocationFromGuidedWithSerial_Arrival_Time = timezone.now(),
        FilmLocationFromGuidedWithSerial_Departure_Time='FilmLocationFromGuidedWithSerial_Departure_time',
        FilmLocationFromGuidedWithSerial_Location_From_Guideno='FilmLocationFromGuidedWithSerial_Location_from_guideno',
        FilmLocationFromGuidedWithSerial_Location='FilmLocationFromGuidedWithSerial_Location',
        FilmLocationFromGuidedWithSerial_Creator=self.user, # Defined above in get_user_model
        )

#-----------------------------------------------------------------------------------------#

    # Check redirection URL
    def test_get_absolute_url(self):
        # Redirection goes to FilmLocationFromGuidedWithSerial details
        self.assertEquals(self.FilmLocationFromGuidedWithSerial.get_absolute_url(), '/filmlocationfromguidedwithserial/1')

#-----------------------------------------------------------------------------------------#

    # Check Conent of FilmLocationFromGuidedWithSerial object created by create object query set
    def test_FilmLocationFromGuidedWithSerial_content(self):
        # Verify for each field  
        self.assertEqual(f'{self.FilmLocationFromGuidedWithSerial.FilmLocationFromGuidedWithSerial_Departure_Time}', 'FilmLocationFromGuidedWithSerial_Departure_time')
        self.assertEqual(f'{self.FilmLocationFromGuidedWithSerial.FilmLocationFromGuidedWithSerial_Location_From_Guideno}', 'FilmLocationFromGuidedWithSerial_Location_from_guideno')
        self.assertEqual(f'{self.FilmLocationFromGuidedWithSerial.FilmLocationFromGuidedWithSerial_Location}', 'FilmLocationFromGuidedWithSerial_Location')
        self.assertEqual(f'{self.FilmLocationFromGuidedWithSerial.FilmLocationFromGuidedWithSerial_Creator}', self.user.username) # Defined in SetUps
#--------------------------------------------------------------------------------------------#

# #############################   Model Test End   ###########################################







# ###############################    Views Test       ########################################

    
    # Test FilmLocationFromGuidedWithSerial List View
    
    def test_FilmLocationFromGuidedWithSerialList_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test')

        # Get respomse from defined URL namespace
        response = self.client.get(reverse('FilmLocationFromGuidedWithSerial_list'))
        self.assertEqual(response.status_code, 200)

        # Check Content of List View
        self.assertContains(response,self.user.username)
        # Check for Correct template used in template/FilmLocationFromGuidedWithSerials
        self.assertTemplateUsed(response, 'FilmLocationFromGuidedWithSerials/FilmLocationFromGuidedWithSerial_list.html')

#--------------------------------------------------------------------------------------------#
    

    # Test FilmLocationFromGuidedWithSerial Detail View

    def test_FilmLocationFromGuidedWithSerialDetail_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test')
        
        # Find primary key of table
        FilmLocationFromGuidedWithSerial_pk = FilmLocationFromGuidedWithSerial.objects.get(FilmLocationFromGuidedWithSerial_Location='FilmLocationFromGuidedWithSerial_Location').pk
        
        # Get response
        response = self.client.get(reverse_lazy('FilmLocationFromGuidedWithSerial_details',kwargs={'pk':FilmLocationFromGuidedWithSerial_pk}))

        # Check for any invalid value
        no_response = self.client.get(reverse_lazy('FilmLocationFromGuidedWithSerial_details',kwargs={'pk':10000}))

        # 202 for valid and 404 for invalid
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)

        # check for content of Detail Page
        self.assertContains(response,self.user.username)

        # Check for Correct template used in template/FilmLocationFromGuidedWithSerials
        self.assertTemplateUsed(response, 'FilmLocationFromGuidedWithSerials/FilmLocationFromGuidedWithSerial_details.html')

#-------------------------------------------------------------------------------------------#    


    # Test FilmLocationFromGuidedWithSerial Create View
    
    def test_FilmLocationFromGuidedWithSerialCreate_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test') 

        # Generate response after creating an view using Http post method
        response = self.client.post('/filmlocationfromguidedwithserial/new/', {
        'FilmLocationFromGuidedWithSerial_Arrival_Time' : timezone.now(),
        'FilmLocationFromGuidedWithSerial_Departure_Time':'FilmLocationFromGuidedWithSerial_Departure_time',
        'FilmLocationFromGuidedWithSerial_Location_From_Guideno':'FilmLocationFromGuidedWithSerial_Location_from_guideno',
        'FilmLocationFromGuidedWithSerial_Location':'FilmLocationFromGuidedWithSerial_Location',
        'FilmLocationFromGuidedWithSerial_Creator': self.user, # Defined above in get_user_model
        })

        # print(response.content)
        # Check for successful response
        self.assertEqual(response.status_code, 200)
        # self.assertContains(response, False)
        self.assertContains(response, 'FilmLocationFromGuidedWithSerial_Departure_time')
        self.assertContains(response, 'FilmLocationFromGuidedWithSerial_Location_from_guideno')
        self.assertContains(response, 'FilmLocationFromGuidedWithSerial_Location')
        self.assertContains(response, self.user.username) # Same as defined in SetUp

        # Check for correct template used in template/FilmLocationFromGuidedWithSerials
        self.assertTemplateUsed(response, 'FilmLocationFromGuidedWithSerials/FilmLocationFromGuidedWithSerial_new.html')

#---------------------------------------------------------------------------------------#


    # Test FilmLocationFromGuidedWithSerial Update view 

    def test_FilmLocationFromGuidedWithSerialupdate_view(self):
        # Login the user
        self.client.login(username='testuser', password='test')
        
        # Find primary key of table
        FilmLocationFromGuidedWithSerial_pk = FilmLocationFromGuidedWithSerial.objects.get(FilmLocationFromGuidedWithSerial_Location='FilmLocationFromGuidedWithSerial_Location').pk
        
        # Get response using pk on details view
        response = self.client.get(reverse_lazy('FilmLocationFromGuidedWithSerial_details',kwargs={'pk':FilmLocationFromGuidedWithSerial_pk}), {
        'FilmLocationFromGuidedWithSerial_Arrival_Time' : timezone.now(),
        'FilmLocationFromGuidedWithSerial_Departure_Time':'FilmLocationFromGuidedWithSerial_Departure_time',
        'FilmLocationFromGuidedWithSerial_Location_From_Guideno':'FilmLocationFromGuidedWithSerial_Location_from_guideno',
        'FilmLocationFromGuidedWithSerial_Location':'FilmLocationFromGuidedWithSerial_Location',
        'FilmLocationFromGuidedWithSerial_Creator': self.user, # Defined above in get_user_model
        })
        # Check for successful response
        self.assertEqual(response.status_code, 200)

        # Check for correct templates
        self.assertTemplateUsed(response,'FilmLocationFromGuidedWithSerials/FilmLocationFromGuidedWithSerial_details.html')


#--------------------------------------------------------------------------------------------#


# Test Delete View of FilmLocationFromGuidedWithSerial views

    def test_FilmLocationFromGuidedWithSerialdelete_view(self):
        # Login the user
        self.client.login(username='testuser', password='test')

        #Find primary key of table
        FilmLocationFromGuidedWithSerial_pk = FilmLocationFromGuidedWithSerial.objects.get(FilmLocationFromGuidedWithSerial_Location='FilmLocationFromGuidedWithSerial_Location').pk
        
        # Get response to delete 

        response = self.client.get(reverse_lazy('FilmLocationFromGuidedWithSerial_delete',kwargs={'pk':FilmLocationFromGuidedWithSerial_pk}))
        # self.assertContains(response, 'Are you sure you want to delete') # THIS PART WORKS

        # Check deleted value , returns false i.e.302
        post_response = self.client.post(reverse_lazy('FilmLocationFromGuidedWithSerial_delete',kwargs={'pk':FilmLocationFromGuidedWithSerial_pk}))
        
        # self.assertRedirects(post_response, reverse_lazy('FilmLocationFromGuidedWithSerial_delete',kwargs={'pk':FilmLocationFromGuidedWithSerial_pk}), status_code=302)


        self.assertEqual(response.status_code, 200)

        # check for Correct Template Used
        self.assertTemplateUsed(response, 'FilmLocationFromGuidedWithSerials/FilmLocationFromGuidedWithSerial_delete.html')




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
#         response = self.client.get('/FilmLocationFromGuidedWithSerials/1/')

#         self.assertEqual(response.status_code, 200)


#------------------------------------------------------------------------------------------------------#
    
        
#     # def test_update_page_status_code(self):
#     #     # url = reverse('FilmLocationFromGuidedWithSerialListView')
#     #     response = self.client.get('/FilmLocationFromGuidedWithSerials/1/')
#     #     self.assertEqual(response.status_code, 200)

#-------------------------------------------------------------------------------------------------------#

#     # def test_detail_page_status_code(self):
#     #     response = self.client.get('/{1}/')
#     #     self.assertEqual(response.status_code, 200)

#-------------------------------------------------------------------------------------------------------#

#     # def test_delete_page_status_code(self):
#     #     response = self.client.get('/{1}/delete/')
#     #     self.assertEqual(response.status_code, 200)