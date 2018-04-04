from django.test import TestCase,SimpleTestCase
from django.urls import reverse,reverse_lazy
from .models import LocationFinancial
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils import timezone


#  Test Class for LocationFinancial Application

class LocationFinancialTest(TestCase):

########################## Model Testing ############################


    # LocationFinancial object with dummy data
    def setUp(self):

        # dummy user for login
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password = 'test'
        )

        self.LocationFinancial =  LocationFinancial.objects.create(

        # Fields according to defined in Model
        LocationFinancial_Availability = 'True',
        LocationFinancial_Discount_On_Crewsize='True',
        LocationFinancial_Discount_On_Shoot_Length='True',
        LocationFinancial_Location_Id='LocationFinancial_Location_Id',
        LocationFinancial_Monthly_Rate_Crewsize1 = 'LocationFinancial_Monthly_Rate_Crewsize1',
        LocationFinancial_Monthly_Rate_Crewsize2 = 'LocationFinancial_Monthly_Rate_Crewsize2',
        LocationFinancial_Monthly_Rate_Crewsize3 = 'LocationFinancial_Monthly_Rate_Crewsize3',
        LocationFinancial_Monthly_Rate_Crewsize4 = 'LocationFinancial_Monthly_Rate_Crewsize4',
        LocationFinancial_One_Day_Rent_Crewsize1 = 'LocationFinancial_One_Day_Rent_Crewsize1',
        LocationFinancial_One_Day_Rent_Crewsize2 = 'LocationFinancial_One_Day_Rent_Crewsize2',
        LocationFinancial_One_Day_Rent_Crewsize3 = 'LocationFinancial_One_Day_Rent_Crewsize3',
        LocationFinancial_One_Day_Rent_Crewsize4 = 'LocationFinancial_One_Day_Rent_Crewsize4',
        LocationFinancial_Prices_Available = True,
        LocationFinancial_Student_Rate = 'LocationFinancial_Student_Rate',
        LocationFinancial_Weekly_Rate_Crewsize1 = 'LocationFinancial_Weekly_Rate_Crewsize1',
        LocationFinancial_Weekly_Rate_Crewsize2 = 'LocationFinancial_Weekly_Rate_Crewsize2',
        LocationFinancial_Weekly_Rate_Crewsize3 = 'LocationFinancial_Weekly_Rate_Crewsize3',
        LocationFinancial_Weekly_Rate_Crewsize4 = 'LocationFinancial_Weekly_Rate_Crewsize4',
        LocationFinancial_Modified_Date = timezone.now(),
        LocationFinancial_Creator = self.user,              # Defined above in get_user_model
        LocationFinancial_Created_Date = timezone.now(),
        )

#-----------------------------------------------------------------------------------------#

    # Check redirection URL
    def test_get_absolute_url(self):
        # Redirection goes to LocationFinancial details
        self.assertEquals(self.LocationFinancial.get_absolute_url(), '/location_financial/1')

