from django.test import TestCase,SimpleTestCase
from django.urls import reverse,reverse_lazy
from .models import SpecialArt
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.core.files.uploadedfile import SimpleUploadedFile


#  Test Class for SpecialArt Application

class SpecialArtTest(TestCase):

########################## Model Testing ############################
  

    # SpecialArt object with dummy data 
    def setUp(self):

        # dummy user for login 
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password = 'test'
        )

        self.SpecialArt =  SpecialArt.objects.create(

        # Fields according to defined in Model    
        SpecialArt_Charges_Available = True,
        SpecialArt_Daily_Charges=100,
        SpecialArt_Description='SpecialArt_Description',
        SpecialArt_Special_Art_ID = '13bcs0035',
        )

#-----------------------------------------------------------------------------------------#

    # Check redirection URL
    def test_get_absolute_url(self):
        # Redirection goes to SpecialArt details
        self.assertEquals(self.SpecialArt.get_absolute_url(), '/specialart/1')

#-----------------------------------------------------------------------------------------#

    # Check Conent of SpecialArt object created by create object query set
    def test_SpecialArt_content(self):
        # Verify for each field  
        self.assertEqual(int(f'{self.SpecialArt.SpecialArt_Daily_Charges}'), 100)
        self.assertEqual(f'{self.SpecialArt.SpecialArt_Charges_Available}', 'True')
        self.assertEqual(f'{self.SpecialArt.SpecialArt_Description}', 'SpecialArt_Description')
        self.assertEqual(f'{self.SpecialArt.SpecialArt_Special_Art_ID}', '13bcs0035')
#--------------------------------------------------------------------------------------------#

# #############################   Model Test End   ###########################################







# ###############################    Views Test       ########################################

    
    # Test SpecialArt List View
    
    def test_SpecialArtList_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test')

        # Get respomse from defined URL namespace
        response = self.client.get(reverse('SpecialArt_list'))
        self.assertEqual(response.status_code, 200)

        # Check Content of List View
        self.assertContains(response,self.user.username)
        # Check for Correct template used in template/SpecialArts
        self.assertTemplateUsed(response, 'SpecialArt/SpecialArt_list.html')

#--------------------------------------------------------------------------------------------#
    

    # Test SpecialArt Detail View

    def test_SpecialArtDetail_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test')
        
        # Find primary key of table
        SpecialArt_pk = SpecialArt.objects.get(SpecialArt_Description='SpecialArt_Description').pk
        
        # Get response
        response = self.client.get(reverse_lazy('SpecialArt_details',kwargs={'pk':SpecialArt_pk}))

        # Check for any invalid value
        no_response = self.client.get(reverse_lazy('SpecialArt_details',kwargs={'pk':10000}))

        # 202 for valid and 404 for invalid
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)

        # check for content of Detail Page
        self.assertContains(response,self.user.username)

        # Check for Correct template used in template/SpecialArts
        self.assertTemplateUsed(response, 'SpecialArt/SpecialArt_details.html')

#-------------------------------------------------------------------------------------------#    


    # Test SpecialArt Create View
    
    def test_SpecialArtCreate_view(self):
        # Login the user defined in SetUps
        self.client.login(username='testuser', password='test') 

        # Generate response after creating an view using Http post method
        response = self.client.post('/specialart/new/', {
        'SpecialArt_Charges_Available' : True,
        'SpecialArt_Daily_Charges':100,
        'SpecialArt_Description':'SpecialArt_Description',
        'SpecialArt_Special_Art_ID' : '13bcs0035',
        },follow = True)

        # print(response.content)
        # Check for successful response
        self.assertEqual(response.status_code, 200)
        # self.assertContains(response, False)
        self.assertContains(response, 100)
        self.assertContains(response, 'True')
        self.assertContains(response, 'SpecialArt_Description')
        self.assertContains(response, '13bcs0035')

        # # Check for correct template used in template/SpecialArts
        # self.assertTemplateUsed(response, 'SpecialArt/SpecialArt_details.html')

#---------------------------------------------------------------------------------------#


    # Test SpecialArt Update view 

    def test_SpecialArtupdate_view(self):
        # Login the user
        self.client.login(username='testuser', password='test')
        
        # Find primary key of table
        SpecialArt_pk = SpecialArt.objects.get(SpecialArt_Description='SpecialArt_Description').pk
        
        # Get response using pk on details view
        response = self.client.get(reverse_lazy('SpecialArt_details',kwargs={'pk':SpecialArt_pk}), {
        'SpecialArt_Charges_Available' : True,
        'SpecialArt_Daily_Charges':100,
        'SpecialArt_Description':'SpecialArt_Description',
        'SpecialArt_Special_Art_ID' : '13bcs0035',
        })
        # Check for successful response
        self.assertEqual(response.status_code, 200)

        # Check for correct templates
        self.assertTemplateUsed(response,'SpecialArt/SpecialArt_details.html')


#--------------------------------------------------------------------------------------------#


# Test Delete View of SpecialArt views

    def test_SpecialArtdelete_view(self):
        # Login the user
        self.client.login(username='testuser', password='test')

        #Find primary key of table
        SpecialArt_pk = SpecialArt.objects.get(SpecialArt_Description='SpecialArt_Description').pk
        
        # Get response to delete 

        response = self.client.get(reverse_lazy('SpecialArt_delete',kwargs={'pk':SpecialArt_pk}))
        # self.assertContains(response, 'Are you sure you want to delete') # THIS PART WORKS

        # Check deleted value , returns false i.e.302
        post_response = self.client.post(reverse_lazy('SpecialArt_delete',kwargs={'pk':SpecialArt_pk}))
        
        # self.assertRedirects(post_response, reverse_lazy('SpecialArt_delete',kwargs={'pk':SpecialArt_pk}), status_code=302)


        self.assertEqual(response.status_code, 200)

        # check for Correct Template Used
        self.assertTemplateUsed(response, 'SpecialArt/SpecialArt_delete.html')




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
#         response = self.client.get('/SpecialArts/1/')

#         self.assertEqual(response.status_code, 200)


#------------------------------------------------------------------------------------------------------#
    
        
#     # def test_update_page_status_code(self):
#     #     # url = reverse('SpecialArtListView')
#     #     response = self.client.get('/SpecialArts/1/')
#     #     self.assertEqual(response.status_code, 200)

#-------------------------------------------------------------------------------------------------------#

#     # def test_detail_page_status_code(self):
#     #     response = self.client.get('/{1}/')
#     #     self.assertEqual(response.status_code, 200)

#-------------------------------------------------------------------------------------------------------#

#     # def test_delete_page_status_code(self):
#     #     response = self.client.get('/{1}/delete/')
#     #     self.assertEqual(response.status_code, 200)