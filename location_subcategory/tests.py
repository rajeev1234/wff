from django.test import TestCase,SimpleTestCase
from django.urls import reverse,reverse_lazy
from .models import LocationSubCategory
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils import timezone


#  Test Class for LocationSubCategory Application

class LocationSubCategoryTest(TestCase):

########################## Model Testing ############################


    # LocationSubCategory object with dummy data
    def setUp(self):

        # dummy user for login
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password = 'test'
        )

        self.LocationSubCategory =  LocationSubCategory.objects.create(

        # Fields according to defined in Model
        LocationSubCategory_Location_Category = 'LocationSubCategory_Location_Category',
        Location_Subcategory='Location_Subcategory',
        LocationSubCategory_Subcategory_No='LocationSubCategory_Subcategory_No',
        LocationSubCategory_Modified_Date=timezone.now(),
        LocationSubCategory_Message = 'LocationSubCategory_Message',
        LocationSubCategory_Author = self.user,      # Defined above in get_user_model
        LocationSubCategory_Created_Date = timezone.now(),
        )

#-----------------------------------------------------------------------------------------#

    # Check redirection URL
    def test_get_absolute_url(self):
        # Redirection goes to LocationSubCategory details
        self.assertEquals(self.LocationSubCategory.get_absolute_url(), '/location_subcategory/1')

#-----------------------------------------------------------------------------------------#

    # Check Conent of LocationSubCategory object created by create object query set
    def test_LocationSubCategory_content(self):
        # Verify for each field
        self.assertEqual(f'{self.LocationSubCategory.LocationSubCategory_Location_Category}', 'LocationSubCategory_Location_Category')
        self.assertEqual(f'{self.LocationSubCategory.Location_Subcategory}', 'Location_Subcategory')
        self.assertEqual(f'{self.LocationSubCategory.LocationSubCategory_Subcategory_No}', 'LocationSubCategory_Subcategory_No')
        self.assertEqual(f'{self.LocationSubCategory.LocationSubCategory_Message}', 'LocationSubCategory_Message')
        self.assertEqual(f'{self.LocationSubCategory.LocationSubCategory_Author}', self.user.username)      # Defined in SetUp


#--------------------------------------------------------------------------------------------#

# #############################   Model Test End   ########################################### #


# ###############################    Views Test       ########################################


    # Test LocationSubCategory List View

    def test_LocationSubCategoryList_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test')

        # Get response from defined URL namespace
        response = self.client.get(reverse('location_subcategory_list'))
        self.assertEqual(response.status_code, 200)

        # Check Content of List View
        self.assertContains(response, self.user.username)
        # Check for Correct template used in template/LocationSubCategorys
        self.assertTemplateUsed(response, 'location_subcategorys/location_subcategory_list.html')

#--------------------------------------------------------------------------------------------#

    # Test LocationSubCategory Detail View

    def test_LocationSubCategoryDetail_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test')

        # Find primary key of table
        LocationSubCategory_pk = LocationSubCategory.objects.get(Location_Subcategory = 'Location_Subcategory').pk

        # Get response
        response = self.client.get(reverse_lazy('location_subcategory_details',kwargs={'pk':LocationSubCategory_pk}))

        # Check for any invalid value
        no_response = self.client.get(reverse_lazy('location_subcategory_details',kwargs={'pk':10000}))

        # 202 for valid and 404 for invalid
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)

        # check for content of Detail Page
        self.assertContains(response, 'Location_Subcategory')

        # Check for Correct template used in template/LocationSubCategorys
        self.assertTemplateUsed(response, 'location_subcategorys/location_subcategory_detail.html')

#-------------------------------------------------------------------------------------------#


    # Test EducationInfo Create View

    def test_LocationSubCategoryCreate_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test')

        # Generate response after creating an view using Http post method
        response = self.client.post('/location_subcategory/new/', {
        'LocationSubCategory_Location_Category' : 'LocationSubCategory_Location_Category',
        'Location_Subcategory':'Location_Subcategory',
        'LocationSubCategory_Subcategory_No':'LocationSubCategory_Subcategory_No',
        'LocationSubCategory_Modified_Date':timezone.now(),
        'LocationSubCategory_Message' : 'LocationSubCategory_Message',
        'LocationSubCategory_Author' : self.user,      # Defined above in get_user_model
        'LocationSubCategory_Created_Date' : timezone.now()
        },follow = True)

        # print(response.content)
        # Check for successful response
        self.assertEqual(response.status_code, 200)
        # self.assertContains(response, False)
        self.assertContains(response, 'LocationSubCategory_Location_Category')
        self.assertContains(response, 'Location_Subcategory')
        self.assertContains(response, 'LocationSubCategory_Subcategory_No')
        self.assertContains(response, 'LocationSubCategory_Message')
        self.assertContains(response, self.user.username)       # Same as defined in SetUp

        # Check for correct template used in template/EducationInfos
        self.assertTemplateUsed(response, 'location_subcategorys/location_subcategory_detail.html')

#---------------------------------------------------------------------------------------#


    # Test EducationInfo Update view

    def test_LocationSubCategoryupdate_view(self):
        # Login the user
        self.client.login(username='testuser', password='test')

        # Find primary key of table
        LocationSubCategory_pk = LocationSubCategory.objects.get(Location_Subcategory='Location_Subcategory').pk

        # Get response using pk on details view
        response = self.client.get(reverse_lazy('location_subcategory_details',kwargs={'pk':LocationSubCategory_pk}), {
        'LocationSubCategory_Location_Category' : 'LocationSubCategory_Location_Category',
        'Location_Subcategory':'Location_Subcategory',
        'LocationSubCategory_Subcategory_No':'LocationSubCategory_Subcategory_No',
        'LocationSubCategory_Modified_Date':timezone.now(),
        'LocationSubCategory_Message' : 'LocationSubCategory_Message',
        'LocationSubCategory_Author' : self.user,      # Defined above in get_user_model
        'LocationSubCategory_Created_Date' : timezone.now(),
        },follow = True)
        # Check for successful response
        self.assertEqual(response.status_code, 200)

        # Check for correct templates
        self.assertTemplateUsed(response,'location_subcategorys/location_subcategory_detail.html')


#--------------------------------------------------------------------------------------------#


# Test Delete View of EducationInfo views

    def test_LocationSubCategorydelete_view(self):
        # Login the user
        self.client.login(username='testuser', password='test')

        # Find primary key of table
        LocationSubCategory_pk = LocationSubCategory.objects.get(Location_Subcategory='Location_Subcategory').pk

        # Get response to delete

        response = self.client.get(reverse_lazy('location_subcategory_delete',kwargs={'pk':LocationSubCategory_pk}))
        self.assertContains(response, 'Are you sure you want to delete') # THIS PART WORKS

        # Check deleted value , returns false i.e.302
        post_response = self.client.post(reverse_lazy('location_subcategory_delete',kwargs={'pk':LocationSubCategory_pk}))

        # self.assertRedirects(post_response, reverse_lazy('EducationInfo_delete',kwargs={'pk':EducationInfo_pk}), status_code=302)


        self.assertEqual(response.status_code, 200)

        # check for Correct Template Used
        self.assertTemplateUsed(response, 'location_subcategorys/location_subcategory_delete.html')




# ################################     View Testing End   #################################################


# ################################     Testing the URLs       ##############################################

class PagesTests(SimpleTestCase):

    # Check URL for list/ Home
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

# #-----------------------------------------------------------------------------------------------------#
