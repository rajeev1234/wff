from django.test import TestCase,SimpleTestCase
from django.urls import reverse,reverse_lazy
from .models import Dancer
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils import timezone


#  Test Class for Dancer Application

class DancerTest(TestCase):

########################## Model Testing ############################
  

    # Dancer object with dummy data 
    def setUp(self):

        # dummy user for login 
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password = 'test'
        )

        self.Dancer =  Dancer.objects.create(

        # Fields according to defined in Model    
        Dancer_Charges_Available=True,
        Dancer_Daily_Charges='Dancer_Daily_Charges',
        Dancer_Dancing_Style='Dancer_Dancing_Style',
        Dancer_Description ='Dancer_Description',
        Dancer_Genre='Dancer_Genre',
        Dancer_Creator=self.user, # Defined above in get_user_model
        Dancer_Modified_Date=  timezone.now(),
        Dancer_Created_Date =  timezone.now(),
        )

#-----------------------------------------------------------------------------------------#

    # Check redirection URL
    def test_get_absolute_url(self):
        # Redirection goes to Dancer details
        self.assertEquals(self.Dancer.get_absolute_url(), '/dancers/1')

#-----------------------------------------------------------------------------------------#

    # Check Conent of Dancer object created by create object query set
    def test_Dancer_content(self):
        # Verify for each field  
        self.assertEqual(f'{self.Dancer.Dancer_Charges_Available}', 'True')
        self.assertEqual(f'{self.Dancer.Dancer_Daily_Charges}', 'Dancer_Daily_Charges')
        self.assertEqual(f'{self.Dancer.Dancer_Dancing_Style}', 'Dancer_Dancing_Style')
        self.assertEqual(f'{self.Dancer.Dancer_Description}', 'Dancer_Description')
        self.assertEqual(f'{self.Dancer.Dancer_Genre}', 'Dancer_Genre')
        self.assertEqual(f'{self.Dancer.Dancer_Creator}', self.user.username) # Defined in SetUp

#--------------------------------------------------------------------------------------------#

# #############################   Model Test End   ###########################################







# ###############################    Views Test       ########################################

    
    # Test Dancer List View
    
    def test_DancerList_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test')

        # Get respomse from defined URL namespace
        response = self.client.get(reverse('Dancer_list'))
        self.assertEqual(response.status_code, 200)

        # Check Content of List View
        self.assertContains(response,self.user.username)
        # Check for Correct template used in template/Dancers
        self.assertTemplateUsed(response, 'Dancers/Dancer_list.html')

#--------------------------------------------------------------------------------------------#
    

    # Test Dancer Detail View

    def test_DancerDetail_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test')
        
        # Find primary key of table
        Dancer_pk = Dancer.objects.get(Dancer_Description='Dancer_Description').pk
        
        # Get response
        response = self.client.get(reverse_lazy('Dancer_details',kwargs={'pk':Dancer_pk}))

        # Check for any invalid value
        no_response = self.client.get(reverse_lazy('Dancer_details',kwargs={'pk':10000}))

        # 202 for valid and 404 for invalid
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)

        # check for content of Detail Page
        self.assertContains(response, 'Dancer_Description')

        # Check for Correct template used in template/Dancers
        self.assertTemplateUsed(response, 'Dancers/Dancer_details.html')

#-------------------------------------------------------------------------------------------#    


    # Test Dancer Create View
    
    def test_DancerCreate_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test') 

        # Generate response after creating an view using Http post method
        response = self.client.post('/dancers/new/', {
        'Dancer_Charges_Available':False,
        'Dancer_Daily_Charges':'Dancer_Dailycharges11',
        'Dancer_Dancing_Style':'Dancer_Dancing_style',
        'Dancer_Description' :'Dancer_Description',
        'Dancer_Genre':'Dancer_Genre',
        'Dancer_Creator':self.user, # Defined above in get_user_model
        'Dancer_Modified_Date':  timezone.now(),
        'Dancer_Created_Date' :  timezone.now(),
        })

        # Check for successful response
        self.assertEqual(response.status_code, 200)
        # self.assertContains(response, False)
        self.assertContains(response, 'Dancer_Dailycharges11')
        self.assertContains(response, 'Dancer_Dancing_style')
        self.assertContains(response, 'Dancer_Description')
        self.assertContains(response, 'Dancer_Genre')
        self.assertContains(response, self.user.username) # Same as defined in SetUp

        # Check for correct template used in template/Dancers
        self.assertTemplateUsed(response, 'Dancers/Dancer_new.html')

#---------------------------------------------------------------------------------------#


    # Test Dancer Update view 

    def test_Dancerupdate_view(self):
        # Login the user
        self.client.login(username='testuser', password='test')
        
        # Find primary key of table
        Dancer_pk = Dancer.objects.get(Dancer_Description='Dancer_Description').pk
        
        # Get response using pk on details view
        response = self.client.get(reverse_lazy('Dancer_details',kwargs={'pk':Dancer_pk}), {
        'Dancer_Charges_Available':True,
        'Dancer_Daily_Charges':'Dancer_Daily_Charges',
        'Dancer_Dancing_Style':'Dancer_Dancing_Style',
        'Dancer_Description' :'Dancer_Description',
        'Dancer_Genre':'Dancer_Genre',
        'Dancer_Creator':self.user, # Defined above in get_user_model
        'Dancer_Modified_Date':  timezone.now(),
        'Dancer_Created_Date' :  timezone.now(),
        })
        # Check for successful response
        self.assertEqual(response.status_code, 200)

        # Check for correct templates
        self.assertTemplateUsed(response,'Dancers/Dancer_details.html')


#--------------------------------------------------------------------------------------------#


# Test Delete View of Dancer views

    def test_Dancerdelete_view(self):
        # Login the user
        self.client.login(username='testuser', password='test')

        # Find primary key of table
        Dancer_pk = Dancer.objects.get(Dancer_Description='Dancer_Description').pk
        
        # Get response to delete 

        response = self.client.get(reverse_lazy('Dancer_delete',kwargs={'pk':Dancer_pk}))
        self.assertContains(response, 'Are you sure you want to delete') # THIS PART WORKS

        # Check deleted value , returns false i.e.302
        post_response = self.client.post(reverse_lazy('Dancer_delete',kwargs={'pk':Dancer_pk}))
        
        # self.assertRedirects(post_response, reverse_lazy('Dancer_delete',kwargs={'pk':Dancer_pk}), status_code=302)


        self.assertEqual(response.status_code, 200)

        # check for Correct Template Used
        self.assertTemplateUsed(response, 'Dancers/Dancer_delete.html')




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
#         response = self.client.get('/Dancers/1/')

#         self.assertEqual(response.status_code, 200)


#------------------------------------------------------------------------------------------------------#
    
        
#     # def test_update_page_status_code(self):
#     #     # url = reverse('DancerListView')
#     #     response = self.client.get('/Dancers/1/')
#     #     self.assertEqual(response.status_code, 200)

#-------------------------------------------------------------------------------------------------------#

#     # def test_detail_page_status_code(self):
#     #     response = self.client.get('/{1}/')
#     #     self.assertEqual(response.status_code, 200)

#-------------------------------------------------------------------------------------------------------#

#     # def test_delete_page_status_code(self):
#     #     response = self.client.get('/{1}/delete/')
#     #     self.assertEqual(response.status_code, 200)