#-----------------------------------------------------------------------------------------#

    # Check Conent of LocationFinancial object created by create object query set
    def test_LocationFinancial_content(self):
        # Verify for each field
        self.assertEqual(f'{self.LocationFinancial.LocationFinancial_Availability}', 'True')
        self.assertEqual(f'{self.LocationFinancial.LocationFinancial_Discount_On_Crewsize}', 'True')
        self.assertEqual(f'{self.LocationFinancial.LocationFinancial_Discount_On_Shoot_Length}', 'True')
        self.assertEqual(f'{self.LocationFinancial.LocationFinancial_Location_Id}', 'LocationFinancial_Location_Id')
        self.assertEqual(f'{self.LocationFinancial.LocationFinancial_Monthly_Rate_Crewsize1}', 'LocationFinancial_Monthly_Rate_Crewsize1')
        self.assertEqual(f'{self.LocationFinancial.LocationFinancial_Monthly_Rate_Crewsize2}', 'LocationFinancial_Monthly_Rate_Crewsize2')
        self.assertEqual(f'{self.LocationFinancial.LocationFinancial_Monthly_Rate_Crewsize3}', 'LocationFinancial_Monthly_Rate_Crewsize3')
        self.assertEqual(f'{self.LocationFinancial.LocationFinancial_Monthly_Rate_Crewsize4}', 'LocationFinancial_Monthly_Rate_Crewsize4')
        self.assertEqual(f'{self.LocationFinancial.LocationFinancial_One_Day_Rent_Crewsize1}', 'LocationFinancial_One_Day_Rent_Crewsize1')
        self.assertEqual(f'{self.LocationFinancial.LocationFinancial_One_Day_Rent_Crewsize2}', 'LocationFinancial_One_Day_Rent_Crewsize2')
        self.assertEqual(f'{self.LocationFinancial.LocationFinancial_One_Day_Rent_Crewsize3}', 'LocationFinancial_One_Day_Rent_Crewsize3')
        self.assertEqual(f'{self.LocationFinancial.LocationFinancial_One_Day_Rent_Crewsize4}', 'LocationFinancial_One_Day_Rent_Crewsize4')
        self.assertEqual(f'{self.LocationFinancial.LocationFinancial_Prices_Available}', 'True')
        self.assertEqual(f'{self.LocationFinancial.LocationFinancial_Student_Rate}', 'LocationFinancial_Student_Rate')
        self.assertEqual(f'{self.LocationFinancial.LocationFinancial_Weekly_Rate_Crewsize1}', 'LocationFinancial_Weekly_Rate_Crewsize1')
        self.assertEqual(f'{self.LocationFinancial.LocationFinancial_Weekly_Rate_Crewsize2}', 'LocationFinancial_Weekly_Rate_Crewsize2')
        self.assertEqual(f'{self.LocationFinancial.LocationFinancial_Weekly_Rate_Crewsize3}', 'LocationFinancial_Weekly_Rate_Crewsize3')
        self.assertEqual(f'{self.LocationFinancial.LocationFinancial_Weekly_Rate_Crewsize4}', 'LocationFinancial_Weekly_Rate_Crewsize4')
        self.assertEqual(f'{self.LocationFinancial.LocationFinancial_Creator}', self.user.username)    # Defined in SetUp


#--------------------------------------------------------------------------------------------#

# #############################   Model Test End   ########################################### #


# ###############################    Views Test       ########################################


    # Test LocationFinancial List View

    def test_LocationFinancialList_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test')

        # Get response from defined URL namespace
        response = self.client.get(reverse('location_financial_list'))
        self.assertEqual(response.status_code, 200)

        # Check Content of List View
        self.assertContains(response, self.user.username)
        # Check for Correct template used in template/LocationFinancials
        self.assertTemplateUsed(response, 'location_financial/location_financial_list.html')

#--------------------------------------------------------------------------------------------#

    # Test LocationFinancial Detail View

    def test_LocationFinancialDetail_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test')

        # Find primary key of table
        LocationFinancial_pk = LocationFinancial.objects.get(LocationFinancial_Student_Rate = 'LocationFinancial_Student_Rate').pk

        # Get response
        response = self.client.get(reverse_lazy('location_financial_details',kwargs={'pk':LocationFinancial_pk}))

        # Check for any invalid value
        no_response = self.client.get(reverse_lazy('location_financial_details',kwargs={'pk':10000}))

        # 202 for valid and 404 for invalid
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)

        # check for content of Detail Page
        self.assertContains(response, 'LocationFinancial_Student_Rate')

        # Check for Correct template used in template/LocationFinancials
        self.assertTemplateUsed(response, 'location_financial/location_financial_detail.html')

