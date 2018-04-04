from django.test import TestCase,SimpleTestCase
from django.urls import reverse,reverse_lazy
from .models import FilmProjectForPermit
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils import timezone


#  Test Class for FilmProjectForPermit Application

class FilmProjectForPermitTest(TestCase):

########################## Model Testing ############################
  

    # FilmProjectForPermit object with dummy data 
    def setUp(self):

        # dummy user for login 
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password = 'test'
        )

        self.FilmProjectForPermit =  FilmProjectForPermit.objects.create(

        # Fields according to defined in Model    
        FilmProjectForPermit_Category = 'FilmProjectForPermit_Category',
        FilmProjectForPermit_Crew_Size='FilmProjectForPermit_CrewSize',
        FilmProjectForPermit_Project_Name='FilmProjectForPermit_Project_Name',
        FilmProjectForPermit_ScriptasFile='FilmProjectForPermit_ScriptasFile',
        FilmProjectForPermit_Synopsis='FilmProjectForPermit_Synopsis',
        FilmProjectForPermit_Title='FilmProjectForPermit_Title',
        FilmProjectForPermit_Creator=self.user,
        FilmProjectForPermit_Modified_Date=  timezone.now(),
        FilmProjectForPermit_Created_Date =  timezone.now(),
        )

#-----------------------------------------------------------------------------------------#

    # Check redirection URL
    def test_get_absolute_url(self):
        # Redirection goes to FilmProjectForPermit details
        self.assertEquals(self.FilmProjectForPermit.get_absolute_url(), '/filmprojectforpermit/1')

#-----------------------------------------------------------------------------------------#

    # Check Conent of FilmProjectForPermit object created by create object query set
    def test_FilmProjectForPermit_content(self):
        # Verify for each field  
        self.assertEqual(f'{self.FilmProjectForPermit.FilmProjectForPermit_Category}', 'FilmProjectForPermit_Category')
        self.assertEqual(f'{self.FilmProjectForPermit.FilmProjectForPermit_Crew_Size}', 'FilmProjectForPermit_CrewSize')
        self.assertEqual(f'{self.FilmProjectForPermit.FilmProjectForPermit_Project_Name}', 'FilmProjectForPermit_Project_Name')
        self.assertEqual(f'{self.FilmProjectForPermit.FilmProjectForPermit_ScriptasFile}', 'FilmProjectForPermit_ScriptasFile')
        self.assertEqual(f'{self.FilmProjectForPermit.FilmProjectForPermit_Synopsis}', 'FilmProjectForPermit_Synopsis')
        self.assertEqual(f'{self.FilmProjectForPermit.FilmProjectForPermit_Title}', 'FilmProjectForPermit_Title')
        self.assertEqual(f'{self.FilmProjectForPermit.FilmProjectForPermit_Creator}', self.user.username)
#--------------------------------------------------------------------------------------------#

# #############################   Model Test End   ###########################################







# ###############################    Views Test       ########################################

    
    # Test FilmProjectForPermit List View
    
    def test_FilmProjectForPermitList_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test')

        # Get respomse from defined URL namespace
        response = self.client.get(reverse('FilmProjectForPermit_list'))
        self.assertEqual(response.status_code, 200)

        # Check Content of List View
        self.assertContains(response,self.user.username)
        # Check for Correct template used in template/FilmProjectForPermits
        self.assertTemplateUsed(response, 'FilmProjectForPermits/FilmProjectForPermit_list.html')

#--------------------------------------------------------------------------------------------#
    

    # Test FilmProjectForPermit Detail View

    def test_FilmProjectForPermitDetail_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test')
        
        # Find primary key of table
        FilmProjectForPermit_pk = FilmProjectForPermit.objects.get(FilmProjectForPermit_Project_Name='FilmProjectForPermit_Project_Name').pk
        
        # Get response
        response = self.client.get(reverse_lazy('FilmProjectForPermit_details',kwargs={'pk':FilmProjectForPermit_pk}))

        # Check for any invalid value
        no_response = self.client.get(reverse_lazy('FilmProjectForPermit_details',kwargs={'pk':10000}))

        # 202 for valid and 404 for invalid
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)

        # check for content of Detail Page
        self.assertContains(response,self.user.username)

        # Check for Correct template used in template/FilmProjectForPermits
        self.assertTemplateUsed(response, 'FilmProjectForPermits/FilmProjectForPermit_details.html')

