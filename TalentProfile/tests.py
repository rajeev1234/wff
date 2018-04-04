from django.test import TestCase,SimpleTestCase
from django.urls import reverse,reverse_lazy
from .models import TalentProfile
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils import timezone


#  Test Class for TalentProfile Application

# class TalentProfileTest(TestCase):

# ########################## Model Testing ####   ########################
  

#     # TalentProfile object with dummy data 
#     def setUp(self):

#         # dummy user for login 
#         self.user = get_user_model().objects.create_user(
#             username='testuser',
#             email='test@email.com',
#             password = 'test'
#         )

#         # self.TalentProfile =  TalentProfile.objects.create(

#         # # Fields according to defined in Model    
#         # TalentProfile_Amount = 199,
#         # TalentProfile_End_Date = timezone.now(),
#         # TalentProfile_FOR_FILM_COIN = 1000,
#         # TalentProfile_Openings_Allowed = True,
#         # TalentProfile_Location_Allowed = True,
#         # TalentProfile_Pitch_Allowed = True,
#         # TalentProfile_Pitch_Box_Capacity_Image_per_pitch = 111,
#         # TalentProfile_Start_Date = timezone.now(),
#         # TalentProfile_Type = 'TalentProfile_Type',
#         # TalentProfile_User_ID = self.user,
#         # )

# #-----------------------------------------------------------------------------------------#

#     # Check redirection URL
#     def test_get_absolute_url(self):
#         # Redirection goes to TalentProfile details
#         self.assertEquals(self.TalentProfile.get_absolute_url(), '/talentprofile/1')

# #-----------------------------------------------------------------------------------------#

#     # Check Conent of TalentProfile object created by create object query set
#     def test_TalentProfile_content(self):
#         # Verify for each field  
#         # self.assertEqual(int(f'{self.TalentProfile.TalentProfile_Amount}'), 199)
#         # self.assertEqual(int(f'{self.TalentProfile.TalentProfile_FOR_FILM_COIN}'), 1000)
#         # self.assertEqual(bool(f'{self.TalentProfile.TalentProfile_Openings_Allowed}'), True)
#         # self.assertEqual(bool(f'{self.TalentProfile.TalentProfile_Location_Allowed}'), True)
#         # self.assertEqual(bool(f'{self.TalentProfile.TalentProfile_Pitch_Allowed}'), True)
#         # self.assertEqual(int(f'{self.TalentProfile.TalentProfile_Pitch_Box_Capacity_Image_per_pitch}'), 111)
#         # self.assertEqual(f'{self.TalentProfile.TalentProfile_Type}', 'TalentProfile_Type')
#         # self.assertEqual(f'{self.TalentProfile.TalentProfile_User_ID}', self.user.username)
# #--------------------------------------------------------------------------------------------#

# # #############################   Model Test End   ###########################################







# # ###############################    Views Test       ########################################

    
#     # Test TalentProfile List View
#     def test_TalentProfileList_view(self):
#         # Login the user defined in SetUp
#         # self.client.login(username='testuser', password='test')

#         # # Get respomse from defined URL namespace
#         # response = self.client.get(reverse('TalentProfile_list'))
#         # self.assertEqual(response.status_code, 200)

#         # # Check Content of List View
#         # self.assertContains(response,199)
#         # self.assertContains(response,'TalentProfile_Type')
#         # # Check for Correct template used in template/TalentProfiles
#         # self.assertTemplateUsed(response, 'TalentProfiles/TalentProfile_list.html')

# #--------------------------------------------------------------------------------------------#
    

#     # Test TalentProfile Detail View

#     def test_TalentProfileDetail_view(self):
#         # Login the user defined in SetUp
#         # self.client.login(username='testuser', password='test')
        
#         # # Find primary key of table
#         # TalentProfile_pk = TalentProfile.objects.get(TalentProfile_Amount=199).pk
        
#         # # Get response
#         # response = self.client.get(reverse_lazy('TalentProfile_details',kwargs={'pk':TalentProfile_pk}))

#         # # Check for any invalid value
#         # no_response = self.client.get(reverse_lazy('TalentProfile_details',kwargs={'pk':10000}))

#         # # 202 for valid and 404 for invalid
#         # self.assertEqual(response.status_code, 200)
#         # self.assertEqual(no_response.status_code, 404)

#         # # check for content of Detail Page
#         # self.assertContains(response,self.user.username)

#         # # Check for Correct template used in template/TalentProfiles
#          # self.assertTemplateUsed(response, 'TalentProfiles/TalentProfile_details.html')

# #-------------------------------------------------------------------------------------------#    


#     # Test TalentProfile Create View
    
#     def test_TalentProfileCreate_view(self):
#         # Login the user defined in SetUps
#         self.client.login(username='testuser', password='test') 