#-------------------------------------------------------------------------------------------#


    # Test EducationInfo Create View

    def test_LocationFinancialCreate_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test')

        # Generate response after creating an view using Http post method
        response = self.client.post('/location_financial/new/', {
        'LocationFinancial_Availability' : True,
        'LocationFinancial_Discount_On_Crewsize':True,
        'LocationFinancial_Discount_On_Shoot_Length':True,
        'LocationFinancial_Location_Id':'LocationFinancial_Location_Id',
        'LocationFinancial_Monthly_Rate_Crewsize1':'LocationFinancial_Monthly_Rate_Crewsize1',
        'LocationFinancial_Monthly_Rate_Crewsize2':'LocationFinancial_Monthly_Rate_Crewsize2',
        'LocationFinancial_Monthly_Rate_Crewsize3':'LocationFinancial_Monthly_Rate_Crewsize3',
        'LocationFinancial_Monthly_Rate_Crewsize4':'LocationFinancial_Monthly_Rate_Crewsize4',
        'LocationFinancial_One_Day_Rent_Crewsize1':'LocationFinancial_One_Day_Rent_Crewsize1',
        'LocationFinancial_One_Day_Rent_Crewsize2':'LocationFinancial_One_Day_Rent_Crewsize2',
        'LocationFinancial_One_Day_Rent_Crewsize3':'LocationFinancial_One_Day_Rent_Crewsize3',
        'LocationFinancial_One_Day_Rent_Crewsize4':'LocationFinancial_One_Day_Rent_Crewsize4',
        'LocationFinancial_Prices_Available':True, # Defined above in get_user_model
        'LocationFinancial_Student_Rate':'LocationFinancial_Student_Rate',
        'LocationFinancial_Weekly_Rate_Crewsize1':'LocationFinancial_Weekly_Rate_Crewsize1',
        'LocationFinancial_Weekly_Rate_Crewsize2':'LocationFinancial_Weekly_Rate_Crewsize2',
        'LocationFinancial_Weekly_Rate_Crewsize3':'LocationFinancial_Weekly_Rate_Crewsize3',
        'LocationFinancial_Weekly_Rate_Crewsize4':'LocationFinancial_Weekly_Rate_Crewsize4',
        'LocationFinancial_Modified_Date':timezone.now(),
        'LocationFinancial_Creator':self.user,
        'LocationFinancial_Created_Date': timezone.now()
        },follow = True)

        # print(response.content)
        # Check for successful response
        self.assertEqual(response.status_code, 200)
        # self.assertContains(response, False)
        self.assertContains(response, 'LocationFinancial_Location_Id')
        self.assertContains(response, 'LocationFinancial_Monthly_Rate_Crewsize1')
        self.assertContains(response, 'LocationFinancial_Monthly_Rate_Crewsize2')
        self.assertContains(response, 'LocationFinancial_Monthly_Rate_Crewsize3')
        self.assertContains(response, 'LocationFinancial_Monthly_Rate_Crewsize4')
        self.assertContains(response, 'LocationFinancial_One_Day_Rent_Crewsize1')
        self.assertContains(response, 'LocationFinancial_One_Day_Rent_Crewsize2')
        self.assertContains(response, 'LocationFinancial_One_Day_Rent_Crewsize3')
        self.assertContains(response, 'LocationFinancial_One_Day_Rent_Crewsize4')
        self.assertContains(response, True)
        self.assertContains(response, 'LocationFinancial_Student_Rate')
        self.assertContains(response, 'LocationFinancial_Weekly_Rate_Crewsize1')
        self.assertContains(response, 'LocationFinancial_Weekly_Rate_Crewsize2')
        self.assertContains(response, 'LocationFinancial_Weekly_Rate_Crewsize3')
        self.assertContains(response, 'LocationFinancial_Weekly_Rate_Crewsize4')
        # self.assertContains(response, 'LocationFinancial_Weekly_Rate_Crewsize1')
        self.assertContains(response, self.user.username)      # Same as defined in SetUp


        # Check for correct template used in template/EducationInfos
        self.assertTemplateUsed(response, 'location_financial/location_financial_detail.html')

