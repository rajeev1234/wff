from django.test import TestCase, SimpleTestCase
from django.urls import reverse, reverse_lazy
from .models import Location_Amenitie
from django.contrib.auth import get_user_model
from django.utils import timezone


# Tests for Location_Amenitie Application
class Location_AmenitieTest(TestCase):

    ########################## Model Testing ############################

    # Location_Amenitie object with dummy data
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='assissh',
            password='test'
        )

        self.Location_Amenitie = Location_Amenitie.objects.create(
            Location_Amenitie_Carparking=True,
            Location_Amenitie_Carparking_Latitide=1,
            Location_Amenitie_Carparking_Longitude=1,
            Location_Amenitie_Catering_Base=True,
            Location_Amenitie_Catering_Base_Latitude=1,
            Location_Amenitie_Catering_Base_Longitude=1,
            Location_Amenitie_Controlling_Status='Location_Amenitie_Controlling_Status',
            Location_Amenitie_Genset_Parking=True,
            Location_Amenitie_Genset_Parking_Latitude=1,
            Location_Amenitie_Genset_Parking_Longitude=1,
            Location_Amenitie_Location_Id=1,
            Location_Amenitie_Truck_Parking_Latitude=1,
            Location_Amenitie_Truck_Parking_Longitude=1,
            Location_Amenitie_Vanity_Parking=True,
            Location_Amenitie_Vanity_Parking_Latitude=1,
            Location_Amenitie_Vanity_Parking_Longitude=1,
            Location_Amenitie_Washroom=True,
            Location_Amenitie_Creator=self.user,
            Location_Amenitie_Modified_Date=timezone.now(),
            Location_Amenitie_Created_Date=timezone.now(),

        )

    # Check redirection URL
    def test_get_absolute_url(self):
        self.assertEquals(self.Location_Amenitie.get_absolute_url(), '/Location_Amenitie/1')

    #     # Check Conent of Location_Amenitie object
    def test_Location_Amenitie_content(self):
        self.assertEqual(f'{self.Location_Amenitie.Location_Amenitie_Carparking}', 'True')
        self.assertEqual(f'{self.Location_Amenitie.Location_Amenitie_Carparking_Latitide}', '1')
        self.assertEqual(f'{self.Location_Amenitie.Location_Amenitie_Carparking_Longitude}', '1')
        self.assertEqual(f'{self.Location_Amenitie.Location_Amenitie_Catering_Base}', 'True')
        self.assertEqual(f'{self.Location_Amenitie.Location_Amenitie_Catering_Base_Latitude}', '1')
        self.assertEqual(f'{self.Location_Amenitie.Location_Amenitie_Catering_Base_Longitude}', '1')
        self.assertEqual(f'{self.Location_Amenitie.Location_Amenitie_Controlling_Status}',
                         'Location_Amenitie_Controlling_Status')
        self.assertEqual(f'{self.Location_Amenitie.Location_Amenitie_Genset_Parking}', 'True')
        self.assertEqual(f'{self.Location_Amenitie.Location_Amenitie_Genset_Parking_Latitude}', '1')
        self.assertEqual(f'{self.Location_Amenitie.Location_Amenitie_Genset_Parking_Longitude}', '1')
        self.assertEqual(f'{self.Location_Amenitie.Location_Amenitie_Location_Id}', '1')
        self.assertEqual(f'{self.Location_Amenitie.Location_Amenitie_Truck_Parking_Latitude}', '1')
        self.assertEqual(f'{self.Location_Amenitie.Location_Amenitie_Truck_Parking_Longitude}', '1')
        self.assertEqual(f'{self.Location_Amenitie.Location_Amenitie_Vanity_Parking}', 'True')
        self.assertEqual(f'{self.Location_Amenitie.Location_Amenitie_Vanity_Parking_Latitude}', '1')
        self.assertEqual(f'{self.Location_Amenitie.Location_Amenitie_Vanity_Parking_Longitude}', '1')
        self.assertEqual(f'{self.Location_Amenitie.Location_Amenitie_Washroom}', 'True')
        self.assertEqual(f'{self.Location_Amenitie.Location_Amenitie_Creator}', self.user.username)

    #
    #     # #############################   Model Test End   ###########################################
    #
    #     # ###############################    Views Test       ########################################

    #     # Test Location_Amenitie List View
    def test_Location_AmenitieList_view(self):
        # print('This is response')
        response = self.client.get(reverse('Location_Amenitie_list'))
        self.client.login(username='assissh', password='test')
        # print(response)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(f'{self.Location_Amenitie.Location_Amenitie_Creator}', self.user.username)
        # print(self.user.username)
        self.assertTemplateUsed(response, 'Location_Amenitie/Location_Amenitie_list.html')

    #      # Test Location_Amenitie Detail View
    #
    #
    def test_Location_AmenitieDetail_view(self):
        # print('This is response')
        # Login the user defined in SetUp
        self.client.login(username='assissh', password='test')

        # Find primary key of table
        Location_Amenitie_pk = Location_Amenitie.objects.get(
            Location_Amenitie_Controlling_Status='Location_Amenitie_Controlling_Status').pk

        # Get response
        response = self.client.get(reverse_lazy('Location_Amenitie_details', kwargs={'pk': Location_Amenitie_pk}))

        # Check for any invalid value
        no_response = self.client.get(reverse_lazy('Location_Amenitie_details', kwargs={'pk': 10000}))

        # 202 for valid and 404 for invalid
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)

        # check for content of Detail Page
        self.assertContains(response, 'Location_Amenitie_Controlling_Status')

        # Check for Correct template used in template/Location_Amenities
        self.assertTemplateUsed(response, 'Location_Amenitie/Location_Amenitie_detail.html')

    def test_Location_Create_view(self):
        # Login the user defined in SetUp
        self.client.login(username='assissh', password='test')

        # Generate response after creating an view using Http post method
        response = self.client.post('/Location_Amenitie/new/', {
            'Location_Amenitie_Carparking': True,
            'Location_Amenitie_Carparking_Latitide': 0,
            'Location_Amenitie_Carparking_Longitude': 0,  # Defined in setup
            'Location_Amenitie_Catering_Base': False,
            'Location_Amenitie_Catering_Base_Latitude': 0,
            'Location_Amenitie_Catering_Base_Longitude': 0,
            'Location_Amenitie_Controlling_Status': 'Location_Amenitie_Controlling_Status',
            'Location_Amenitie_Genset_Parking': True,
            'Location_Amenitie_Genset_Parking_Latitude': 0,
            'Location_Amenitie_Genset_Parking_Longitude': 0,
            'Location_Amenitie_Location_Id': False,
            'Location_Amenitie_Truck_Parking_Latitude': 0,
            'Location_Amenitie_Truck_Parking_Longitude': 0,
            'Location_Amenitie_Vanity_Parking': True,
            'Location_Amenitie_Vanity_Parking_Latitude': 0,
            'Location_Amenitie_Vanity_Parking_Longitude': 0,
            'Location_Amenitie_Washroom': True,
            'Location_Amenitie_Creator': self.user,
            'Location_Modified_Date': timezone.now(),
            'Location_Created_Date': timezone.now(),
        })

        # print('This is response')
        # print(response.content)
        self.assertEqual(response.status_code, 200)

        # Check response values
        self.assertContains(response, 'checked')
        self.assertContains(response, 0)
        self.assertContains(response, 0)
        self.assertContains(response, 0)
        self.assertContains(response, 'checked')
        self.assertContains(response, 0)
        self.assertContains(response, 0)
        self.assertContains(response, 'Location_Amenitie_Controlling_Status')
        self.assertContains(response, 'checked')
        self.assertContains(response, 0)
        self.assertContains(response, 0)
        self.assertContains(response, 'checked')
        self.assertContains(response, 0)
        self.assertContains(response, 0)
        self.assertContains(response, 'checked')
        self.assertContains(response, 0)
        self.assertContains(response, 0)
        self.assertContains(response, 'checked')
        self.assertContains(response, self.user.username)  # Same as defined in SetUp

        # Check for correct template used in template/Locations
        self.assertTemplateUsed(response, 'Location_Amenitie/Location_Amenitie_new.html')

        # Test Location Update view

    def Location_Amenitie_update_view(self):
        # Login the user
        self.client.login(username='assissh', password='test')

        # Find primary key of table
        Location_Amenitie_pk = Location_Amenitie.objects.get(Area='Area').pk

        # Get response using pk on details view
        response = self.client.get(reverse_lazy('Location_details', kwargs={'pk': Location_Amenitie_pk}), {
            'Location_Amenitie_Carparking': 'Location_Amenitie_Carparking',
            'Location_Amenitie_Carparking_Latitide': 1,
            'Location_Amenitie_Carparking_Longitude': 1,
            'Location_Amenitie_Catering_Base': True,
            'Location_Amenitie_Catering_Base_Latitude': 1,
            'Location_Amenitie_Catering_Base_Longitude': 1,
            'Location_Amenitie_Controlling_Status': 'Location_Amenitie_Controlling_Status',
            'Location_Amenitie_Genset_Parking': True,
            'Location_Amenitie_Genset_Parking_Latitude': 1,
            'Location_Amenitie_Genset_Parking_Longitude': 1,
            'Location_Amenitie_Location_Id': True,
            'Location_Amenitie_Truck_Parking_Latitude': 1,
            'Location_Amenitie_Truck_Parking_Longitude': 1,
            'Location_Amenitie_Vanity_Parking': True,
            'Location_Amenitie_Vanity_Parking_Latitude': 1,
            'Location_Amenitie_Vanity_Parking_Longitude': 1,
            'Location_Amenitie_Washroom': True,
            'Location_Amenitie_Creator': self.user,
            'Location_Modified_Date': timezone.now(),
            'Location_Created_Date': timezone.now(),
        })
        # Check for successful response
        self.assertEqual(response.status_code, 200)

        # Check for correct templates
        self.assertTemplateUsed(response, 'Location_Amenitie/Location_Amenitie_update.html')

        #

    def test_Locationdelete_view(self):
        # Login the user
        self.client.login(username='assissh', password='test')

        # Find primary key of table
        Location_Amenitie_pk = Location_Amenitie.objects.get(
            Location_Amenitie_Controlling_Status='Location_Amenitie_Controlling_Status').pk

        # Get response to delete

        response = self.client.get(reverse_lazy('Location_Amenitie_delete', kwargs={'pk': Location_Amenitie_pk}))
        self.assertContains(response, 'Are you sure you want to delete')  # THIS PART WORKS

        # Check deleted value , returns false i.e.302
        post_response = self.client.post(reverse_lazy('Location_Amenitie_delete', kwargs={'pk': Location_Amenitie_pk}))

        # self.assertRedirects(post_response, reverse_lazy('Location_delete', kwargs={'pk': Location_Amenitie_pk}), status_code=302)

        self.assertEqual(response.status_code, 200)

        # check for Correct Template Used
        self.assertTemplateUsed(response, 'Location_Amenitie/Location_Amenitie_delete.html')

        # # # ################################     View Testing End   ##############################################
        # #
        # # # ################################     Testing URLs       ##############################################
        #
        #
        #
        #


#
#
class PagesTests(SimpleTestCase):

    # Check URL for list
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
#
# #URLfor update
#     def test_new_page_status_code(self):
#         # Login the user defined in SetUp
#         self.client.login(username='assissh', password='test')

# #         # Get response
#         response = self.client.get('/Location_Amenitie/1/')

# self.assertEqual(response.status_code, 200)

#     def test_update_page_status_code(self):
#         url = reverse('LocationListView')
#         response = self.client.get('/Location_Amenitie/1/')
#         self.assertEqual(response.status_code, 200)
# #
#     def test_detail_page_status_code(self):
#         response = self.client.get('/{1}/')
#         self.assertEqual(response.status_code, 200)

#     def test_delete_page_status_code(self):
#         response = self.client.get('/{1}/delete/')
#         self.assertEqual(response.status_code, 200)

