from django.test import TestCase,SimpleTestCase
from django.urls import reverse,reverse_lazy
from .models import ServiceSubcatagory
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.core.files.uploadedfile import SimpleUploadedFile


#  Test Class for ServiceSubcatagory Application

class ServiceSubcatagoryTest(TestCase):

########################## Model Testing ############################
  

    # ServiceSubcatagory object with dummy data 
    def setUp(self):

        # dummy user for login 
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password = 'test'
        )

        self.ServiceSubcatagory =  ServiceSubcatagory.objects.create(

        # Fields according to defined in Model    
        Service_Subcatagory_Name = "Service_Subcatagory_Name",
        )

#-----------------------------------------------------------------------------------------#

    # Check redirection URL
    def test_get_absolute_url(self):
        # Redirection goes to ServiceSubcatagory details
        self.assertEquals(self.ServiceSubcatagory.get_absolute_url(), '/servicesubcatagory/1')

#-----------------------------------------------------------------------------------------#

    # Check Conent of ServiceSubcatagory object created by create object query set
    def test_ServiceSubcatagory_content(self):
        # Verify for each field  
        self.assertEqual(f'{self.ServiceSubcatagory.Service_Subcatagory_Name}', 'Service_Subcatagory_Name')
#--------------------------------------------------------------------------------------------#

# #############################   Model Test End   ###########################################







# ###############################    Views Test       ########################################

    
    # Test ServiceSubcatagory List View
    
    def test_ServiceSubcatagoryList_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test')

        # Get respomse from defined URL namespace
        response = self.client.get(reverse('ServiceSubcatagory_list'))
        self.assertEqual(response.status_code, 200)

        # Check Content of List View
        self.assertContains(response,self.user.username)
        # Check for Correct template used in template/ServiceSubcatagorys
        self.assertTemplateUsed(response, 'ServiceSubcatagory/ServiceSubcatagory_list.html')

#--------------------------------------------------------------------------------------------#
    

    # Test ServiceSubcatagory Detail View

    def test_ServiceSubcatagoryDetail_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test')
        
        # Find primary key of table
        ServiceSubcatagory_pk = ServiceSubcatagory.objects.get(Service_Subcatagory_Name='Service_Subcatagory_Name').pk
        
        # Get response
        response = self.client.get(reverse_lazy('ServiceSubcatagory_details',kwargs={'pk':ServiceSubcatagory_pk}))

        # Check for any invalid value
        no_response = self.client.get(reverse_lazy('ServiceSubcatagory_details',kwargs={'pk':10000}))

        # 202 for valid and 404 for invalid
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)

        # check for content of Detail Page
        self.assertContains(response,self.user.username)

        # Check for Correct template used in template/ServiceSubcatagorys
        self.assertTemplateUsed(response, 'ServiceSubcatagory/ServiceSubcatagory_details.html') 

#-------------------------------------------------------------------------------------------#    


    # Test ServiceSubcatagory Create View
    
    def test_ServiceSubcatagoryCreate_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test')

        # Generate response after creating an view using Http post method
        
        ''' Here post request doesnot return correct response content of no reason. 
            So by enabling follow = True we send the request to the ultimate destination page,
            i.e. details page which comes after submitting the form on new page.
            Response of the details page comes out to be correct and true .'''
        response = self.client.post('/servicesubcatagory/new/', {
        'Service_Subcatagory_Name':"javfsd"
        },follow = True)


        # print(response.content)
        # Check for successful response
        self.assertEqual(response.status_code, 200)

        self.assertContains(response, 'javfsd')

        # Template of destination page after submitting the page
        self.assertTemplateUsed(response, 'ServiceSubcatagory/ServiceSubcatagory_details.html')

#---------------------------------------------------------------------------------------#


    # Test ServiceSubcatagory Update view 

    def test_ServiceSubcatagoryupdate_view(self):
        # Login the user
        self.client.login(username='testuser', password='test')
        
        # Find primary key of table
        ServiceSubcatagory_pk = ServiceSubcatagory.objects.get(Service_Subcatagory_Name='Service_Subcatagory_Name').pk
        
        # Get response using pk on details view
        response = self.client.get(reverse_lazy('ServiceSubcatagory_details',kwargs={'pk':ServiceSubcatagory_pk}), {
        'Service_Subcatagory_Name':'Service_Subcatagory_Name',
        })
        # Check for successful response
        self.assertEqual(response.status_code, 200)

        # Check for correct templates
        self.assertTemplateUsed(response,'ServiceSubcatagory/ServiceSubcatagory_details.html')


#--------------------------------------------------------------------------------------------#


# Test Delete View of ServiceSubcatagory views

    def test_ServiceSubcatagorydelete_view(self):
        # Login the user
        self.client.login(username='testuser', password='test')

        #Find primary key of table
        ServiceSubcatagory_pk = ServiceSubcatagory.objects.get(Service_Subcatagory_Name='Service_Subcatagory_Name').pk
        
        # Get response to delete 

        response = self.client.get(reverse_lazy('ServiceSubcatagory_delete',kwargs={'pk':ServiceSubcatagory_pk}))
        # self.assertContains(response, 'Are you sure you want to delete') # THIS PART WORKS

        # Check deleted value , returns false i.e.302
        post_response = self.client.post(reverse_lazy('ServiceSubcatagory_delete',kwargs={'pk':ServiceSubcatagory_pk}))
        
        # self.assertRedirects(post_response, reverse_lazy('ServiceSubcatagory_delete',kwargs={'pk':ServiceSubcatagory_pk}), status_code=302)


        self.assertEqual(response.status_code, 200)

        # check for Correct Template Used
        self.assertTemplateUsed(response, 'ServiceSubcatagory/ServiceSubcatagory_delete.html')




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
#         response = self.client.get('/ServiceSubcatagorys/1/')

#         self.assertEqual(response.status_code, 200)


#------------------------------------------------------------------------------------------------------#
    
        
#     # def test_update_page_status_code(self):
#     #     # url = reverse('ServiceSubcatagoryListView')
#     #     response = self.client.get('/ServiceSubcatagorys/1/')
#     #     self.assertEqual(response.status_code, 200)

#-------------------------------------------------------------------------------------------------------#

#     # def test_detail_page_status_code(self):
#     #     response = self.client.get('/{1}/')
#     #     self.assertEqual(response.status_code, 200)

#-------------------------------------------------------------------------------------------------------#

#     # def test_delete_page_status_code(self):
#     #     response = self.client.get('/{1}/delete/')
#     #     self.assertEqual(response.status_code, 200)