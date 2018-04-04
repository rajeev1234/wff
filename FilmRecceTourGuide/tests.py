from django.test import TestCase,SimpleTestCase
from django.urls import reverse,reverse_lazy
from .models import FilmRecceTourGuide
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils import timezone


#  Test Class for FilmRecceTourGuide Application

class FilmRecceTourGuideTest(TestCase):

########################## Model Testing ############################
  

    # FilmRecceTourGuide object with dummy data 
    def setUp(self):

        # dummy user for login 
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password = 'test'
        )

        self.FilmRecceTourGuide =  FilmRecceTourGuide.objects.create(

        # Fields according to defined in Model    
        FilmRecceTourGuide_EndLocation = 'FilmRecceTourGuide_EndLocation',
        FilmRecceTourGuide_EndTime= timezone.now(),
        FilmRecceTourGuide_Passing_Year='FilmRecceTourGuide_Passing_Year',
        FilmRecceTourGuide_StartLocation='FilmRecceTourGuide_StartLocation',
        FilmRecceTourGuide_StartTime=timezone.now(),
        FilmRecceTourGuide_TourGuideName='FilmRecceTourGuide_TourGuideName',
        FilmRecceTourGuide_Creator=self.user,
        FilmRecceTourGuide_Modified_Date=  timezone.now(),
        FilmRecceTourGuide_Created_Time =  timezone.now(),
        )

#-----------------------------------------------------------------------------------------#

    # Check redirection URL
    def test_get_absolute_url(self):
        # Redirection goes to FilmRecceTourGuide details
        self.assertEquals(self.FilmRecceTourGuide.get_absolute_url(), '/filmreccetourguide/1')

#-----------------------------------------------------------------------------------------#

    # Check Conent of FilmRecceTourGuide object created by create object query set
    def test_FilmRecceTourGuide_content(self):
        # Verify for each field  
        self.assertEqual(f'{self.FilmRecceTourGuide.FilmRecceTourGuide_EndLocation}', 'FilmRecceTourGuide_EndLocation')
        self.assertEqual(f'{self.FilmRecceTourGuide.FilmRecceTourGuide_Passing_Year}', 'FilmRecceTourGuide_Passing_Year')
        self.assertEqual(f'{self.FilmRecceTourGuide.FilmRecceTourGuide_StartLocation}', 'FilmRecceTourGuide_StartLocation')
        self.assertEqual(f'{self.FilmRecceTourGuide.FilmRecceTourGuide_TourGuideName}', 'FilmRecceTourGuide_TourGuideName')
        self.assertEqual(f'{self.FilmRecceTourGuide.FilmRecceTourGuide_Creator}', self.user.username)
#--------------------------------------------------------------------------------------------#

# #############################   Model Test End   ###########################################







# ###############################    Views Test       ########################################

    
    # Test FilmRecceTourGuide List View
    
    def test_FilmRecceTourGuideList_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test')

        # Get respomse from defined URL namespace
        response = self.client.get(reverse('FilmRecceTourGuide_list'))
        self.assertEqual(response.status_code, 200)

        # Check Content of List View
        self.assertContains(response,self.user.username)
        # Check for Correct template used in template/FilmRecceTourGuides
        self.assertTemplateUsed(response, 'FilmRecceTourGuides/FilmRecceTourGuide_list.html')

#--------------------------------------------------------------------------------------------#
    

    # Test FilmRecceTourGuide Detail View

    def test_FilmRecceTourGuideDetail_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test')
        
        # Find primary key of table
        FilmRecceTourGuide_pk = FilmRecceTourGuide.objects.get(FilmRecceTourGuide_StartLocation='FilmRecceTourGuide_StartLocation').pk
        
        # Get response
        response = self.client.get(reverse_lazy('FilmRecceTourGuide_details',kwargs={'pk':FilmRecceTourGuide_pk}))

        # Check for any invalid value
        no_response = self.client.get(reverse_lazy('FilmRecceTourGuide_details',kwargs={'pk':10000}))

        # 202 for valid and 404 for invalid
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)

        # check for content of Detail Page
        self.assertContains(response,self.user.username)

        # Check for Correct template used in template/FilmRecceTourGuides
        self.assertTemplateUsed(response, 'FilmRecceTourGuides/FilmRecceTourGuide_details.html')

