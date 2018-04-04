from django.test import TestCase,SimpleTestCase
from django.urls import reverse,reverse_lazy
from .models import UserCoinBox
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils import timezone


#  Test Class for UserCoinBox Application

# class UserCoinBoxTest(TestCase):

# ########################## Model Testing ####   ########################
  

#     # UserCoinBox object with dummy data 
#     def setUp(self):

#         # dummy user for login 
#         self.user = get_user_model().objects.create_user(
#             username='testuser',
#             email='test@email.com',
#             password = 'test'
#         )

#         # self.UserCoinBox =  UserCoinBox.objects.create(

#         # # Fields according to defined in Model    
#         # UserCoinBox_Amount = 199,
#         # UserCoinBox_End_Date = timezone.now(),
#         # UserCoinBox_FOR_FILM_COIN = 1000,
#         # UserCoinBox_Openings_Allowed = True,
#         # UserCoinBox_Location_Allowed = True,
#         # UserCoinBox_Pitch_Allowed = True,
#         # UserCoinBox_Pitch_Box_Capacity_Image_per_pitch = 111,
#         # UserCoinBox_Start_Date = timezone.now(),
#         # UserCoinBox_Type = 'UserCoinBox_Type',
#         # UserCoinBox_User_ID = self.user,
#         # )

# #-----------------------------------------------------------------------------------------#

#     # Check redirection URL
#     def test_get_absolute_url(self):
#         # Redirection goes to UserCoinBox details
#         self.assertEquals(self.UserCoinBox.get_absolute_url(), '/usercoinbox/1')

# #-----------------------------------------------------------------------------------------#

#     # Check Conent of UserCoinBox object created by create object query set
#     def test_UserCoinBox_content(self):
#         # Verify for each field  
#         # self.assertEqual(int(f'{self.UserCoinBox.UserCoinBox_Amount}'), 199)
#         # self.assertEqual(int(f'{self.UserCoinBox.UserCoinBox_FOR_FILM_COIN}'), 1000)
#         # self.assertEqual(bool(f'{self.UserCoinBox.UserCoinBox_Openings_Allowed}'), True)
#         # self.assertEqual(bool(f'{self.UserCoinBox.UserCoinBox_Location_Allowed}'), True)
#         # self.assertEqual(bool(f'{self.UserCoinBox.UserCoinBox_Pitch_Allowed}'), True)
#         # self.assertEqual(int(f'{self.UserCoinBox.UserCoinBox_Pitch_Box_Capacity_Image_per_pitch}'), 111)
#         # self.assertEqual(f'{self.UserCoinBox.UserCoinBox_Type}', 'UserCoinBox_Type')
#         # self.assertEqual(f'{self.UserCoinBox.UserCoinBox_User_ID}', self.user.username)
# #--------------------------------------------------------------------------------------------#

# # #############################   Model Test End   ###########################################







# # ###############################    Views Test       ########################################

    
#     # Test UserCoinBox List View
    
#     def test_UserCoinBoxList_view(self):
#         # # Login the user defined in SetUp
#         # self.client.login(username='testuser', password='test')

#         # # Get respomse from defined URL namespace
#         # response = self.client.get(reverse('UserCoinBox_list'))
#         # self.assertEqual(response.status_code, 200)

#         # # Check Content of List View
#         # self.assertContains(response,199)
#         # self.assertContains(response,'UserCoinBox_Type')
#         # # Check for Correct template used in template/UserCoinBoxs
#         # self.assertTemplateUsed(response, 'UserCoinBoxs/UserCoinBox_list.html')

# #--------------------------------------------------------------------------------------------#
    

#     # Test UserCoinBox Detail View

#     def test_UserCoinBoxDetail_view(self):
#         # # Login the user defined in SetUp
#         # self.client.login(username='testuser', password='test')
        
#         # # Find primary key of table
#         # UserCoinBox_pk = UserCoinBox.objects.get(UserCoinBox_Amount=199).pk
        
#         # # Get response
#         # response = self.client.get(reverse_lazy('UserCoinBox_details',kwargs={'pk':UserCoinBox_pk}))

#         # # Check for any invalid value
#         # no_response = self.client.get(reverse_lazy('UserCoinBox_details',kwargs={'pk':10000}))

#         # # 202 for valid and 404 for invalid
#         # self.assertEqual(response.status_code, 200)
#         # self.assertEqual(no_response.status_code, 404)

#         # # check for content of Detail Page
#         # self.assertContains(response,self.user.username)

#         # # Check for Correct template used in template/UserCoinBoxs
#         # self.assertTemplateUsed(response, 'UserCoinBoxs/UserCoinBox_details.html')

# #-------------------------------------------------------------------------------------------#    


#     # Test UserCoinBox Create View
    
#     def test_UserCoinBoxCreate_view(self):
#         # # Login the user defined in SetUps
#         # self.client.login(username='testuser', password='test') 

