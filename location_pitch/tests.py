from django.test import TestCase,SimpleTestCase
from django.urls import reverse,reverse_lazy
from .models import LocationPitch
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.forms.models import model_to_dict


#  Test Class for Costume Application

class LocationPitchTest(TestCase):

########################## Model Testing ############################


    # Costume object with dummy data
    def setUp(self):
        # User for login
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password = 'test'
        )

        self.LocationPitch =  LocationPitch.objects.create(

        # Fields according to defined in Model
        LocationPitch_By_User = self.user, #Defined above in get_user_model
        LocationPitch_Location_Required = 'LocationPitch_Location_Required',
        LocationPitch_Submitted = True,
        LocationPitch_Modified_Date = timezone.now(),
        LocationPitch_Message = 'LocationPitch_Message',
        location_pitch_Author = self.user,
        LocationPitch_Created_Date =  timezone.now(),
        )

#-----------------------------------------------------------------------------------------#

    # Check redirection URL
    def test_get_absolute_url(self):
        # Redirection goes to costume details
        self.assertEquals(self.LocationPitch.get_absolute_url(), '/location_pitch/1')

#-----------------------------------------------------------------------------------------#

    # Check Conent of costume object created by create object query set
    def test_LocationPitch_content(self):
        # Verify for each field
        self.assertEqual(f'{self.LocationPitch.LocationPitch_By_User}', self.user.username)  #Defined in SetUp
        self.assertEqual(f'{self.LocationPitch.LocationPitch_Location_Required}', 'LocationPitch_Location_Required')
        self.assertEqual(f'{self.LocationPitch.LocationPitch_Submitted}', 'True')
        self.assertEqual(f'{self.LocationPitch.LocationPitch_Message}', 'LocationPitch_Message')
        self.assertEqual(f'{self.LocationPitch.location_pitch_Author}', self.user.username)   #Defined in SetUp

#--------------------------------------------------------------------------------------------#

# #############################   Model Test End   ###########################################







# ###############################    Views Test       ########################################


    # Test Costume List View

    def test_LocationPitchList_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test')

        # Get respomse from defined URL namespace
        response = self.client.get(reverse('location_pitch_list'))
        self.assertEqual(response.status_code, 200)

        # Check Content of List View
        self.assertContains(response,self.user.username)
        # Check for Correct template used in template/Costumes
        self.assertTemplateUsed(response, 'location_pitch/location_pitch_list.html')

#--------------------------------------------------------------------------------------------#


    # Test LocationFinancial Detail View

    def test_LocationPitchDetail_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test')

        # Find primary key of table
        LocationPitch_pk = LocationPitch.objects.get(LocationPitch_Message = 'LocationPitch_Message').pk

        # Get response
        response = self.client.get(reverse_lazy('location_pitch_details',kwargs={'pk':LocationPitch_pk}))

        # Check for any invalid value
        no_response = self.client.get(reverse_lazy('location_pitch_details',kwargs={'pk':10000}))

        # 202 for valid and 404 for invalid
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)

        # check for content of Detail Page
        self.assertContains(response, 'LocationPitch_Message')

        # Check for Correct template used in template/LocationFinancials
        self.assertTemplateUsed(response, 'location_pitch/location_pitch_detail.html')

#-------------------------------------------------------------------------------------------#


    # Test Costume Create View

    def test_LocationPitchCreate_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test')

        # Generate response after creating an view using Http post method
        response = self.client.post('/location_pitch/new/', {
        'LocationPitch_By_User':self.user,   #defined in setup
        'LocationPitch_Location_Required':'LocationPitch_Location_Required',
        'LocationPitch_Submitted':True,
        'LocationPitch_Modified_Date':timezone.now(),
        'LocationPitch_Message':'LocationPitch_Message',
        'location_pitch_Author':self.user,
        'LocationPitch_Created_Date':timezone.now(),
        })

        # Check for successful response
        self.assertEqual(response.status_code, 200)

        # Check response values
        self.assertContains(response, self.user.username)    # Same as defined in SetUp
        self.assertContains(response, 'LocationPitch_Location_Required')
        self.assertContains(response, 'checked')
        self.assertContains(response, 'LocationPitch_Message')
        self.assertContains(response, self.user.username)     # Same as defined in SetUp


        # Check for correct template used in template/location_pitch
        self.assertTemplateUsed(response, 'location_pitch/location_pitch_new.html')

#---------------------------------------------------------------------------------------#


    # Test LocationPitch Update view

    def test_LocationPitchupdate_view(self):
        # Login the user
        self.client.login(username='testuser', password='test')

        # Find primary key of table
        LocationPitch_pk = LocationPitch.objects.get(LocationPitch_Message='LocationPitch_Message').pk

        # Get response using pk on details view
        response = self.client.get(reverse_lazy('location_pitch_details',kwargs={'pk':LocationPitch_pk}), {
        'LocationPitch_By_User':self.user.username,
        'LocationPitch_Location_Required':'LocationPitch_Location_Required',
        'LocationPitch_Submitted':True,
        'LocationPitch_Modified_Date': timezone.now(),
        'LocationPitch_Message':'LocationPitch_Message',
        'location_pitch_Author':self.user.username,
        'LocationPitch_Created_Date':timezone.now(),
        })
        #Check for successful response
        self.assertEqual(response.status_code, 200)

        # Check for correct templates
        self.assertTemplateUsed(response,'location_pitch/location_pitch_detail.html')


#--------------------------------------------------------------------------------------------#


# Test Delete View of location_pitch views

    def test_LocationPitchdelete_view(self):
        # Login the user
        self.client.login(username='testuser', password='test')

        # Find primary key of table
        LocationPitch_pk = LocationPitch.objects.get(LocationPitch_Message='LocationPitch_Message').pk

        # Get response to delete

        response = self.client.get(reverse_lazy('location_pitch_delete',kwargs={'pk':LocationPitch_pk}))
        self.assertContains(response, 'Are you sure you want to delete') # THIS PART WORKS

        # Check deleted value , returns false i.e.302
        post_response = self.client.post(reverse_lazy('location_pitch_delete',kwargs={'pk':LocationPitch_pk}))

        # self.assertRedirects(post_response, reverse_lazy('Costume_delete',kwargs={'pk':Costume_pk}), status_code=302)


        self.assertEqual(response.status_code, 200)

        # check for Correct Template Used
        self.assertTemplateUsed(response, 'location_pitch/location_pitch_delete.html')




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
