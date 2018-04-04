from django.test import TestCase,SimpleTestCase
from django.urls import reverse,reverse_lazy
from .models import FilmRecceRoute
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils import timezone


#  Test Class for FilmRecceRoute Application

class FilmRecceRouteTest(TestCase):

########################## Model Testing ############################
  

    # FilmRecceRoute object with dummy data 
    def setUp(self):

        # dummy user for login 
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password = 'test'
        )

        self.FilmRecceRoute =  FilmRecceRoute.objects.create(

        # Fields according to defined in Model    
        FilmRecceRoute_Distance = 'FilmRecceRoute_Distance',
        FilmRecceRoute_Filmrecce_Name='FilmRecceRoute_Filmrecce_Name',
        FilmRecceRoute_Route_Name='FilmRecceRoute_Route_Name',
        FilmRecceRoute_Travel_Time='FilmRecceRoute_Travel_Time',
        FilmRecceRoute_Creator=self.user,
        FilmRecceRoute_Modified_Date=  timezone.now(),
        FilmRecceRoute_Created_Date =  timezone.now()
        )

#-----------------------------------------------------------------------------------------#

    # Check redirection URL
    def test_get_absolute_url(self):
        # Redirection goes to FilmRecceRoute details
        self.assertEquals(self.FilmRecceRoute.get_absolute_url(), '/filmrecceroute/1')

#-----------------------------------------------------------------------------------------#

    # Check Conent of FilmRecceRoute object created by create object query set
    def test_FilmRecceRoute_content(self):
        # Verify for each field  
        self.assertEqual(f'{self.FilmRecceRoute.FilmRecceRoute_Distance}', 'FilmRecceRoute_Distance')
        self.assertEqual(f'{self.FilmRecceRoute.FilmRecceRoute_Filmrecce_Name}', 'FilmRecceRoute_Filmrecce_Name')
        self.assertEqual(f'{self.FilmRecceRoute.FilmRecceRoute_Route_Name}', 'FilmRecceRoute_Route_Name')
        self.assertEqual(f'{self.FilmRecceRoute.FilmRecceRoute_Travel_Time}', 'FilmRecceRoute_Travel_Time')
        self.assertEqual(f'{self.FilmRecceRoute.FilmRecceRoute_Creator}', self.user.username)
#--------------------------------------------------------------------------------------------#

# #############################   Model Test End   ###########################################







# ###############################    Views Test       ########################################

    
    # Test FilmRecceRoute List View
    
    def test_FilmRecceRouteList_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test')

        # Get respomse from defined URL namespace
        response = self.client.get(reverse('FilmRecceRoute_list'))
        self.assertEqual(response.status_code, 200)

        # Check Content of List View
        self.assertContains(response,self.user.username)
        # Check for Correct template used in template/FilmRecceRoutes
        self.assertTemplateUsed(response, 'FilmRecceRoutes/FilmRecceRoute_list.html')

#--------------------------------------------------------------------------------------------#
    

    # Test FilmRecceRoute Detail View

    def test_FilmRecceRouteDetail_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test')
        
        # Find primary key of table
        FilmRecceRoute_pk = FilmRecceRoute.objects.get(FilmRecceRoute_Route_Name='FilmRecceRoute_Route_Name').pk
        
        # Get response
        response = self.client.get(reverse_lazy('FilmRecceRoute_details',kwargs={'pk':FilmRecceRoute_pk}))

        # Check for any invalid value
        no_response = self.client.get(reverse_lazy('FilmRecceRoute_details',kwargs={'pk':10000}))

        # 202 for valid and 404 for invalid
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)

        # check for content of Detail Page
        self.assertContains(response,self.user.username)

        # Check for Correct template used in template/FilmRecceRoutes
        self.assertTemplateUsed(response, 'FilmRecceRoutes/FilmRecceRoute_details.html')

