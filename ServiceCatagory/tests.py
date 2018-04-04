from django.test import TestCase,SimpleTestCase
from django.urls import reverse,reverse_lazy
from .models import ServiceCatagory
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.core.files.uploadedfile import SimpleUploadedFile


#  Test Class for ServiceCatagory Application

class ServiceCatagoryTest(TestCase):

########################## Model Testing ############################
  

    # ServiceCatagory object with dummy data 
    def setUp(self):

        # dummy user for login 
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password = 'test'
        )

        self.ServiceCatagory =  ServiceCatagory.objects.create(

        # Fields according to defined in Model    
        ServiceCatagory_Icon_Number = 334,
        ServiceCatagory_Responsibilities='ServiceCatagory_Responsibilities',
        ServiceCatagory_Service_Category='ServiceCatagory_Service_Category',
        ServiceCatagory_Users = self.user,
        ServiceCatagory_What_Do_You_Do='ServiceCatagory_What_Do_You_Do',
        )

#-----------------------------------------------------------------------------------------#

    # Check redirection URL
    def test_get_absolute_url(self):
        # Redirection goes to ServiceCatagory details
        self.assertEquals(self.ServiceCatagory.get_absolute_url(), '/servicecatagory/1')

#-----------------------------------------------------------------------------------------#

    # Check Conent of ServiceCatagory object created by create object query set
    def test_ServiceCatagory_content(self):
        # Verify for each field  
        self.assertEqual(f'{self.ServiceCatagory.ServiceCatagory_Responsibilities}', 'ServiceCatagory_Responsibilities')
        self.assertEqual(f'{self.ServiceCatagory.ServiceCatagory_Service_Category}', 'ServiceCatagory_Service_Category')
        self.assertEqual(f'{self.ServiceCatagory.ServiceCatagory_Users}', self.user.username)
        self.assertEqual(f'{self.ServiceCatagory.ServiceCatagory_What_Do_You_Do}', 'ServiceCatagory_What_Do_You_Do')
        self.assertEqual(int(self.ServiceCatagory.ServiceCatagory_Icon_Number), 334)
#--------------------------------------------------------------------------------------------#

# #############################   Model Test End   ###########################################







# ###############################    Views Test       ########################################

    
    # Test ServiceCatagory List View
    
    def test_ServiceCatagoryList_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test')

        # Get respomse from defined URL namespace
        response = self.client.get(reverse('ServiceCatagory_list'))
        self.assertEqual(response.status_code, 200)

        # Check Content of List View
        self.assertContains(response,self.user.username)
        # Check for Correct template used in template/ServiceCatagorys
        self.assertTemplateUsed(response, 'ServiceCatagory/ServiceCatagory_list.html')

#--------------------------------------------------------------------------------------------#
    

    # Test ServiceCatagory Detail View

    def test_ServiceCatagoryDetail_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test')
        
        # Find primary key of table
        ServiceCatagory_pk = ServiceCatagory.objects.get(ServiceCatagory_Responsibilities='ServiceCatagory_Responsibilities').pk
        
        # Get response
        response = self.client.get(reverse_lazy('ServiceCatagory_details',kwargs={'pk':ServiceCatagory_pk}))

        # Check for any invalid value
        no_response = self.client.get(reverse_lazy('ServiceCatagory_details',kwargs={'pk':10000}))

        # 202 for valid and 404 for invalid
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)

        # check for content of Detail Page
        self.assertContains(response,self.user.username)

        # Check for Correct template used in template/ServiceCatagorys
        self.assertTemplateUsed(response, 'ServiceCatagory/ServiceCatagory_details.html')

