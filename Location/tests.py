from django.test import TestCase, SimpleTestCase
from django.urls import reverse, reverse_lazy
from .models import Location
from django.contrib.auth import get_user_model
from django.utils import timezone



# Tests for Location Application
class LocationTest(TestCase):

    ########################## Model Testing ############################

    # Location object with dummy data
    def setUp(self):

        self.user = get_user_model().objects.create_user(
            username='assissh',
            password='test'
        )

        self.Location = Location.objects.create(
            Location_Area = 'Area',
            Location_Authorities_Involved = self.user,
            Location_Budget=1,
            Location_City = 'City',
            Location_Description  = 'Description',
            Location_District = 'District',
            Location_Locality = 'Locality',
            Location_Name = 'Location_name',
            Location_Postal_Address = 'Location_postal_address',
            Location_Financial = 'Location_financial',
            Location_Creator = self.user,
            Location_Id = 1,
            Location_Latitude = 1,
            Location_Longitude = 1,
            Location_Subcategory = 'Location_subcategory',
            Location_Modifications_Allowed = 'Modifications_allowed',
            Location_Ownership_Status = 'Ownership_status',
            Location_Pincode = 1,
            Location_Restrictions = 'Restrictions',
            Location_State= 'State',
            Location_Street_Address = 'Street_address',
            Location_Surrounding = 'Surrounding',
            Location_Created_Date=timezone.now(),
            Location_Modified_Date= timezone.now()




        )

      # Check redirection URL
    def test_get_absolute_url(self):
         self.assertEquals(self.Location.get_absolute_url(),'/Location/1')

#     # Check Conent of Location object
    def test_Location_content(self):
        self.assertEqual(f'{self.Location.Location_Area}','Area')
        self.assertEqual(f'{self.Location.Location_Authorities_Involved}',self.user.username)
        self.assertEqual(f'{self.Location.Location_Budget}', '1')
        self.assertEqual(f'{self.Location.Location_City}', 'City')
        self.assertEqual(f'{self.Location.Location_Description}', 'Description')
        self.assertEqual(f'{self.Location.Location_District}', 'District')
        self.assertEqual(f'{self.Location.Location_Locality}', 'Locality')
        self.assertEqual(f'{self.Location.Location_Creator}',self.user.username)
        self.assertEqual(f'{self.Location.Location_Financial}', 'Location_financial')
        self.assertEqual(f'{self.Location.Location_Id}', '1')
        self.assertEqual(f'{self.Location.Location_Latitude}', '1')
        self.assertEqual(f'{self.Location.Location_Longitude}', '1')
        self.assertEqual(f'{self.Location.Location_Subcategory}', 'Location_subcategory')
        self.assertEqual(f'{self.Location.Location_Modifications_Allowed}', 'Modifications_allowed')
        self.assertEqual(f'{self.Location.Location_Id}', '1')
        self.assertEqual(f'{self.Location.Location_Modifications_Allowed}', 'Modifications_allowed')
        self.assertEqual(f'{self.Location.Location_Ownership_Status}', 'Ownership_status')
        self.assertEqual(f'{self.Location.Location_Restrictions}', 'Restrictions')
        self.assertEqual(f'{self.Location.Location_State}', 'State')
        self.assertEqual(f'{self.Location.Location_Street_Address}', 'Street_address')
        self.assertEqual(f'{self.Location.Location_Surrounding}', 'Surrounding')



