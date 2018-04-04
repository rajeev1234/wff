from django.test import TestCase, SimpleTestCase
from django.urls import reverse, reverse_lazy
from .models import Location_Category
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.forms.models import model_to_dict


#  Test Class for Location_Category Application

class Location_CategoryTest(TestCase):

    ########################## Model Testing ############################

    # Location_Category object with dummy data
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='test'
        )

        self.Location_Category = Location_Category.objects.create(

            # Fields according to defined in Model
            Location_Category_No=1,
            Location_Category_Name='Location_Category_Name',

            Location_Category_Creator=self.user,
            Location_Category_Modified_Date=timezone.now(),
            Location_Category_Created_Date=timezone.now(),
        )

    # -----------------------------------------------------------------------------------------#

    # Check redirection URL
    def test_get_absolute_url(self):
        # Redirection goes to Location_Category details
        self.assertEquals(self.Location_Category.get_absolute_url(), '/Location_Category/1')

    # -----------------------------------------------------------------------------------------#

    # Check Conent of Location_Category object created by create object query set
    def test_Location_Category_content(self):
        # Verify for each field
        self.assertEqual(f'{self.Location_Category.Location_Category_No}', '1')
        self.assertEqual(f'{self.Location_Category.Location_Category_Name}', 'Location_Category_Name')

        self.assertEqual(f'{self.Location_Category.Location_Category_Creator}', self.user.username)

    # --------------------------------------------------------------------------------------------#

    # #############################   Model Test End   ###########################################

    # ###############################    Views Test       ########################################

    # Test Location_Category List View

    def test_Location_CategoryList_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test')

        # Get respomse from defined URL namespace
        response = self.client.get(reverse('Location_Category_list'))
        self.assertEqual(response.status_code, 200)

        # Check Content of List View
        self.assertContains(response, self.user.username)

        # Check for Correct template used in template/Location_Categorys
        self.assertTemplateUsed(response, 'Location_Category/Location_Category_list.html')

    # --------------------------------------------------------------------------------------------#

    # Test Location_Category Detail View

    def test_Location_CategoryDetail_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test')

        # Find primary key of table
        Location_Category_pk = Location_Category.objects.get(Location_Category_Name='Location_Category_Name').pk

        # Get response
        response = self.client.get(reverse_lazy('Location_Category_details', kwargs={'pk': Location_Category_pk}))

        # Check for any invalid value
        no_response = self.client.get(reverse_lazy('Location_Category_details', kwargs={'pk': 10000}))

        # 202 for valid and 404 for invalid
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)

        # check for content of Detail Page

        # Check for Correct template used in template/Location_Categorys
        self.assertTemplateUsed(response, 'Location_Category/Location_Category_detail.html')

    # -------------------------------------------------------------------------------------------#

    #Test Location_Category Create View

    def test_Location_CategoryCreate_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test')

        # Generate response after creating an view using Http post method
        response = self.client.post('/Location_Category/new/', {
            'Location_Category_No': 'Location_Category_No',
            'Location_Category_Name': 'Location_Category_Name',

            'Location_Category_Creator': self.user,  # Defined in setup
            'Location_Category_Modified_Date': timezone.now(),
            'Location_Category_Created_Date': timezone.now(),
        })

        # Check for successful response
        self.assertEqual(response.status_code, 200)

        # Check response values
        self.assertContains(response, 'Location_Category_No')
        self.assertContains(response, 'Location_Category_Name')
        self.assertContains(response, self.user.username)  # Same as defined in SetUp

        # Check for correct template used in template/Location_Categorys
        self.assertTemplateUsed(response, 'Location_Category/Location_Category_new.html')

    # ---------------------------------------------------------------------------------------#

    # Test Location_Category Update view

    def test_Location_Categoryupdate_view(self):
        # Login the user
        self.client.login(username='testuser', password='test')

        # Find primary key of table
        Location_Category_pk = Location_Category.objects.get(Location_Category_Name='Location_Category_Name').pk

        # Get response using pk on details view
        response = self.client.get(reverse_lazy('Location_Category_details', kwargs={'pk': Location_Category_pk}), {
            'Location_Category_No': 1,
            'Location_Category_Name': 'Location_Category_Name',
            'Location_Category_Creator': self.user.username,
            'Location_Category_Modified_Date': timezone.now(),
            'Location_Category_Created_Date': timezone.now(),
        })
        # Check for successful response
        self.assertEqual(response.status_code, 200)

        # Check for correct templates
        self.assertTemplateUsed(response, 'Location_Category/Location_Category_detail.html')

    # --------------------------------------------------------------------------------------------#

    # Test Delete View of Location_Category views

    def test_Location_Categorydelete_view(self):
        # Login the user
        self.client.login(username='testuser', password='test')

        # Find primary key of table
        Location_Category_pk = Location_Category.objects.get(Location_Category_Name='Location_Category_Name').pk

        # Get response to delete

        response = self.client.get(reverse_lazy('Location_Category_delete', kwargs={'pk': Location_Category_pk}))
        self.assertContains(response, 'Are you sure you want to delete')  # THIS PART WORKS

        # Check deleted value , returns false i.e.302
        post_response = self.client.post(reverse_lazy('Location_Category_delete', kwargs={'pk': Location_Category_pk}))

        # self.assertRedirects(post_response, reverse_lazy('Location_Category_delete',kwargs={'pk':Location_Category_pk}), status_code=302)

        self.assertEqual(response.status_code, 200)

        # check for Correct Template Used
        self.assertTemplateUsed(response, 'Location_Category/Location_Category_delete.html')


################################     View Testing End   #################################################


# ################################     Testing the URLs       ##############################################

class PagesTests(SimpleTestCase):

    # Check URL for list/ Home
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

#-----------------------------------------------------------------------------------------------------#

#     # URL for new
#     def test_new_page_status_code(self):
#         # Login the user defined in SetUp
#         # self.client.login(username='testuser', password='test')

#         # Get response
#         response = self.client.get('/Location_Categorys/1/')

#         self.assertEqual(response.status_code, 200)


# ------------------------------------------------------------------------------------------------------#


#     # def test_update_page_status_code(self):
#     #     # url = reverse('Location_CategoryListView')
#     #     response = self.client.get('/Location_Categorys/1/')
#     #     self.assertEqual(response.status_code, 200)

# -------------------------------------------------------------------------------------------------------#

#     # def test_detail_page_status_code(self):
#     #     response = self.client.get('/{1}/')
#     #     self.assertEqual(response.status_code, 200)

# -------------------------------------------------------------------------------------------------------#

#     # def test_delete_page_status_code(self):
#     #     response = self.client.get('/{1}/delete/')
#     #     self.assertEqual(response.status_code, 200)