#-------------------------------------------------------------------------------------------#    


    # Test FilmRecceRoute Create View
    
    def test_FilmRecceRouteCreate_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test') 

        # Generate response after creating an view using Http post method
        response = self.client.post('/filmrecceroute/new/', {
        'FilmRecceRoute_Distance' : 'FilmRecceRoute_Distance',
        'FilmRecceRoute_Filmrecce_Name':'FilmRecceRoute_Filmrecce_Name',
        'FilmRecceRoute_Route_Name':'FilmRecceRoute_Route_Name',
        'FilmRecceRoute_Travel_Time':'FilmRecceRoute_Travel_Time',
        'FilmRecceRoute_Creator':self.user,
        })

        # print(response.content)
        # Check for successful response
        self.assertEqual(response.status_code, 200)
        # self.assertContains(response, False)
        self.assertContains(response, 'FilmRecceRoute_Distance')
        self.assertContains(response, 'FilmRecceRoute_Filmrecce_Name')
        self.assertContains(response, 'FilmRecceRoute_Route_Name')
        self.assertContains(response, 'FilmRecceRoute_Travel_Time')
        self.assertContains(response, self.user.username) # Same as defined in SetUp

        # Check for correct template used in template/FilmRecceRoutes
        self.assertTemplateUsed(response, 'FilmRecceRoutes/FilmRecceRoute_new.html')

#---------------------------------------------------------------------------------------#


    # Test FilmRecceRoute Update view 

    def test_FilmRecceRouteupdate_view(self):
        # Login the user
        self.client.login(username='testuser', password='test')
        
        # Find primary key of table
        FilmRecceRoute_pk = FilmRecceRoute.objects.get(FilmRecceRoute_Distance='FilmRecceRoute_Distance').pk
        
        # Get response using pk on details view
        response = self.client.get(reverse_lazy('FilmRecceRoute_details',kwargs={'pk':FilmRecceRoute_pk}), {
        'FilmRecceRoute_Distance' : 'FilmRecceRoute_Distance',
        'FilmRecceRoute_Filmrecce_Name':'FilmRecceRoute_Filmrecce_Name',
        'FilmRecceRoute_Route_Name':'FilmRecceRoute_Route_Name',
        'FilmRecceRoute_Travel_Time':'FilmRecceRoute_Travel_Time',
        'FilmRecceRoute_Creator':self.user,
        })
        # Check for successful response
        self.assertEqual(response.status_code, 200)

        # Check for correct templates
        self.assertTemplateUsed(response,'FilmRecceRoutes/FilmRecceRoute_details.html')


#--------------------------------------------------------------------------------------------#


# Test Delete View of FilmRecceRoute views

    def test_FilmRecceRoutedelete_view(self):
        # Login the user
        self.client.login(username='testuser', password='test')

        #Find primary key of table
        FilmRecceRoute_pk = FilmRecceRoute.objects.get(FilmRecceRoute_Route_Name='FilmRecceRoute_Route_Name').pk
        
        # Get response to delete 

        response = self.client.get(reverse_lazy('FilmRecceRoute_delete',kwargs={'pk':FilmRecceRoute_pk}))
        # self.assertContains(response, 'Are you sure you want to delete') # THIS PART WORKS

        # Check deleted value , returns false i.e.302
        post_response = self.client.post(reverse_lazy('FilmRecceRoute_delete',kwargs={'pk':FilmRecceRoute_pk}))
        
        # self.assertRedirects(post_response, reverse_lazy('FilmRecceRoute_delete',kwargs={'pk':FilmRecceRoute_pk}), status_code=302)


        self.assertEqual(response.status_code, 200)

        # check for Correct Template Used
        self.assertTemplateUsed(response, 'FilmRecceRoutes/FilmRecceRoute_delete.html')




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
#         response = self.client.get('/FilmRecceRoutes/1/')

#         self.assertEqual(response.status_code, 200)


#------------------------------------------------------------------------------------------------------#
    
        
#     # def test_update_page_status_code(self):
#     #     # url = reverse('FilmRecceRouteListView')
#     #     response = self.client.get('/FilmRecceRoutes/1/')
#     #     self.assertEqual(response.status_code, 200)

#-------------------------------------------------------------------------------------------------------#

#     # def test_detail_page_status_code(self):
#     #     response = self.client.get('/{1}/')
#     #     self.assertEqual(response.status_code, 200)

#-------------------------------------------------------------------------------------------------------#

#     # def test_delete_page_status_code(self):
#     #     response = self.client.get('/{1}/delete/')
#     #     self.assertEqual(response.status_code, 200)