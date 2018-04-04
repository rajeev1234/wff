from django.test import TestCase,SimpleTestCase
from django.urls import reverse,reverse_lazy
from .models import District
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils import timezone


#  Test Class for District Application

class DistrictTest(TestCase):

########################## Model Testing ############################
  

    # District object with dummy data 
    def setUp(self):

        # dummy user for login 
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password = 'test'
        )

        self.District =  District.objects.create(

        # Fields according to defined in Model    
        District_Code = 'District_Code',
        District_Complete=True,
        District_Name='District_District_Name',
        District_Email='District_Email',
        District_Headquater='District_Headquater',
        District_Phq ='District_Phq',
        District_Phq_Email ='District_Phq_Email',
        District_Phq_Postal_Address ='District_Phq_Postal_Address',
        District_Phq_Web = 'District_Phq_Web',
        District_Police_Hqaddress = 'District_Police_Hqaddress',
        District_Postal_Address = 'District_Postal_Address',
        District_State = 'District_State',
        District_Web_Address = 'District_Web_Address',
        District_Creator=self.user, # Defined above in get_user_model
        District_Modified_Date=  timezone.now(),
        District_Created_Date =  timezone.now(),
        )

#-----------------------------------------------------------------------------------------#

    # Check redirection URL
    def test_get_absolute_url(self):
        # Redirection goes to District details
        self.assertEquals(self.District.get_absolute_url(), '/districts/1')

#-----------------------------------------------------------------------------------------#

    # Check Conent of District object created by create object query set
    def test_District_content(self):
        # Verify for each field  
        self.assertEqual(f'{self.District.District_Code}', 'District_Code')
        self.assertEqual(f'{self.District.District_Complete}', 'True')
        self.assertEqual(f'{self.District.District_Name}', 'District_District_Name')
        self.assertEqual(f'{self.District.District_Email}', 'District_Email')
        self.assertEqual(f'{self.District.District_Headquater}', 'District_Headquater')
        self.assertEqual(f'{self.District.District_Phq}', 'District_Phq')
        self.assertEqual(f'{self.District.District_Phq_Email}', 'District_Phq_Email')
        self.assertEqual(f'{self.District.District_Phq_Postal_Address}', 'District_Phq_Postal_Address')
        self.assertEqual(f'{self.District.District_Phq_Web}', 'District_Phq_Web')
        self.assertEqual(f'{self.District.District_Police_Hqaddress}', 'District_Police_Hqaddress')
        self.assertEqual(f'{self.District.District_Postal_Address}', 'District_Postal_Address')
        self.assertEqual(f'{self.District.District_State}', 'District_State')
        self.assertEqual(f'{self.District.District_Web_Address}', 'District_Web_Address')
        self.assertEqual(f'{self.District.District_Creator}', self.user.username) # Defined in SetUp

#--------------------------------------------------------------------------------------------#

# #############################   Model Test End   ###########################################







# ###############################    Views Test       ########################################

    
    # Test District List View
    
    def test_DistrictList_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test')

        # Get respomse from defined URL namespace
        response = self.client.get(reverse('District_list'))
        self.assertEqual(response.status_code, 200)

        # Check Content of List View
        self.assertContains(response,self.user.username)
        # Check for Correct template used in template/Districts
        self.assertTemplateUsed(response, 'Districts/District_list.html')

#--------------------------------------------------------------------------------------------#
    

    # Test District Detail View

    def test_DistrictDetail_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test')
        
        # Find primary key of table
        District_pk =District.objects.get(District_Name='District_District_Name').pk
        
        # Get response
        response = self.client.get(reverse_lazy('District_details',kwargs={'pk':District_pk}))

        # Check for any invalid value
        no_response = self.client.get(reverse_lazy('District_details',kwargs={'pk':10000}))

        # 202 for valid and 404 for invalid
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)

        # check for content of Detail Page

        # Check for Correct template used in template/Districts
        self.assertTemplateUsed(response, 'Districts/District_details.html')

