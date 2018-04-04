from django.test import TestCase,SimpleTestCase
from django.urls import reverse,reverse_lazy
from .models import LocationPSnDC
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.forms.models import model_to_dict


#  Test Class for Costume Application

class LocationPSnDCTest(TestCase):

########################## Model Testing ############################


    # Costume object with dummy data
    def setUp(self):
        # User for login
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password = 'test'
        )

        self.LocationPSnDC =  LocationPSnDC.objects.create(

        # Fields according to defined in Model
        LocationPSnDC_Dc_Office = 'LocationPSnDC_Dc_Office', #Defined above in get_user_model
        LocationPSnDC_Dcp_Office = 'LocationPSnDC_Dcp_Office',
        LocationPSnDC_Location_Id = 'LocationPSnDC_Location_Id',
        LocationPSnDC_Police_Station = 'LocationPSnDC_Police_Station',
        LocationPSnDC_Modified_Date = timezone.now(),
        LocationPSnDC_Created_Date = timezone.now(),
        LocationPSnDC_Message =  'LocationPSnDC_Message',
        LocationPSnDC_Author = self.user,
        )

#-----------------------------------------------------------------------------------------#

    # Check redirection URL
    def test_get_absolute_url(self):
        # Redirection goes to costume details
        self.assertEquals(self.LocationPSnDC.get_absolute_url(), '/location_psndc/1')

#-----------------------------------------------------------------------------------------#

    # Check Conent of costume object created by create object query set
    def test_LocationPSnDC_content(self):
        # Verify for each field
        self.assertEqual(f'{self.LocationPSnDC.LocationPSnDC_Dc_Office}', 'LocationPSnDC_Dc_Office')  #Defined in SetUp
        self.assertEqual(f'{self.LocationPSnDC.LocationPSnDC_Dcp_Office}', 'LocationPSnDC_Dcp_Office')
        self.assertEqual(f'{self.LocationPSnDC.LocationPSnDC_Location_Id}', 'LocationPSnDC_Location_Id')
        self.assertEqual(f'{self.LocationPSnDC.LocationPSnDC_Police_Station}', 'LocationPSnDC_Police_Station')
        self.assertEqual(f'{self.LocationPSnDC.LocationPSnDC_Message}', 'LocationPSnDC_Message')
        self.assertEqual(f'{self.LocationPSnDC.LocationPSnDC_Author}', self.user.username)



    #Test Location_psndc ListView

    # def test_LocationPSnDCList_view(self):
    #     # Login the user defined in SetUp
    #     self.client.login(username='testuser', password='test')
    #
    #     # Get respomse from defined URL namespace
    #     response = self.client.get(reverse('location_psndc_list'))
    #     self.assertEqual(response.status_code, 200)
    #
    #     # Check Content of List View
    #     self.assertContains(response,self.user.username)
    #     # Check for Correct template used in template/Costumes
    #     self.assertTemplateUsed(response, 'location_psndc/location_psndc_list.html')


    def test_LocationPSnDCList_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test')

        # Get respomse from defined URL namespace
        response = self.client.get(reverse('location_psndc_list'))
        self.assertEqual(response.status_code, 200)

        # Check Content of List View
        self.assertContains(response,self.user.username)
        # Check for Correct template used in template/Costumes
        self.assertTemplateUsed(response, 'location_psndc/location_psndc_list.html')



    # Test LocationPSnDC Detail View

    def test_LocationPSnDCDetail_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test')

        # Find primary key of table
        LocationPSnDC_pk = LocationPSnDC.objects.get(LocationPSnDC_Message='LocationPSnDC_Message').pk

        # Get response
        response = self.client.get(reverse_lazy('location_psndc_details',kwargs={'pk':LocationPSnDC_pk}))

        # Check for any invalid value
        no_response = self.client.get(reverse_lazy('location_psndc_details',kwargs={'pk':10000}))

        # 202 for valid and 404 for invalid
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)

        # check for content of Detail Page
        self.assertContains(response, 'LocationPSnDC_Message')  #LocationPSnDC_Message

        # Check for Correct template used in template/LocationPSnDC
        self.assertTemplateUsed(response, 'location_psndc/location_psndc_detail.html')




    # Test EducationInfo Create View

    def test_LocationPSnDCCreate_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test')

        # Generate response after creating an view using Http post method
        response = self.client.post('/location_psndc/new/', {
        'LocationPSnDC_Dc_Office' : 'LocationPSnDC_Dc_Office',
        'LocationPSnDC_Dcp_Office':'LocationPSnDC_Dcp_Office',
        'LocationPSnDC_Location_Id':'LocationPSnDC_Location_Id',
        'LocationPSnDC_Police_Station':'LocationPSnDC_Police_Station',
        'LocationPSnDC_Modified_Date':timezone.now(),
        'LocationPSnDC_Created_Date':timezone.now(),
        'LocationPSnDC_Message':'LocationPSnDC_Message',
        'LocationPSnDC_Author':self.user,
        },follow = True)

        # print(response.content)
        # Check for successful response
        self.assertEqual(response.status_code, 200)
        # self.assertContains(response, False)
        self.assertContains(response, 'LocationPSnDC_Dc_Office')
        self.assertContains(response, 'LocationPSnDC_Dcp_Office')
        self.assertContains(response, 'LocationPSnDC_Location_Id')
        self.assertContains(response, 'LocationPSnDC_Police_Station')
        self.assertContains(response, 'LocationPSnDC_Message')
        self.assertContains(response, self.user.username)     # Same as defined in SetUp
        # Check for correct template used in template/EducationInfos
        self.assertTemplateUsed(response, 'location_psndc/location_psndc_detail.html')

