from django.test import TestCase,SimpleTestCase
from django.urls import reverse,reverse_lazy
from .models import EducationInfo
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils import timezone


#  Test Class for EducationInfo Application

class EducationInfoTest(TestCase):

########################## Model Testing ############################
  

    # EducationInfo object with dummy data 
    def setUp(self):

        # dummy user for login 
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password = 'test'
        )

        self.EducationInfo =  EducationInfo.objects.create(

        # Fields according to defined in Model    
        EducationInfo_Course = 'EducationInfo_Course',
        EducationInfo_Course_Detail='EducationInfo_Course_Detail',
        EducationInfo_Institute='EducationInfo_Institute',
        EducationInfo_Passing_Year='EducationInfo_Passing_Year',
        EducationInfo_Creator=self.user, # Defined above in get_user_model
        EducationInfo_Modified_Date=  timezone.now(),
        EducationInfo_Created_Time =  timezone.now(),
        )

#-----------------------------------------------------------------------------------------#

    # Check redirection URL
    def test_get_absolute_url(self):
        # Redirection goes to EducationInfo details
        self.assertEquals(self.EducationInfo.get_absolute_url(), '/educationinfos/1')

#-----------------------------------------------------------------------------------------#

    # Check Conent of EducationInfo object created by create object query set
    def test_EducationInfo_content(self):
        # Verify for each field  
        self.assertEqual(f'{self.EducationInfo.EducationInfo_Course}', 'EducationInfo_Course')
        self.assertEqual(f'{self.EducationInfo.EducationInfo_Course_Detail}', 'EducationInfo_Course_Detail')
        self.assertEqual(f'{self.EducationInfo.EducationInfo_Institute}', 'EducationInfo_Institute')
        self.assertEqual(f'{self.EducationInfo.EducationInfo_Passing_Year}', 'EducationInfo_Passing_Year')
        self.assertEqual(f'{self.EducationInfo.EducationInfo_Creator}', self.user.username) # Defined in SetUp

#--------------------------------------------------------------------------------------------#

# #############################   Model Test End   ###########################################







# ###############################    Views Test       ########################################

    
    # Test EducationInfo List View
    
    def test_EducationInfoList_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test')

        # Get respomse from defined URL namespace
        response = self.client.get(reverse('EducationInfo_list'))
        self.assertEqual(response.status_code, 200)

        # Check Content of List View
        self.assertContains(response,self.user.username)
        # Check for Correct template used in template/EducationInfos
        self.assertTemplateUsed(response, 'EducationInfos/EducationInfo_list.html')

#--------------------------------------------------------------------------------------------#
    

    # Test EducationInfo Detail View

    def test_EducationInfoDetail_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test')
        
        # Find primary key of table
        EducationInfo_pk = EducationInfo.objects.get(EducationInfo_Course='EducationInfo_Course').pk
        
        # Get response
        response = self.client.get(reverse_lazy('EducationInfo_details',kwargs={'pk':EducationInfo_pk}))

        # Check for any invalid value
        no_response = self.client.get(reverse_lazy('EducationInfo_details',kwargs={'pk':10000}))

        # 202 for valid and 404 for invalid
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)

        # check for content of Detail Page
        self.assertContains(response, 'EducationInfo_Course')

        # Check for Correct template used in template/EducationInfos
        self.assertTemplateUsed(response, 'EducationInfos/EducationInfo_details.html')

#-------------------------------------------------------------------------------------------#    


    # Test EducationInfo Create View
    
    def test_EducationInfoCreate_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test') 

        # Generate response after creating an view using Http post method
        response = self.client.post('/educationinfos/new/', {
        'EducationInfo_Course' : 'EducationInfo_Course',
        'EducationInfo_Course_Detail':'EducationInfo_Course_Detail',
        'EducationInfo_Institute':'EducationInfo_Institute',
        'EducationInfo_Passing_Year':'EducationInfo_Passing_Year',
        'EducationInfo_Creator':self.user, # Defined above in get_user_model
        })

        # print(response.content)
        # Check for successful response
        self.assertEqual(response.status_code, 200)
        # self.assertContains(response, False)
        self.assertContains(response, 'EducationInfo_Course')
        self.assertContains(response, 'EducationInfo_Course_Detail')
        self.assertContains(response, 'EducationInfo_Institute')
        self.assertContains(response, 'EducationInfo_Passing_Year')
        self.assertContains(response, self.user.username) # Same as defined in SetUp

        # Check for correct template used in template/EducationInfos
        self.assertTemplateUsed(response, 'EducationInfos/EducationInfo_new.html')

#---------------------------------------------------------------------------------------#


    # Test EducationInfo Update view 

    def test_EducationInfoupdate_view(self):
        # Login the user
        self.client.login(username='testuser', password='test')
        
        # Find primary key of table
        EducationInfo_pk = EducationInfo.objects.get(EducationInfo_Course='EducationInfo_Course').pk
        
        # Get response using pk on details view
        response = self.client.get(reverse_lazy('EducationInfo_details',kwargs={'pk':EducationInfo_pk}), {
        'EducationInfo_Course' : 'EducationInfo_Course',
        'EducationInfo_Course_Detail':'EducationInfo_Course_Detail',
        'EducationInfo_Institute':'EducationInfo_Institute',
        'EducationInfo_Passing_Year':'EducationInfo_Passing_Year',
        'EducationInfo_Creator':self.user, # Defined above in get_user_model
        })
        # Check for successful response
        self.assertEqual(response.status_code, 200)

        # Check for correct templates
        self.assertTemplateUsed(response,'EducationInfos/EducationInfo_details.html')


#--------------------------------------------------------------------------------------------#


# Test Delete View of EducationInfo views

    def test_EducationInfodelete_view(self):
        # Login the user
        self.client.login(username='testuser', password='test')

        # Find primary key of table
        EducationInfo_pk = EducationInfo.objects.get(EducationInfo_Course='EducationInfo_Course').pk
        
        # Get response to delete 

        response = self.client.get(reverse_lazy('EducationInfo_delete',kwargs={'pk':EducationInfo_pk}))
        self.assertContains(response, 'Are you sure you want to delete') # THIS PART WORKS

        # Check deleted value , returns false i.e.302
        post_response = self.client.post(reverse_lazy('EducationInfo_delete',kwargs={'pk':EducationInfo_pk}))
        
        # self.assertRedirects(post_response, reverse_lazy('EducationInfo_delete',kwargs={'pk':EducationInfo_pk}), status_code=302)


        self.assertEqual(response.status_code, 200)

        # check for Correct Template Used
        self.assertTemplateUsed(response, 'EducationInfos/EducationInfo_delete.html')




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
#         response = self.client.get('/EducationInfos/1/')

#         self.assertEqual(response.status_code, 200)


#------------------------------------------------------------------------------------------------------#
    
        
#     # def test_update_page_status_code(self):
#     #     # url = reverse('EducationInfoListView')
#     #     response = self.client.get('/EducationInfos/1/')
#     #     self.assertEqual(response.status_code, 200)

#-------------------------------------------------------------------------------------------------------#

#     # def test_detail_page_status_code(self):
#     #     response = self.client.get('/{1}/')
#     #     self.assertEqual(response.status_code, 200)

#-------------------------------------------------------------------------------------------------------#

#     # def test_delete_page_status_code(self):
#     #     response = self.client.get('/{1}/delete/')
#     #     self.assertEqual(response.status_code, 200)