#-------------------------------------------------------------------------------------------#    


    # Test District Create View
    
    def test_DistrictCreate_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test') 

        # Generate response after creating an view using Http post method
        response = self.client.post('/districts/new/', {
        'District_Code' : 'District_Code',
        'District_Complete' : True,
        'District_Name' : 'District_District_Name',
        'District_Email' : 'District_Email',
        'District_Headquater' : 'District_Headquater',
        'District_Phq' : 'District_Phq',
        'District_Phq_Email' : 'District_Phq_Email',
        'District_Phq_Postal_Address' : 'District_Phq_Postal_Address',
        'District_Phq_Web' : 'District_Phq_Web',
        'District_Police_Hqaddress' : 'District_Police_Hqaddress',
        'District_Postal_Address' : 'District_Postal_Address',
        'District_State' : 'District_State',
        'District_Web_Address' : 'District_Web_Address',
        'District_Creator': self.user, # Defined above in get_user_model
        })

        # print(response.content)
        # Check for successful response
        self.assertEqual(response.status_code, 200)
        # self.assertContains(response, False)
        self.assertContains(response, 'District_Code')
        self.assertContains(response, 'District_District_Name')
        self.assertContains(response, 'District_Email')
        self.assertContains(response, 'District_Headquater')
        self.assertContains(response, 'District_Phq')
        self.assertContains(response, 'District_Phq_Email')
        self.assertContains(response, 'District_Phq_Postal_Address')
        self.assertContains(response, 'District_Phq_Web')
        self.assertContains(response, 'District_Police_Hqaddress')
        self.assertContains(response, 'District_Postal_Address')
        self.assertContains(response, 'District_State')
        self.assertContains(response, 'District_Web_Address')
        self.assertContains(response, self.user.username) # Same as defined in SetUp

        # Check for correct template used in template/Districts
        self.assertTemplateUsed(response, 'Districts/District_new.html')

#---------------------------------------------------------------------------------------#


    # Test District Update view 

    def test_Districtupdate_view(self):
        # Login the user
        self.client.login(username='testuser', password='test')
        
        # Find primary key of table
        District_pk = District.objects.get(District_Code='District_Code').pk
        
        # Get response using pk on details view
        response = self.client.get(reverse_lazy('District_details',kwargs={'pk':District_pk}), {
        'District_Code' : 'District_Code',
        'District_Complete' : True,
        'District_Name' : 'District_District_Name',
        'District_Email' : 'District_Email',
        'District_Headquater' : 'District_Headquater',
        'District_Phq' : 'District_Phq',
        'District_Phq_Email' : 'District_Phq_Email',
        'District_Phq_Postal_Address' : 'District_Phq_Postal_Address',
        'District_Phq_Web' : 'District_Phq_Web',
        'District_Police_Hqaddress' : 'District_Police_Hqaddress',
        'District_Postal_Address' : 'District_Postal_Address',
        'District_State' : 'District_State',
        'District_Web_Address' : 'District_Web_Address',
        'District_Creator': self.user, # Defined above in get_user_model
        })
        # Check for successful response
        self.assertEqual(response.status_code, 200)

        # Check for correct templates
        self.assertTemplateUsed(response,'Districts/District_details.html')


#--------------------------------------------------------------------------------------------#


# Test Delete View of District views

    def test_Districtdelete_view(self):
        # Login the user
        self.client.login(username='testuser', password='test')

        # Find primary key of table
        District_pk = District.objects.get(District_Code='District_Code').pk
        
        # Get response to delete 

        response = self.client.get(reverse_lazy('District_delete',kwargs={'pk':District_pk}))
        self.assertContains(response, 'Are you sure you want to delete') # THIS PART WORKS

        # Check deleted value , returns false i.e.302
        post_response = self.client.post(reverse_lazy('District_delete',kwargs={'pk':District_pk}))
        
        # self.assertRedirects(post_response, reverse_lazy('District_delete',kwargs={'pk':District_pk}), status_code=302)


        self.assertEqual(response.status_code, 200)

        # check for Correct Template Used
        self.assertTemplateUsed(response, 'Districts/District_delete.html')




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
#         response = self.client.get('/Districts/1/')

#         self.assertEqual(response.status_code, 200)


#------------------------------------------------------------------------------------------------------#
    
        
#     # def test_update_page_status_code(self):
#     #     # url = reverse('DistrictListView')
#     #     response = self.client.get('/Districts/1/')
#     #     self.assertEqual(response.status_code, 200)

#-------------------------------------------------------------------------------------------------------#

#     # def test_detail_page_status_code(self):
#     #     response = self.client.get('/{1}/')
#     #     self.assertEqual(response.status_code, 200)

#-------------------------------------------------------------------------------------------------------#

#     # def test_delete_page_status_code(self):
#     #     response = self.client.get('/{1}/delete/')
#     #     self.assertEqual(response.status_code, 200)