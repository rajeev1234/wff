from django.test import TestCase,SimpleTestCase
from django.urls import reverse,reverse_lazy
from .models import Singer
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.core.files.uploadedfile import SimpleUploadedFile


#  Test Class for Singer Application

class SingerTest(TestCase):

########################## Model Testing ############################
  

    # Singer object with dummy data 
    def setUp(self):

        # dummy user for login 
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password = 'test'
        )

        self.Singer =  Singer.objects.create(

        # Fields according to defined in Model    
        Singer_Daily_Charges = 141,
        Singer_Description='Singer_Description',
        Singer_Financials_Available=True,
        Singer_Genre = 'Singer_Genre',
        )

#-----------------------------------------------------------------------------------------#

    # Check redirection URL
    def test_get_absolute_url(self):
        # Redirection goes to Singer details
        self.assertEquals(self.Singer.get_absolute_url(), '/singer/1')

#-----------------------------------------------------------------------------------------#

    # Check Conent of Singer object created by create object query set
    def test_Singer_content(self):
        # Verify for each field  
        self.assertEqual(int(f'{self.Singer.Singer_Daily_Charges}'), 141)
        self.assertEqual(f'{self.Singer.Singer_Description}', 'Singer_Description')
        self.assertEqual(f'{self.Singer.Singer_Financials_Available}', 'True')
        self.assertEqual(f'{self.Singer.Singer_Genre}', 'Singer_Genre')
#--------------------------------------------------------------------------------------------#

# #############################   Model Test End   ###########################################







# ###############################    Views Test       ########################################

    
    # Test Singer List View
    
    def test_SingerList_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test')

        # Get respomse from defined URL namespace
        response = self.client.get(reverse('Singer_list'))
        self.assertEqual(response.status_code, 200)

        # Check Content of List View
        self.assertContains(response,self.user.username)
        # Check for Correct template used in template/Singers
        self.assertTemplateUsed(response, 'Singer/Singer_list.html')

#--------------------------------------------------------------------------------------------#
    

    # Test Singer Detail View

    def test_SingerDetail_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test')
        
        # Find primary key of table
        Singer_pk = Singer.objects.get(Singer_Description='Singer_Description').pk
        
        # Get response
        response = self.client.get(reverse_lazy('Singer_details',kwargs={'pk':Singer_pk}))

        # Check for any invalid value
        no_response = self.client.get(reverse_lazy('Singer_details',kwargs={'pk':10000}))

        # 202 for valid and 404 for invalid
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)

        # check for content of Detail Page
        self.assertContains(response,self.user.username)

        # Check for Correct template used in template/Singers
        self.assertTemplateUsed(response, 'Singer/Singer_details.html')

#-------------------------------------------------------------------------------------------#    


    # Test Singer Create View
    
    def test_SingerCreate_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test') 

        # Generate response after creating an view using Http post method
        response = self.client.post('/singer/new/', {
        'Singer_Daily_Charges' : 141,
        'Singer_Description': 'Singer_Description',
        'Singer_Financials_Available':True,
        'Singer_Genre' :'Singer_Genre',
        },follow = True)

        # print(response.content)
        # Check for successful response
        self.assertEqual(response.status_code, 200)
        # self.assertContains(response, False)
        self.assertContains(response, 141)
        self.assertContains(response, 'True')
        self.assertContains(response, 'Singer_Description')
        self.assertContains(response, 'Singer_Genre')

        # Check for correct template used in template/Singers
        self.assertTemplateUsed(response, 'Singer/Singer_details.html')

#---------------------------------------------------------------------------------------#


    # Test Singer Update view 

    def test_Singerupdate_view(self):
        # Login the user
        self.client.login(username='testuser', password='test')
        
        # Find primary key of table
        Singer_pk = Singer.objects.get(Singer_Description='Singer_Description').pk
        
        # Get response using pk on details view
        response = self.client.get(reverse_lazy('Singer_details',kwargs={'pk':Singer_pk}), {
        'Singer_Daily_Charges' : 141,
        'Singer_Description': 'Singer_Description',
        'Singer_Financials_Available':True,
        'Singer_Genre' :'Singer_Genre',
        })
        # Check for successful response
        self.assertEqual(response.status_code, 200)

        # Check for correct templates
        self.assertTemplateUsed(response,'Singer/Singer_details.html')


#--------------------------------------------------------------------------------------------#


# Test Delete View of Singer views

    def test_Singerdelete_view(self):
        # Login the user
        self.client.login(username='testuser', password='test')

        #Find primary key of table
        Singer_pk = Singer.objects.get(Singer_Description='Singer_Description').pk
        
        # Get response to delete 

        response = self.client.get(reverse_lazy('Singer_delete',kwargs={'pk':Singer_pk}))
        # self.assertContains(response, 'Are you sure you want to delete') # THIS PART WORKS

        # Check deleted value , returns false i.e.302
        post_response = self.client.post(reverse_lazy('Singer_delete',kwargs={'pk':Singer_pk}))
        
        # self.assertRedirects(post_response, reverse_lazy('Singer_delete',kwargs={'pk':Singer_pk}), status_code=302)


        self.assertEqual(response.status_code, 200)

        # check for Correct Template Used
        self.assertTemplateUsed(response, 'Singer/Singer_delete.html')




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
#         response = self.client.get('/Singers/1/')

#         self.assertEqual(response.status_code, 200)


#------------------------------------------------------------------------------------------------------#
    
        
#     # def test_update_page_status_code(self):
#     #     # url = reverse('SingerListView')
#     #     response = self.client.get('/Singers/1/')
#     #     self.assertEqual(response.status_code, 200)

#-------------------------------------------------------------------------------------------------------#

#     # def test_detail_page_status_code(self):
#     #     response = self.client.get('/{1}/')
#     #     self.assertEqual(response.status_code, 200)

#-------------------------------------------------------------------------------------------------------#

#     # def test_delete_page_status_code(self):
#     #     response = self.client.get('/{1}/delete/')
#     #     self.assertEqual(response.status_code, 200)