#-------------------------------------------------------------------------------------------#    


    # Test ServiceCatagory Create View
    
    def test_ServiceCatagoryCreate_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test') 

        # Generate response after creating an view using Http post method
        response = self.client.post('/servicecatagory/new/', {
        'ServiceCatagory_Responsibilities':'ServiceCatagory_Responsibilities',
        'ServiceCatagory_Service_Category':'ServiceCatagory_Service_Category',
        'ServiceCatagory_Users' : self.user,
        'ServiceCatagory_Icon_Number':334,
        'ServiceCatagory_What_Do_You_Do':'ServiceCatagory_What_Do_You_Do',
        })

        # print(response.content)
        # Check for successful response
        self.assertEqual(response.status_code, 200)
        # self.assertContains(response, False)
        self.assertContains(response, 'ServiceCatagory_Responsibilities')
        self.assertContains(response, 'ServiceCatagory_Service_Category')
        self.assertContains(response, 334)
        self.assertContains(response, 'ServiceCatagory_What_Do_You_Do')
        self.assertContains(response, self.user.username) # Same as defined in SetUp

        # Check for correct template used in template/ServiceCatagorys
        self.assertTemplateUsed(response, 'ServiceCatagory/ServiceCatagory_new.html')

#---------------------------------------------------------------------------------------#


    # Test ServiceCatagory Update view 

    def test_ServiceCatagoryupdate_view(self):
        # Login the user
        self.client.login(username='testuser', password='test')
        
        # Find primary key of table
        ServiceCatagory_pk = ServiceCatagory.objects.get(ServiceCatagory_Responsibilities='ServiceCatagory_Responsibilities').pk
        
        # Get response using pk on details view
        response = self.client.get(reverse_lazy('ServiceCatagory_details',kwargs={'pk':ServiceCatagory_pk}), {
        'ServiceCatagory_Responsibilities':'ServiceCatagory_Responsibilities',
        'ServiceCatagory_Service_Category':'ServiceCatagory_Service_Category',
        'ServiceCatagory_Users' : self.user.username,
        'ServiceCatagory_What_Do_You_Do':'ServiceCatagory_What_Do_You_Do',
        'ServiceCatagory_Icon_Number':334,
        })
        # Check for successful response
        self.assertEqual(response.status_code, 200)

        # Check for correct templates
        self.assertTemplateUsed(response,'ServiceCatagory/ServiceCatagory_details.html')


#--------------------------------------------------------------------------------------------#


# Test Delete View of ServiceCatagory views

    def test_ServiceCatagorydelete_view(self):
        # Login the user
        self.client.login(username='testuser', password='test')

        #Find primary key of table
        ServiceCatagory_pk = ServiceCatagory.objects.get(ServiceCatagory_Responsibilities='ServiceCatagory_Responsibilities').pk
        
        # Get response to delete 

        response = self.client.get(reverse_lazy('ServiceCatagory_delete',kwargs={'pk':ServiceCatagory_pk}))
        # self.assertContains(response, 'Are you sure you want to delete') # THIS PART WORKS

        # Check deleted value , returns false i.e.302
        post_response = self.client.post(reverse_lazy('ServiceCatagory_delete',kwargs={'pk':ServiceCatagory_pk}))
        
        # self.assertRedirects(post_response, reverse_lazy('ServiceCatagory_delete',kwargs={'pk':ServiceCatagory_pk}), status_code=302)


        self.assertEqual(response.status_code, 200)

        # check for Correct Template Used
        self.assertTemplateUsed(response, 'ServiceCatagory/ServiceCatagory_delete.html')




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
#         response = self.client.get('/ServiceCatagorys/1/')

#         self.assertEqual(response.status_code, 200)


#------------------------------------------------------------------------------------------------------#
    
        
#     # def test_update_page_status_code(self):
#     #     # url = reverse('ServiceCatagoryListView')
#     #     response = self.client.get('/ServiceCatagorys/1/')
#     #     self.assertEqual(response.status_code, 200)

#-------------------------------------------------------------------------------------------------------#

#     # def test_detail_page_status_code(self):
#     #     response = self.client.get('/{1}/')
#     #     self.assertEqual(response.status_code, 200)

#-------------------------------------------------------------------------------------------------------#

#     # def test_delete_page_status_code(self):
#     #     response = self.client.get('/{1}/delete/')
#     #     self.assertEqual(response.status_code, 200)