#
#     # #############################   Model Test End   ###########################################
#
#     # ###############################    Views Test       ########################################
#
# #     # Test Location List View
    def test_LocationList_view(self):
         response = self.client.get(reverse('Location_list'))
         self.client.login(username='assissh',password='test')
         print(response)
         self.assertEqual(response.status_code, 200)
         self.assertEqual(f'{self.Location.Location_Creator}', self.user.username)
         self.assertTemplateUsed(response, 'Location/Location_list.html')

     # Test Location Detail View


    def test_LocationDetail_view(self):
        # Login the user defined in SetUp
        self.client.login(username='assissh', password='test')

        # Find primary key of table
        Location_pk = Location.objects.get(Location_Area='Area').pk
        # Get response
        response = self.client.get(reverse_lazy('Location_details', kwargs={'pk': Location_pk}))

        # Check for any invalid value
        no_response = self.client.get(reverse_lazy('Location_details', kwargs={'pk': 10000}))

        # 202 for valid and 404 for invalid
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        # Check for Correct template used in template/Locations
        self.assertTemplateUsed(response, 'Location/Location_detail.html')

    def test_Location_Create_view(self):
            # Login the user defined in SetUp
            self.client.login(username='assissh', password='test')
            # Generate response after creating an view using Http post method
            response = self.client.post('/Location/new/', {
                'Location_Area': 'Area',
                'Location_Authorities_Involved': 'Authorities_Involved',
                'Location_Location_Creater': self.user,  # Defined in setup
                'Location_Budget' : 1,
                'Location_City' : 'City',
                'Location_Description': 'Description',
                'Location_District': 'District',
                'Location_Locality ': 'Locality',
                'Location_Name': 'Location_name',
                'Location_Postal_Address ': 'Location_postal_address',
                'Location_Financial': 'Location_financial',
                'Location_Id': 1,
                'Location_Latitude': 1,
                'Location_Longitude': 1,
                'Location_Subcategory': 'Location_subcategory',
                'Location_Modifications_Allowed': 'Modifications_allowed',
                'Location_Ownership_Status': 'Ownership_status',
                'Location_Pincode' : 1,
                'Location_Restrictions': 'Restrictions',
                'Location_State': 'State',
                'Location_Street_Address':'Street_address',
                'Location_Surrounding': 'Surrounding',
                'Location_Modified_Date': timezone.now(),
                'Location_Created_Date': timezone.now(),
            })

            # Check for successful response
            self.assertEqual(response.status_code, 200)

            # Check response values
            self.assertContains(response, 'Area')
            self.assertContains(response, 'Authorities_Involved')
            self.assertContains(response, 1)
            self.assertContains(response, 'City')
            self.assertContains(response, 'Description')
            self.assertContains(response, 'District')
            self.assertContains(response, 'Locality')
            self.assertContains(response, 'Location_name')
            self.assertContains(response, 'Location_postal_address')
            self.assertContains(response, 'Location_financial')
            self.assertContains(response, 1)
            self.assertContains(response, 1)
            self.assertContains(response, 1)
            self.assertContains(response, 'Modifications_allowed')
            self.assertContains(response, 'Ownership_status')
            self.assertContains(response, 1)
            self.assertContains(response, 'Restrictions')
            self.assertContains(response, 'State')
            self.assertContains(response, 'Street_address')
            self.assertContains(response, 'Surrounding')
            self.assertContains(response, self.user.username)  # Same as defined in SetUp

            # Check for correct template used in template/Locations
            self.assertTemplateUsed(response, 'Location/Location_new.html')

            # Test Location Update view


    def Location_update_view(self):
        # Login the user
        self.client.login(username='assissh', password='test')
        print(self.user.username)

        # Find primary key of table
        Location_pk = Location.objects.get(Locaon_Area='Locatn_Area').pk
        print(self.user.username)
        # Get response using pk on details view
        response = self.client.get(reverse_lazy('Location_details', kwargs={'pk': Location_pk}), {
                    'Area': 'Area',
                    'Authorities_involved ': 'Authorities_involved',
                    'Location_creater': self.user,  # Defined in setup
                    'Budget': 1,
                    'City': 'City',
                    'Description': 'Description',
                    'District': 'District',
                    'Locality ': 'Locality',
                    'Location_name': 'Location_name',
                    'Location_postal_address ': 'Location_postal_address',
                    'Location_financial': 'Location_financial',
                    'Location_id': 1,
                    'Location_latitude': 1,
                    'Location_longitude': 1,
                    'Location_subcategory': 'Location_subcategory',
                    'Modifications_allowed': 'Modifications_allowed',
                    'Ownership_status': 'Ownership_status',
                    'Pincode': 1,
                    'Restrictions': 'Restrictions',
                    'State': 'State',
                    'Street_address': 'Street_address',
                    'Surrounding': 'Surrounding',
                    'Location_Modified_Date': timezone.now(),
                    'Location_Created_Date': timezone.now(),
                })
        # Check for successful response
        self.assertEqual(response.status_code, 200)
        print(self.user.username)
        # Check for correct templates
        self.assertTemplateUsed(response, 'Location/Location_update.html')


    def test_Locationdelete_view(self):
        # Login the user
        self.client.login(username='assissh', password='test')

        # Find primary key of table
        Location_pk = Location.objects.get(Location_Area='Area').pk
        # Get response to delete

        response = self.client.get(reverse_lazy('Location_delete', kwargs={'pk': Location_pk}))
        self.assertContains(response, 'Are you sure you want to delete')  # THIS PART WORKS

        # Check deleted value , returns false i.e.302
        post_response = self.client.post(reverse_lazy('Location_delete', kwargs={'pk': Location_pk}))



        self.assertEqual(response.status_code, 200)

        # check for Correct Template Used
        self.assertTemplateUsed(response, 'Location/Location_delete.html')
#
# # # ################################     View Testing End   ##############################################
# #
# # # ################################     Testing URLs       ##############################################
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
# # def test_new_page_status_code(self):
# #         # Login the user defined in SetUp
# #         self.client.login(username='assissh', password='test')
# #
# #         # Get response
# #         response = self.client.get('/Location/1/')
# #
# #         self.assertEqual(response.status_code, 200)
# #
# # # def test_update_page_status_code(self):
# #         url = reverse('LocationListView')
# #         response = self.client.get('/Lettzkxudh/1/')
# #         self.assertEqual(response.status_code, 200)
# # #
# # def test_detail_page_status_code(self):
# #         response = self.client.get('/{1}/')
# #         self.assertEqual(response.status_code, 200)
# #
# # def test_delete_page_status_code(self):
# #                 response = self.client.get('/{1}/delete/')
# #                 self.assertEqual(response.status_code, 200)
