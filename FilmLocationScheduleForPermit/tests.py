from django.test import TestCase,SimpleTestCase
from django.urls import reverse,reverse_lazy
from .models import FilmLocationScheduleForPermit
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils import timezone


#  Test Class for FilmLocationScheduleForPermit Application

class FilmLocationScheduleForPermitTest(TestCase):

########################## Model Testing ############################
  

    # FilmLocationScheduleForPermit object with dummy data 
    def setUp(self):

        # dummy user for login 
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password = 'test'
        )

        self.FilmLocationScheduleForPermit =  FilmLocationScheduleForPermit.objects.create(

        # Fields according to defined in Model    
        FilmLocationScheduleForPermit_Location = 'FilmLocationScheduleForPermit_Location',
        FilmLocationScheduleForPermit_SNo='FilmLocationScheduleForPermit_SNo',
        FilmLocationScheduleForPermit_Modified_Date=  timezone.now(),
        FilmLocationScheduleForPermit_Created_Date =  timezone.now(),
        FilmLocationScheduleForPermit_Creator =  self.user,

        )

#-----------------------------------------------------------------------------------------#

    # Check redirection URL
    def test_get_absolute_url(self):
        # Redirection goes to FilmLocationScheduleForPermit details
        self.assertEquals(self.FilmLocationScheduleForPermit.get_absolute_url(), '/filmlocationscheduleforpermit/1')

#-----------------------------------------------------------------------------------------#

    # Check Conent of FilmLocationScheduleForPermit object created by create object query set
    def test_FilmLocationScheduleForPermit_content(self):
        # Verify for each field  
        self.assertEqual(f'{self.FilmLocationScheduleForPermit.FilmLocationScheduleForPermit_Location}', 'FilmLocationScheduleForPermit_Location')
        self.assertEqual(f'{self.FilmLocationScheduleForPermit.FilmLocationScheduleForPermit_SNo}', 'FilmLocationScheduleForPermit_SNo')
        self.assertEqual(f'{self.FilmLocationScheduleForPermit.FilmLocationScheduleForPermit_Creator}', self.user.username)
#--------------------------------------------------------------------------------------------#

# #############################   Model Test End   ###########################################







# ###############################    Views Test       ########################################

    
    # Test FilmLocationScheduleForPermit List View
    
    def test_FilmLocationScheduleForPermitList_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test')

        # Get respomse from defined URL namespace
        response = self.client.get(reverse('FilmLocationScheduleForPermit_list'))
        self.assertEqual(response.status_code, 200)

        # Check Content of List View
        self.assertContains(response,self.user.username)
        # Check for Correct template used in template/FilmLocationScheduleForPermits
        self.assertTemplateUsed(response, 'FilmLocationScheduleForPermits/FilmLocationScheduleForPermit_list.html')

#--------------------------------------------------------------------------------------------#
    

    # Test FilmLocationScheduleForPermit Detail View

    def test_FilmLocationScheduleForPermitDetail_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test')
        
        # Find primary key of table
        FilmLocationScheduleForPermit_pk = FilmLocationScheduleForPermit.objects.get(FilmLocationScheduleForPermit_Location='FilmLocationScheduleForPermit_Location').pk
        
        # Get response
        response = self.client.get(reverse_lazy('FilmLocationScheduleForPermit_details',kwargs={'pk':FilmLocationScheduleForPermit_pk}))

        # Check for any invalid value
        no_response = self.client.get(reverse_lazy('FilmLocationScheduleForPermit_details',kwargs={'pk':10000}))

        # 202 for valid and 404 for invalid
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)

        # check for content of Detail Page
        self.assertContains(response,self.user.username)

        # Check for Correct template used in template/FilmLocationScheduleForPermits
        self.assertTemplateUsed(response, 'FilmLocationScheduleForPermits/FilmLocationScheduleForPermit_details.html')