#-------------------------------------------------------------------------------------------#    


    # Test FilmProjectForPermit Create View
    
    def test_FilmProjectForPermitCreate_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test') 

        # Generate response after creating an view using Http post method
        response = self.client.post('/filmprojectforpermit/new/', {
        'FilmProjectForPermit_Category': 'FilmProjectForPermit_Category',
        'FilmProjectForPermit_Crew_Size':'FilmProjectForPermit_CrewSize',
        'FilmProjectForPermit_Project_Name':'FilmProjectForPermit_Project_Name',
        'FilmProjectForPermit_ScriptasFile':'FilmProjectForPermit_ScriptasFile',
        'FilmProjectForPermit_Synopsis':'FilmProjectForPermit_Synopsis',
        'FilmProjectForPermit_Title':'FilmProjectForPermit_Title',
        'FilmProjectForPermit_Creator':self.user,
        })

        # print(response.content)
        # Check for successful response
        self.assertEqual(response.status_code, 200)
        # self.assertContains(response, False)
        self.assertContains(response, 'FilmProjectForPermit_Category')
        self.assertContains(response, 'FilmProjectForPermit_CrewSize')
        self.assertContains(response, 'FilmProjectForPermit_Project_Name')
        self.assertContains(response, 'FilmProjectForPermit_ScriptasFile')
        self.assertContains(response, 'FilmProjectForPermit_Synopsis')
        self.assertContains(response, 'FilmProjectForPermit_Title')
        self.assertContains(response, self.user.username) # Same as defined in SetUp

        # Check for correct template used in template/FilmProjectForPermits
        self.assertTemplateUsed(response, 'FilmProjectForPermits/FilmProjectForPermit_new.html')

#---------------------------------------------------------------------------------------#


    # Test FilmProjectForPermit Update view 

    def test_FilmProjectForPermitupdate_view(self):
        # Login the user
        self.client.login(username='testuser', password='test')
        
        # Find primary key of table
        FilmProjectForPermit_pk = FilmProjectForPermit.objects.get(FilmProjectForPermit_Project_Name='FilmProjectForPermit_Project_Name').pk
        
        # Get response using pk on details view
        response = self.client.get(reverse_lazy('FilmProjectForPermit_details',kwargs={'pk':FilmProjectForPermit_pk}), {
        'FilmProjectForPermit_Category': 'FilmProjectForPermit_Category',
        'FilmProjectForPermit_CrewSize':'FilmProjectForPermit_CrewSize',
        'FilmProjectForPermit_Project_Name':'FilmProjectForPermit_Project_Name',
        'FilmProjectForPermit_ScriptasFile':'FilmProjectForPermit_ScriptasFile',
        'FilmProjectForPermit_Synopsis':'FilmProjectForPermit_Synopsis',
        'FilmProjectForPermit_Title':'FilmProjectForPermit_Title',
        'FilmProjectForPermit_Creator':self.user,
        })
        # Check for successful response
        self.assertEqual(response.status_code, 200)

        # Check for correct templates
        self.assertTemplateUsed(response,'FilmProjectForPermits/FilmProjectForPermit_details.html')


#--------------------------------------------------------------------------------------------#


# Test Delete View of FilmProjectForPermit views

    def test_FilmProjectForPermitdelete_view(self):
        # Login the user
        self.client.login(username='testuser', password='test')

        #Find primary key of table
        FilmProjectForPermit_pk = FilmProjectForPermit.objects.get(FilmProjectForPermit_Category='FilmProjectForPermit_Category').pk
        
        # Get response to delete 

        response = self.client.get(reverse_lazy('FilmProjectForPermit_delete',kwargs={'pk':FilmProjectForPermit_pk}))
        # self.assertContains(response, 'Are you sure you want to delete') # THIS PART WORKS

        # Check deleted value , returns false i.e.302
        post_response = self.client.post(reverse_lazy('FilmProjectForPermit_delete',kwargs={'pk':FilmProjectForPermit_pk}))
        
        # self.assertRedirects(post_response, reverse_lazy('FilmProjectForPermit_delete',kwargs={'pk':FilmProjectForPermit_pk}), status_code=302)


        self.assertEqual(response.status_code, 200)

        # check for Correct Template Used
        self.assertTemplateUsed(response, 'FilmProjectForPermits/FilmProjectForPermit_delete.html')




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
#         response = self.client.get('/FilmProjectForPermits/1/')

#         self.assertEqual(response.status_code, 200)


#------------------------------------------------------------------------------------------------------#
    
        
#     # def test_update_page_status_code(self):
#     #     # url = reverse('FilmProjectForPermitListView')
#     #     response = self.client.get('/FilmProjectForPermits/1/')
#     #     self.assertEqual(response.status_code, 200)

#-------------------------------------------------------------------------------------------------------#

#     # def test_detail_page_status_code(self):
#     #     response = self.client.get('/{1}/')
#     #     self.assertEqual(response.status_code, 200)

#-------------------------------------------------------------------------------------------------------#

#     # def test_delete_page_status_code(self):
#     #     response = self.client.get('/{1}/delete/')
#     #     self.assertEqual(response.status_code, 200)