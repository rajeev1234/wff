from django.test import TestCase,SimpleTestCase
from django.urls import reverse,reverse_lazy
from .models import Costume
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.forms.models import model_to_dict


#  Test Class for Costume Application

class CostumeTest(TestCase):

########################## Model Testing ############################
  

    # Costume object with dummy data 
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password = 'test'
        )

        self.Costume =  Costume.objects.create(

        # Fields according to defined in Model    
        Costume_Color='Costume_Color',
        Costume_Category='Costume_Category',

        Costume_Style='Costume_Style',
        Costume_Description ='Costume_Description',
        Costume_Modification_Allowed=True,
        Costume_Trend_Year=  '2018-03-27',
        Costume_Weekly_Rent=9999,
        Costume_Type = 'Costume_Type',
        Costume_Creator=self.user, # Defined above in get_user_model
        Costume_Modified_Date=  timezone.now(),
        Costume_Created_Date =  timezone.now(),
        )

#-----------------------------------------------------------------------------------------#

    # Check redirection URL
    def test_get_absolute_url(self):
        # Redirection goes to costume details
        self.assertEquals(self.Costume.get_absolute_url(), '/costumes/1')

#-----------------------------------------------------------------------------------------#

    # Check Conent of costume object created by create object query set
    def test_Costume_content(self):
        # Verify for each field  
        self.assertEqual(f'{self.Costume.Costume_Color}', 'Costume_Color')
        self.assertEqual(f'{self.Costume.Costume_Category}', 'Costume_Category')

        self.assertEqual(f'{self.Costume.Costume_Style}', 'Costume_Style')
        self.assertEqual(f'{self.Costume.Costume_Description}', 'Costume_Description')
        self.assertEqual(bool(f'{self.Costume.Costume_Modification_Allowed}'), True)
        self.assertEqual(f'{self.Costume.Costume_Trend_Year}', '2018-03-27')
        self.assertEqual(int(self.Costume.Costume_Weekly_Rent), 9999)
        self.assertEqual(f'{self.Costume.Costume_Creator}', self.user.username) # Defined in SetUp
        self.assertEqual(f'{self.Costume.Costume_Color}', 'Costume_Color')
        self.assertEqual(f'{self.Costume.Costume_Type}', 'Costume_Type')

#--------------------------------------------------------------------------------------------#

# #############################   Model Test End   ###########################################







# ###############################    Views Test       ########################################

    
    # Test Costume List View
    
    def test_CostumeList_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test')

        # Get respomse from defined URL namespace
        response = self.client.get(reverse('Costume_list'))
        self.assertEqual(response.status_code, 200)

        # Check Content of List View
        self.assertContains(response,self.user.username)
        self.assertContains(response,'Costume_Style')

        # Check for Correct template used in template/Costumes
        self.assertTemplateUsed(response, 'Costumes/Costume_list.html')

#--------------------------------------------------------------------------------------------#
    

    # Test Costume Detail View

    def test_CostumeDetail_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test')
        
        # Find primary key of table
        Costume_pk = Costume.objects.get(Costume_Color='Costume_Color').pk
        
        # Get response
        response = self.client.get(reverse_lazy('Costume_details',kwargs={'pk':Costume_pk}))

        # Check for any invalid value
        no_response = self.client.get(reverse_lazy('Costume_details',kwargs={'pk':10000}))

        # 202 for valid and 404 for invalid
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)

        # check for content of Detail Page


        # Check for Correct template used in template/Costumes
        self.assertTemplateUsed(response, 'Costumes/Costume_details.html')

#-------------------------------------------------------------------------------------------#    


    # Test Costume Create View
    
    def test_CostumeCreate_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test') 

        # Generate response after creating an view using Http post method
        response = self.client.post('/costumes/new/', {
        'Costume_Color':'Costume_Color',
        'Costume_Category':'Costume_Category',

        'Costume_Style':'Costume_Style',
        'Costume_Description':'Costume_Description',
        'Costume_Modification_Allowed':True,
        'Costume_Trend_Year':'2018-03-25',
        'Costume_Weekly_Rent':9999,
        'Costume_Creator':self.user, #Defined in setup
        'Costume_Modified_Date': timezone.now(),
        'Costume_Created_Date' :  timezone.now(),
        })
        
        # Check for successful response
        self.assertEqual(response.status_code, 200)

        # Check response values
        self.assertContains(response, 'Costume_Color')
        self.assertContains(response, 'Costume_Category')

        self.assertContains(response, 'Costume_Style')
        self.assertContains(response, 'Costume_Description')
        self.assertContains(response, 'checked')
        self.assertContains(response, '2018-03-25')
        self.assertContains(response, 9999)
        self.assertContains(response, self.user.username) # Same as defined in SetUp

        # Check for correct template used in template/Costumes
        self.assertTemplateUsed(response, 'Costumes/Costume_new.html')

#---------------------------------------------------------------------------------------#


    # Test Costume Update view 

    def test_Costumeupdate_view(self):
        # Login the user
        self.client.login(username='testuser', password='test')
        
        # Find primary key of table
        Costume_pk = Costume.objects.get(Costume_Color='Costume_Color').pk
        
        # Get response using pk on details view
        response = self.client.get(reverse_lazy('Costume_details',kwargs={'pk':Costume_pk}), {
        'Costume_Color':'Costume_Color',
        'Costume_Category':'Costume_Category',

        'Costume_Style':'Costume_Style',
        'Costume_Description':'Costume_Description',
        'Costume_Modification_Allowed':True,
        'Costume_Trend_Year':'2018-03-25',
        'Costume_Weekly_Rent':9999,
        'Costume_Creator':self.user.username,
        'Costume_Modified_Date': timezone.now(),
        'Costume_Created_Date' :  timezone.now(),
        })
        # Check for successful response
        self.assertEqual(response.status_code, 200)

        # Check for correct templates
        self.assertTemplateUsed(response,'Costumes/Costume_details.html')


#--------------------------------------------------------------------------------------------#


# Test Delete View of Costume views

    def test_Costumedelete_view(self):
        # Login the user
        self.client.login(username='testuser', password='test')

        # Find primary key of table
        Costume_pk = Costume.objects.get(Costume_Color='Costume_Color').pk
        
        # Get response to delete 

        response = self.client.get(reverse_lazy('Costume_delete',kwargs={'pk':Costume_pk}))
        self.assertContains(response, 'Are you sure you want to delete') # THIS PART WORKS

        # Check deleted value , returns false i.e.302
        post_response = self.client.post(reverse_lazy('Costume_delete',kwargs={'pk':Costume_pk}))
        
        # self.assertRedirects(post_response, reverse_lazy('Costume_delete',kwargs={'pk':Costume_pk}), status_code=302)


        self.assertEqual(response.status_code, 200)

        # check for Correct Template Used
        self.assertTemplateUsed(response, 'Costumes/Costume_delete.html')




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
#         response = self.client.get('/costumes/1/')

#         self.assertEqual(response.status_code, 200)


#------------------------------------------------------------------------------------------------------#
    
        
#     # def test_update_page_status_code(self):
#     #     # url = reverse('CostumeListView')
#     #     response = self.client.get('/costumes/1/')
#     #     self.assertEqual(response.status_code, 200)

#-------------------------------------------------------------------------------------------------------#

#     # def test_detail_page_status_code(self):
#     #     response = self.client.get('/{1}/')
#     #     self.assertEqual(response.status_code, 200)

#-------------------------------------------------------------------------------------------------------#

#     # def test_delete_page_status_code(self):
#     #     response = self.client.get('/{1}/delete/')
#     #     self.assertEqual(response.status_code, 200)