#---------------------------------------------------------------------------------------#


    # Test EducationInfo Update view

    def test_LocationPSnDCupdate_view(self):
        # Login the user
        self.client.login(username='testuser', password='test')

        # Find primary key of table
        LocationPSnDC_pk = LocationPSnDC.objects.get(LocationPSnDC_Location_Id='LocationPSnDC_Location_Id').pk

        # Get response using pk on details view
        response = self.client.get(reverse_lazy('location_psndc_details',kwargs={'pk':LocationPSnDC_pk}), {
        'LocationPSnDC_Dc_Office' : 'LocationPSnDC_Dc_Office',
        'LocationPSnDC_Dcp_Office':'LocationPSnDC_Dcp_Office',
        'LocationPSnDC_Location_Id':'LocationPSnDC_Location_Id',
        'LocationPSnDC_Police_Station':'LocationPSnDC_Police_Station',
        'LocationPSnDC_Modified_Date':timezone.now(),
        'LocationPSnDC_Created_Date':timezone.now(),
        'LocationPSnDC_Message':'LocationPSnDC_Message',
        'LocationPSnDC_Author':self.user,
        },follow = True)
        # Check for successful response
        self.assertEqual(response.status_code, 200)

        # Check for correct templates
        self.assertTemplateUsed(response,'location_psndc/location_psndc_detail.html')


#--------------------------------------------------------------------------------------------#

# Test Delete View of EducationInfo views

    def test_LocationPSnDCdelete_view(self):
        # Login the user
        self.client.login(username='testuser', password='test')

        # Find primary key of table
        LocationPSnDC_pk = LocationPSnDC.objects.get(LocationPSnDC_Location_Id='LocationPSnDC_Location_Id').pk

        # Get response to delete

        response = self.client.get(reverse_lazy('location_psndc_delete',kwargs={'pk':LocationPSnDC_pk}))
        self.assertContains(response, 'Are you sure you want to delete') # THIS PART WORKS

        # Check deleted value , returns false i.e.302
        post_response = self.client.post(reverse_lazy('location_psndc_delete',kwargs={'pk':LocationPSnDC_pk}))

        # self.assertRedirects(post_response, reverse_lazy('EducationInfo_delete',kwargs={'pk':EducationInfo_pk}), status_code=302)


        self.assertEqual(response.status_code, 200)

        # check for Correct Template Used
        self.assertTemplateUsed(response, 'location_psndc/location_psndc_delete.html')




# ################################     View Testing End   #################################################


# ################################     Testing the URLs       ##############################################

class PagesTests(SimpleTestCase):

    # Check URL for list/ Home
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

# #-----------------------------------------------------------------------------------------------------#
