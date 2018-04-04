from django.test import TestCase, SimpleTestCase
from django.urls import reverse, reverse_lazy
from .models import LocationAuthority
from django.contrib.auth import get_user_model
from django.utils import timezone


# Tests for Location_Authority Application
class Location_AuthorityTest(TestCase):

    ######################### Model Testing ############################

    #Location_Authority object with dummy data
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='assissh',
            password='test'
        )


        self.Location_Authority = LocationAuthority.objects.create(
            Location_Authority_Detail = 'Location_Authority_Detail',
            Location_Authority_Email = 'Location_Authority_Email',
            Location_Authority_Google_Address = 'Location_Authority_Google_Address',
            Location_Authority_Latitude = 1,
            Location_Authority_Longitude = 1,
            Location_Authority_Name = 1,
            Location_Authority_Postal_Address = 'Location_Authority_Postal_Address',
            Location_Authority_Contact_Number = 1,
            Location_Authority_Contact_Name = 'Location_Authority_Contact_Name',
            Location_Authority_Locality_City_State = 'Location_Authority_Locality_City_State',
            Location_Authority_Location_ID = 1,
            Location_Authority_Office_Charges = 1,
            Location_Authority_Street_Address = 'Location_Authority_Street_Address',
            Location_Authority_Creator = self.user,
            Location_Authority_Modified_Date = timezone.now(),
            Location_Authority_Created_Date = timezone.now(),

        )

    # Check redirection URL
    def test_get_absolute_url(self):
        self.assertEquals(self.Location_Authority.get_absolute_url(), '/Location_Authoritie/1')

        # Check Conent of Location_Authority object
    def test_Location_Authority_content(self):

        self.assertEqual(f'{self.Location_Authority.Location_Authority_Detail}', 'Location_Authority_Detail')
        self.assertEqual(f'{self.Location_Authority.Location_Authority_Email}', 'Location_Authority_Email')
        self.assertEqual(f'{self.Location_Authority.Location_Authority_Google_Address}', 'Location_Authority_Google_Address')
        self.assertEqual(f'{self.Location_Authority.Location_Authority_Latitude}', '1')
        self.assertEqual(f'{self.Location_Authority.Location_Authority_Longitude}', '1')
        self.assertEqual(f'{self.Location_Authority.Location_Authority_Name}', '1')
        self.assertEqual(f'{self.Location_Authority.Location_Authority_Postal_Address}','Location_Authority_Postal_Address')
        self.assertEqual(f'{self.Location_Authority.Location_Authority_Contact_Number}', '1')
        self.assertEqual(f'{self.Location_Authority.Location_Authority_Contact_Name}', 'Location_Authority_Contact_Name')
        self.assertEqual(f'{self.Location_Authority.Location_Authority_Locality_City_State}', 'Location_Authority_Locality_City_State')
        self.assertEqual(f'{self.Location_Authority.Location_Authority_Location_ID}', '1')
        self.assertEqual(f'{self.Location_Authority.Location_Authority_Office_Charges}', '1')
        self.assertEqual(f'{self.Location_Authority.Location_Authority_Street_Address}', 'Location_Authority_Street_Address')
        self.assertEqual(f'{self.Location_Authority.Location_Authority_Creator}', self.user.username)

    def test_Location_AuthorityList_view(self):
            # print('This is response')
            response = self.client.get(reverse('Location_Authorities_list'))
            self.client.login(username='assissh', password='test')
            # print(response)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(f'{self.Location_Authority.Location_Authority_Creator}', self.user.username)
            # print(self.user.username)
            self.assertTemplateUsed(response, 'Location_Authorities/Location_Authorities_list.html')

         # Test Location_Authority Detail View

    def test_Location_AuthorityDetail_view(self):
        # print('This is response')
        # Login the user defined in SetUp
        self.client.login(username='assissh', password='test')

        # Find primary key of table
        Location_Authority_pk = LocationAuthority.objects.get(
            Location_Authority_Detail='Location_Authority_Detail').pk

        # Get response
        response = self.client.get(reverse_lazy('Location_Authorities_details', kwargs={'pk': Location_Authority_pk}))

        # Check for any invalid value
        no_response = self.client.get(reverse_lazy('Location_Authorities_details', kwargs={'pk': 10000}))

        # 202 for valid and 404 for invalid
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)

        # check for content of Detail Page
        self.assertContains(response, 'Location_Authority_Detail')

        # Check for Correct template used in template/Location_Authoritys
        self.assertTemplateUsed(response, 'Location_Authorities/Location_Authorities_detail.html')

    def test_Location_Create_view(self):
            # Login the user defined in SetUp
            self.client.login(username='assissh', password='test')

            # Generate response after creating an view using Http post method
            response = self.client.post('/Location_Authoritie/new/', {
                'Location_Authority_Detail ': 'Location_Authority_Detail',
                'Location_Authority_Email ': 'Location_Authority_Email',
                'Location_Authority_Google_Address ': 'Location_Authority_Google_Address',  # Defined in setup
                'Location_Authority_Latitude ': 1,
                'Location_Authority_Longitude ': 1,
                'Location_Authority_Name ': 'Location_Authority_Name',
                'Location_Authority_Postal_Address ': 'Location_Authority_Controlling_Status',
                'Location_Authority_Contact_Number ': 1,
                'Location_Authority_Contact_Name ': 'Location_Authority_Contact_Name',
                '#Location_Authoritie_Contact_Officer ': 1,
                'Location_Authority_Locality_City_State ': 'Location_Authority_Locality_City_State',
                'Location_Authority_Location_ID ': 1,
                'Location_Authority_Office_Charges ': 1,
                'Location_Authority_Street_Address ': 'Location_Authority_Street_Address',
                'Location_Authority_Creator ': self.user,
                'Location_Authority_Modified_Date ': timezone.now(),
                'Location_Authority_Created_Date ': timezone.now(),
            })

            # print('This is response')

            self.assertEqual(response.status_code, 200)

            # Check response values
            self.assertContains(response, 'Location_Authority_Detail')
            self.assertContains(response, 'Location_Authority_Email')
            self.assertContains(response, 1)
            self.assertContains(response, 1)
            self.assertContains(response, 'Location_Authority_Name')
            self.assertContains(response, 'Location_Authority_Controlling_Status')
            self.assertContains(response, 1)
            self.assertContains(response, 'Location_Authority_Contact_Name')
            self.assertContains(response, 1)
            self.assertContains(response, 'Location_Authority_Locality_City_State')
            self.assertContains(response, 1)
            self.assertContains(response, 1)
            self.assertContains(response, 'Location_Authority_Street_Address')
            self.assertContains(response, self.user.username)  # Same as defined in SetUp

            # Check for correct template used in template/Locations
            self.assertTemplateUsed(response, 'Location_Authorities/Location_Authorities_new.html')



        # Test Location Update view

    def Location_Authority_update_view(self):

        self.client.login(username='assissh', password='test')
        print(self.user.username)

        # Find primary key of table
        Location_Authority_pk = LocationAuthority.objects.get(
            Location_Authority_Detail='Location_Authority_Detail').pk

        # Get response to delete

        response = self.client.get(reverse_lazy('Location_Authority_delete', kwargs={'pk': Location_Authority_pk}))
        self.assertContains(response, 'Are you sure you want to delete')  # THIS PART WORKS

        # Check deleted value , returns false i.e.302
        post_response = self.client.post(reverse_lazy('Location_Authority_delete', kwargs={'pk': Location_Authority_pk}))

        # self.assertRedirects(post_response, reverse_lazy('Location_delete', kwargs={'pk': Location_Authority_pk}), status_code=302)

        self.assertEqual(response.status_code, 200)

        # check for Correct Template Used
        self.assertTemplateUsed(response, 'Location_Authority/Location_Authority_delete.html')

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
# # #URLfor update
# #     def test_new_page_status_code(self):
# #         # Login the user defined in SetUp
# #         self.client.login(username='assissh', password='test')
#
# # #         # Get response
# #         response = self.client.get('/Location_Authority/1/')
#
# # self.assertEqual(response.status_code, 200)
#
# #     def test_update_page_status_code(self):
# #         url = reverse('LocationListView')
# #         response = self.client.get('/Location_Authority/1/')
# #         self.assertEqual(response.status_code, 200)
# # #
# #     def test_detail_page_status_code(self):
# #         response = self.client.get('/{1}/')
# #         self.assertEqual(response.status_code, 200)
#
# #     def test_delete_page_status_code(self):
# #         response = self.client.get('/{1}/delete/')
# #         self.assertEqual(response.status_code, 200)
#