#-------------------------------------------------------------------------------------------#    


    # Test FilmLocationScheduleForPermit Create View
    
    def test_FilmLocationScheduleForPermitCreate_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test') 

        # Generate response after creating an view using Http post method
        response = self.client.post('/filmlocationscheduleforpermit/new/', {
        'FilmLocationScheduleForPermit_Location' : 'FilmLocationScheduleForPermit_Location',
        'FilmLocationScheduleForPermit_SNo':'FilmLocationScheduleForPermit_SNo',
        'FilmLocationScheduleForPermit_Creator': self.user
        })

        # print(response.content)
        # Check for successful response
        self.assertEqual(response.status_code, 200)
        # self.assertContains(response, False)
        self.assertContains(response, 'FilmLocationScheduleForPermit_Location')
        self.assertContains(response, 'FilmLocationScheduleForPermit_SNo')
        self.assertContains(response, self.user.username) # Same as defined in SetUp

        # Check for correct template used in template/FilmLocationScheduleForPermits
        self.assertTemplateUsed(response, 'FilmLocationScheduleForPermits/FilmLocationScheduleForPermit_new.html')

#---------------------------------------------------------------------------------------#


    # Test FilmLocationScheduleForPermit Update view 

    def test_FilmLocationScheduleForPermitupdate_view(self):
        # Login the user
        self.client.login(username='testuser', password='test')
        
        # Find primary key of table
        FilmLocationScheduleForPermit_pk = FilmLocationScheduleForPermit.objects.get(FilmLocationScheduleForPermit_Location='FilmLocationScheduleForPermit_Location').pk
        
        # Get response using pk on details view
        response = self.client.get(reverse_lazy('FilmLocationScheduleForPermit_details',kwargs={'pk':FilmLocationScheduleForPermit_pk}), {
        'FilmLocationScheduleForPermit_Location' : 'FilmLocationScheduleForPermit_Location',
        'FilmLocationScheduleForPermit_SNo':'FilmLocationScheduleForPermit_SNo',
        'FilmLocationScheduleForPermit_Creator': self.user
        })
        # Check for successful response
        self.assertEqual(response.status_code, 200)

        # Check for correct templates
        self.assertTemplateUsed(response,'FilmLocationScheduleForPermits/FilmLocationScheduleForPermit_details.html')


#--------------------------------------------------------------------------------------------#


# Test Delete View of FilmLocationScheduleForPermit views

    def test_FilmLocationScheduleForPermitdelete_view(self):
        # Login the user
        self.client.login(username='testuser', password='test')

        #Find primary key of table
        FilmLocationScheduleForPermit_pk = FilmLocationScheduleForPermit.objects.get(FilmLocationScheduleForPermit_Location='FilmLocationScheduleForPermit_Location').pk
        
        # Get response to delete 

        response = self.client.get(reverse_lazy('FilmLocationScheduleForPermit_delete',kwargs={'pk':FilmLocationScheduleForPermit_pk}))
        # self.assertContains(response, 'Are you sure you want to delete') # THIS PART WORKS

        # Check deleted value , returns false i.e.302
        post_response = self.client.post(reverse_lazy('FilmLocationScheduleForPermit_delete',kwargs={'pk':FilmLocationScheduleForPermit_pk}))
        
        # self.assertRedirects(post_response, reverse_lazy('FilmLocationScheduleForPermit_delete',kwargs={'pk':FilmLocationScheduleForPermit_pk}), status_code=302)


        self.assertEqual(response.status_code, 200)

        # check for Correct Template Used
        self.assertTemplateUsed(response, 'FilmLocationScheduleForPermits/FilmLocationScheduleForPermit_delete.html')




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
#         response = self.client.get('/FilmLocationScheduleForPermits/1/')

#         self.assertEqual(response.status_code, 200)


#------------------------------------------------------------------------------------------------------#
    
        
#     # def test_update_page_status_code(self):
#     #     # url = reverse('FilmLocationScheduleForPermitListView')
#     #     response = self.client.get('/FilmLocationScheduleForPermits/1/')
#     #     self.assertEqual(response.status_code, 200)

#-------------------------------------------------------------------------------------------------------#

#     # def test_detail_page_status_code(self):
#     #     response = self.client.get('/{1}/')
#     #     self.assertEqual(response.status_code, 200)

#-------------------------------------------------------------------------------------------------------#

#     # def test_delete_page_status_code(self):
#     #     response = self.client.get('/{1}/delete/')
#     #     self.assertEqual(response.status_code, 200)