#         # # Generate response after creating an view using Http post method
#         # response = self.client.post('/UserCoinBox/new/', {
#         # 'UserCoinBox_Amount' : 199,
#         # 'UserCoinBox_End_Date' : timezone.now(),
#         # 'UserCoinBox_FOR_FILM_COIN' : 1000,
#         # 'UserCoinBox_Openings_Allowed' : True,
#         # 'UserCoinBox_Location_Allowed' : True,
#         # 'UserCoinBox_Pitch_Allowed' : True,
#         # 'UserCoinBox_Pitch_Box_Capacity_Image_per_pitch' : 111,
#         # 'UserCoinBox_Start_Date' : timezone.now(),
#         # 'UserCoinBox_Type' : 'UserCoinBox_Type',
#         # 'UserCoinBox_User_ID' : self.user,
#         # })

#         # # print(response.content)
#         # # Check for successful response
#         # self.assertEqual(response.status_code, 200)
#         # self.assertContains(response, 'UserCoinBox_Type')
#         # self.assertContains(response, self.user.username)
#         # self.assertContains(response, 'checked')
#         # self.assertContains(response, 111)
#         # self.assertContains(response, 1000)
#         # self.assertContains(response, 199)


#         # # Check for correct template used in template/UserCoinBoxs
#         # self.assertTemplateUsed(response, 'UserCoinBoxs/UserCoinBox_new.html')

# #---------------------------------------------------------------------------------------#


#     # Test UserCoinBox Update view 

#     def test_UserCoinBoxupdate_view(self):
#         # # Login the user
#         # self.client.login(username='testuser', password='test')
        
#         # # Find primary key of table
#         # UserCoinBox_pk = UserCoinBox.objects.get(UserCoinBox_Type='UserCoinBox_Type').pk
        
#         # # Get response using pk on details view
#         # response = self.client.get(reverse_lazy('UserCoinBox_details',kwargs={'pk':UserCoinBox_pk}), {
#         # 'UserCoinBox_Amount' : 199,
#         # 'UserCoinBox_End_Date' : timezone.now(),
#         # 'UserCoinBox_FOR_FILM_COIN' : 1000,
#         # 'UserCoinBox_Openings_Allowed' : True,
#         # 'UserCoinBox_Location_Allowed' : True,
#         # 'UserCoinBox_Pitch_Allowed' : True,
#         # 'UserCoinBox_Pitch_Box_Capacity_Image_per_pitch' : 111,
#         # 'UserCoinBox_Start_Date' : timezone.now(),
#         # 'UserCoinBox_Type' : 'UserCoinBox_Type',
#         # 'UserCoinBox_User_ID' : self.user,
#         # })
#         # # Check for successful response
#         # self.assertEqual(response.status_code, 200)

#         # # Check for correct templates
#         # self.assertTemplateUsed(response,'UserCoinBoxs/UserCoinBox_details.html')


# #--------------------------------------------------------------------------------------------#


# # Test Delete View of UserCoinBox views

#     def test_UserCoinBoxdelete_view(self):
#         # # Login the user
#         # self.client.login(username='testuser', password='test')

#         # #Find primary key of table
#         # UserCoinBox_pk = UserCoinBox.objects.get(UserCoinBox_Type='UserCoinBox_Type').pk
        
#         # # Get response to delete 

#         # response = self.client.get(reverse_lazy('UserCoinBox_delete',kwargs={'pk':UserCoinBox_pk}))
#         # # self.assertContains(response, 'Are you sure you want to delete') # THIS PART WORKS

#         # # Check deleted value , returns false i.e.302
#         # post_response = self.client.post(reverse_lazy('UserCoinBox_delete',kwargs={'pk':UserCoinBox_pk}))
        
#         # # self.assertRedirects(post_response, reverse_lazy('UserCoinBox_delete',kwargs={'pk':UserCoinBox_pk}), status_code=302)


#         # self.assertEqual(response.status_code, 200)

#         # # check for Correct Template Used
#         # self.assertTemplateUsed(response, 'UserCoinBoxs/UserCoinBox_delete.html')




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
#         response = self.client.get('/UserCoinBoxs/1/')

#         self.assertEqual(response.status_code, 200)


#------------------------------------------------------------------------------------------------------#
    
        
#     # def test_update_page_status_code(self):
#     #     # url = reverse('UserCoinBoxListView')
#     #     response = self.client.get('/UserCoinBoxs/1/')
#     #     self.assertEqual(response.status_code, 200)

#-------------------------------------------------------------------------------------------------------#

#     # def test_detail_page_status_code(self):
#     #     response = self.client.get('/{1}/')
#     #     self.assertEqual(response.status_code, 200)

#-------------------------------------------------------------------------------------------------------#

#     # def test_delete_page_status_code(self):
#     #     response = self.client.get('/{1}/delete/')
#     #     self.assertEqual(response.status_code, 200)