#         # Generate response after creating an view using Http post method
#         # response = self.client.post('/TalentProfile/new/', {
#         # 'TalentProfile_Amount' : 199,
#         # 'TalentProfile_End_Date' : timezone.now(),
#         # 'TalentProfile_FOR_FILM_COIN' : 1000,
#         # 'TalentProfile_Openings_Allowed' : True,
#         # 'TalentProfile_Location_Allowed' : True,
#         # 'TalentProfile_Pitch_Allowed' : True,
#         # 'TalentProfile_Pitch_Box_Capacity_Image_per_pitch' : 111,
#         # 'TalentProfile_Start_Date' : timezone.now(),
#         # 'TalentProfile_Type' : 'TalentProfile_Type',
#         # 'TalentProfile_User_ID' : self.user,
#         # })

#         # print(response.content)
#         # Check for successful response
#         # self.assertEqual(response.status_code, 200)
#         # self.assertContains(response, 'TalentProfile_Type')
#         # self.assertContains(response, self.user.username)
#         # self.assertContains(response, 'checked')
#         # self.assertContains(response, 111)
#         # self.assertContains(response, 1000)
#         # self.assertContains(response, 199)


#         # Check for correct template used in template/TalentProfiles
#         # self.assertTemplateUsed(response, 'TalentProfiles/TalentProfile_new.html')

# #---------------------------------------------------------------------------------------#


#     # Test TalentProfile Update view 

#     def test_TalentProfileupdate_view(self):
#         # Login the user
#         self.client.login(username='testuser', password='test')
        
#         # Find primary key of table
#         # TalentProfile_pk = TalentProfile.objects.get(TalentProfile_Type='TalentProfile_Type').pk
        
#         # # Get response using pk on details view
#         # response = self.client.get(reverse_lazy('TalentProfile_details',kwargs={'pk':TalentProfile_pk}), {
#         # 'TalentProfile_Amount' : 199,
#         # 'TalentProfile_End_Date' : timezone.now(),
#         # 'TalentProfile_FOR_FILM_COIN' : 1000,
#         # 'TalentProfile_Openings_Allowed' : True,
#         # 'TalentProfile_Location_Allowed' : True,
#         # 'TalentProfile_Pitch_Allowed' : True,
#         # 'TalentProfile_Pitch_Box_Capacity_Image_per_pitch' : 111,
#         # 'TalentProfile_Start_Date' : timezone.now(),
#         # 'TalentProfile_Type' : 'TalentProfile_Type',
#         # 'TalentProfile_User_ID' : self.user,
#         # })
#         # Check for successful response
#         # self.assertEqual(response.status_code, 200)

#         # # Check for correct templates
#         # self.assertTemplateUsed(response,'TalentProfiles/TalentProfile_details.html')


# #--------------------------------------------------------------------------------------------#


# # Test Delete View of TalentProfile views

#     def test_TalentProfiledelete_view(self):
#         # Login the user
#         self.client.login(username='testuser', password='test')

#         # #Find primary key of table
#         # TalentProfile_pk = TalentProfile.objects.get(TalentProfile_Type='TalentProfile_Type').pk
        
#         # # Get response to delete 

#         # response = self.client.get(reverse_lazy('TalentProfile_delete',kwargs={'pk':TalentProfile_pk}))
#         # # self.assertContains(response, 'Are you sure you want to delete') # THIS PART WORKS

#         # # Check deleted value , returns false i.e.302
#         # post_response = self.client.post(reverse_lazy('TalentProfile_delete',kwargs={'pk':TalentProfile_pk}))
        
#         # # self.assertRedirects(post_response, reverse_lazy('TalentProfile_delete',kwargs={'pk':TalentProfile_pk}), status_code=302)


#         # self.assertEqual(response.status_code, 200)

#         # # check for Correct Template Used
#         # self.assertTemplateUsed(response, 'TalentProfiles/TalentProfile_delete.html')




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
#         response = self.client.get('/TalentProfiles/1/')

#         self.assertEqual(response.status_code, 200)


#------------------------------------------------------------------------------------------------------#
    
        
#     # def test_update_page_status_code(self):
#     #     # url = reverse('TalentProfileListView')
#     #     response = self.client.get('/TalentProfiles/1/')
#     #     self.assertEqual(response.status_code, 200)

#-------------------------------------------------------------------------------------------------------#

#     # def test_detail_page_status_code(self):
#     #     response = self.client.get('/{1}/')
#     #     self.assertEqual(response.status_code, 200)

#-------------------------------------------------------------------------------------------------------#

#     # def test_delete_page_status_code(self):
#     #     response = self.client.get('/{1}/delete/')
#     #     self.assertEqual(response.status_code, 200)