#---------------------------------------------------------------------------------------#


    # Test EducationInfo Update view

    def test_LocationFinancialupdate_view(self):
        # Login the user
        self.client.login(username='testuser', password='test')

        # Find primary key of table
        LocationFinancial_pk = LocationFinancial.objects.get(LocationFinancial_Location_Id='LocationFinancial_Location_Id').pk

        # Get response using pk on details view
        response = self.client.get(reverse_lazy('location_financial_details',kwargs={'pk':LocationFinancial_pk}), {
        'LocationFinancial_Availability' : True,
        'LocationFinancial_Discount_On_Crewsize':True,
        'LocationFinancial_Discount_On_Shoot_Length':True,
        'LocationFinancial_Location_Id':'LocationFinancial_Location_Id',
        'LocationFinancial_Monthly_Rate_Crewsize1':'LocationFinancial_Monthly_Rate_Crewsize1',
        'LocationFinancial_Monthly_Rate_Crewsize2':'LocationFinancial_Monthly_Rate_Crewsize2',
        'LocationFinancial_Monthly_Rate_Crewsize3':'LocationFinancial_Monthly_Rate_Crewsize3',
        'LocationFinancial_Monthly_Rate_Crewsize4':'LocationFinancial_Monthly_Rate_Crewsize4',
        'LocationFinancial_One_Day_Rent_Crewsize1':'LocationFinancial_One_Day_Rent_Crewsize1',
        'LocationFinancial_One_Day_Rent_Crewsize2':'LocationFinancial_One_Day_Rent_Crewsize2',
        'LocationFinancial_One_Day_Rent_Crewsize3':'LocationFinancial_One_Day_Rent_Crewsize3',
        'LocationFinancial_One_Day_Rent_Crewsize4':'LocationFinancial_One_Day_Rent_Crewsize4',
        'LocationFinancial_Prices_Available':True, # Defined above in get_user_model
        'LocationFinancial_Student_Rate':'LocationFinancial_Student_Rate',
        'LocationFinancial_Weekly_Rate_Crewsize1':'LocationFinancial_Weekly_Rate_Crewsize1',
        'LocationFinancial_Weekly_Rate_Crewsize2':'LocationFinancial_Weekly_Rate_Crewsize2',
        'LocationFinancial_Weekly_Rate_Crewsize3':'LocationFinancial_Weekly_Rate_Crewsize3',
        'LocationFinancial_Weekly_Rate_Crewsize4':'LocationFinancial_Weekly_Rate_Crewsize4',
        'LocationFinancial_Modified_Date':timezone.now(),
        'LocationFinancial_Creator':self.user,
        'LocationFinancial_Created_Date': timezone.now()
        },follow = True)
        # Check for successful response
        self.assertEqual(response.status_code, 200)

        # Check for correct templates
        self.assertTemplateUsed(response,'location_financial/location_financial_detail.html')


#--------------------------------------------------------------------------------------------#


# Test Delete View of EducationInfo views

    def test_LocationFinancialdelete_view(self):
        # Login the user
        self.client.login(username='testuser', password='test')

        # Find primary key of table
        LocationFinancial_pk = LocationFinancial.objects.get(LocationFinancial_Location_Id='LocationFinancial_Location_Id').pk

        # Get response to delete

        response = self.client.get(reverse_lazy('location_financial_delete',kwargs={'pk':LocationFinancial_pk}))
        self.assertContains(response, 'Are you sure you want to delete') # THIS PART WORKS

        # Check deleted value , returns false i.e.302
        post_response = self.client.post(reverse_lazy('location_financial_delete',kwargs={'pk':LocationFinancial_pk}))

        # self.assertRedirects(post_response, reverse_lazy('EducationInfo_delete',kwargs={'pk':EducationInfo_pk}), status_code=302)


        self.assertEqual(response.status_code, 200)

        # check for Correct Template Used
        self.assertTemplateUsed(response, 'location_financial/location_financial_delete.html')




# ################################     View Testing End   #################################################


# ################################     Testing the URLs       ##############################################

class PagesTests(SimpleTestCase):

    # Check URL for list/ Home
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

# #-----------------------------------------------------------------------------------------------------#