#-------------------------------------------------------------------------------------------#    


    # Test FilmRecceTourGuide Create View
    
    def test_FilmRecceTourGuideCreate_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test') 

        # Generate response after creating an view using Http post method
        response = self.client.post('/filmreccetourguide/new/', {
        'FilmRecceTourGuide_EndLocation' : 'FilmRecceTourGuide_EndLocation',
        'FilmRecceTourGuide_EndTime': timezone.now(),
        'FilmRecceTourGuide_Passing_Year':'FilmRecceTourGuide_Passing_Year',
        'FilmRecceTourGuide_StartLocation':'FilmRecceTourGuide_StartLocation',
        'FilmRecceTourGuide_StartTime':timezone.now(),
        'FilmRecceTourGuide_TourGuideName':'FilmRecceTourGuide_TourGuideName',
        'FilmRecceTourGuide_Creator':self.user,
        })

        # print(response.content)
        # Check for successful response
        self.assertEqual(response.status_code, 200)
        # self.assertContains(response, False)
        self.assertContains(response, 'FilmRecceTourGuide_EndLocation')
        self.assertContains(response, 'FilmRecceTourGuide_Passing_Year')
        self.assertContains(response, 'FilmRecceTourGuide_StartLocation')
        self.assertContains(response, 'FilmRecceTourGuide_TourGuideName')
        self.assertContains(response, self.user.username) # Same as defined in SetUp

        # Check for correct template used in template/FilmRecceTourGuides
        self.assertTemplateUsed(response, 'FilmRecceTourGuides/FilmRecceTourGuide_new.html')

#---------------------------------------------------------------------------------------#


    # Test FilmRecceTourGuide Update view 

    def test_FilmRecceTourGuideupdate_view(self):
        # Login the user
        self.client.login(username='testuser', password='test')
        
        # Find primary key of table
        FilmRecceTourGuide_pk = FilmRecceTourGuide.objects.get(FilmRecceTourGuide_EndLocation='FilmRecceTourGuide_EndLocation').pk
        
        # Get response using pk on details view
        response = self.client.get(reverse_lazy('FilmRecceTourGuide_details',kwargs={'pk':FilmRecceTourGuide_pk}), {
        'FilmRecceTourGuide_EndLocation' : 'FilmRecceTourGuide_EndLocation',
        'FilmRecceTourGuide_EndTime': timezone.now(),
        'FilmRecceTourGuide_Passing_Year':'FilmRecceTourGuide_Passing_Year',
        'FilmRecceTourGuide_StartLocation':'FilmRecceTourGuide_StartLocation',
        'FilmRecceTourGuide_StartTime':timezone.now(),
        'FilmRecceTourGuide_TourGuideName':'FilmRecceTourGuide_TourGuideName',
        'FilmRecceTourGuide_Creator':self.user,
        })
        # Check for successful response
        self.assertEqual(response.status_code, 200)

        # Check for correct templates
        self.assertTemplateUsed(response,'FilmRecceTourGuides/FilmRecceTourGuide_details.html')


#--------------------------------------------------------------------------------------------#


# Test Delete View of FilmRecceTourGuide views

    def test_FilmRecceTourGuidedelete_view(self):
        # Login the user
        self.client.login(username='testuser', password='test')

        #Find primary key of table
        FilmRecceTourGuide_pk = FilmRecceTourGuide.objects.get(FilmRecceTourGuide_StartLocation='FilmRecceTourGuide_StartLocation').pk
        
        # Get response to delete 

        response = self.client.get(reverse_lazy('FilmRecceTourGuide_delete',kwargs={'pk':FilmRecceTourGuide_pk}))
        # self.assertContains(response, 'Are you sure you want to delete') # THIS PART WORKS

        # Check deleted value , returns false i.e.302
        post_response = self.client.post(reverse_lazy('FilmRecceTourGuide_delete',kwargs={'pk':FilmRecceTourGuide_pk}))
        
        # self.assertRedirects(post_response, reverse_lazy('FilmRecceTourGuide_delete',kwargs={'pk':FilmRecceTourGuide_pk}), status_code=302)


        self.assertEqual(response.status_code, 200)

        # check for Correct Template Used
        self.assertTemplateUsed(response, 'FilmRecceTourGuides/FilmRecceTourGuide_delete.html')




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
#         response = self.client.get('/FilmRecceTourGuides/1/')

#         self.assertEqual(response.status_code, 200)


#------------------------------------------------------------------------------------------------------#
    
        
#     # def test_update_page_status_code(self):
#     #     # url = reverse('FilmRecceTourGuideListView')
#     #     response = self.client.get('/FilmRecceTourGuides/1/')
#     #     self.assertEqual(response.status_code, 200)

#-------------------------------------------------------------------------------------------------------#

#     # def test_detail_page_status_code(self):
#     #     response = self.client.get('/{1}/')
#     #     self.assertEqual(response.status_code, 200)

#-------------------------------------------------------------------------------------------------------#

#     # def test_delete_page_status_code(self):
#     #     response = self.client.get('/{1}/delete/')
#     #     self.assertEqual(response.status_code, 200)