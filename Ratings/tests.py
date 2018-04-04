from django.test import TestCase, SimpleTestCase
from django.urls import reverse, reverse_lazy
from .models import Rating
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.forms.models import model_to_dict


#  Test Class for Ratings Application

class RatingsTest(TestCase):

    ########################## Model Testing ############################

    # Ratings object with dummy data
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='test'
        )

        self.Ratings = Rating.objects.create(

            # Fields according to defined in Model
            Rating=1,
            Rating_User_ID=self.user,
            Rating_Creator=self.user,
            Rating_Modified_Date=timezone.now(),
            Rating_Create_Date = timezone.now(),
        )

    # -----------------------------------------------------------------------------------------#

    # Check redirection URL
    def test_get_absolute_url(self):
        # Redirection goes to Ratings details
        self.assertEquals(self.Ratings.get_absolute_url(), '/rating/1')

    # -----------------------------------------------------------------------------------------#

    # Check Conent of Ratings object created by create object query set
    def test_Ratings_content(self):
        # Verify for each field
        self.assertEqual(f'{self.Ratings.Rating}', '1')
        self.assertEqual(f'{self.Ratings.Rating_User_ID}', self.user.username)
        self.assertEqual(f'{self.Ratings.Rating_Creator}', self.user.username)

    # --------------------------------------------------------------------------------------------#

    # #############################   Model Test End   ###########################################

    # ###############################    Views Test       ########################################

    # Test Ratings List View

    def test_RatingsList_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test')

        # Get respomse from defined URL namespace
        response = self.client.get(reverse('Rating_list'))
        self.assertEqual(response.status_code, 200)

        # Check Content of List View
        self.assertContains(response, self.user.username)

        # Check for Correct template used in template/Ratingss
        self.assertTemplateUsed(response, 'Rating/Rating_list.html')

    # --------------------------------------------------------------------------------------------#

    # Test Ratings Detail View

    def test_RatingsDetail_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test')

        # Find primary key of table
        Rating_pk = Rating.objects.get(Rating='1').pk

        # Get response
        response = self.client.get(reverse_lazy('Rating_details', kwargs={'pk': Rating_pk}))

        # Check for any invalid value
        no_response = self.client.get(reverse_lazy('Rating_details', kwargs={'pk': 10000}))

        # 202 for valid and 404 for invalid
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        # check for content of Detail Page

        # Check for Correct template used in template/Ratingss
        self.assertTemplateUsed(response, 'Rating/Rating_detail.html')

    # -------------------------------------------------------------------------------------------#

    #Test Ratings Create View

    def test_RatingsCreate_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test')

        # Generate response after creating an view using Http post method
        response = self.client.post('/rating/new/', {
            'Rating': 1,
            'Rating_User_ID': 1,
            'Rating_Creator': self.user,  # Defined in setup
            'Rating_Modified_Date': timezone.now(),
            'Rating_Created_Date': timezone.now(),
        })

        # Check for successful response
        self.assertEqual(response.status_code, 200)

        # Check response values
        self.assertContains(response, 1)
        self.assertContains(response, 1)
        self.assertContains(response, self.user.username)  # Same as defined in SetUp

        # Check for correct template used in template/Ratingss
        self.assertTemplateUsed(response, 'Rating/Rating_new.html')

    # ---------------------------------------------------------------------------------------#

    # Test Ratings Update view

    def test_Ratingsupdate_view(self):
        # Login the user
        self.client.login(username='testuser', password='test')

        # Find primary key of table
        Rating_pk = Rating.objects.get(Rating='1').pk

        # Get response using pk on details view
        response = self.client.get(reverse_lazy('Rating_details', kwargs={'pk': Rating_pk}), {
            'Rating': 1,
            'Rating_User_ID': 1,
            'Rating_Creator': self.user.username,
            'Rating_Modified_Date': timezone.now(),
            'Rating_Created_Date': timezone.now(),
        })
        # Check for successful response
        self.assertEqual(response.status_code, 200)

        # Check for correct templates
        self.assertTemplateUsed(response, 'Rating/Rating_detail.html')

    # --------------------------------------------------------------------------------------------#

    # Test Delete View of Ratings views

    def test_Ratingsdelete_view(self):
        # Login the user
        self.client.login(username='testuser', password='test')

        # Find primary key of table
        Rating_pk = Rating.objects.get(Rating='1').pk

        # Get response to delete

        response = self.client.get(reverse_lazy('Rating_delete', kwargs={'pk': Rating_pk}))
        self.assertContains(response, 'Are you sure you want to delete')  # THIS PART WORKS

        # Check deleted value , returns false i.e.302
        post_response = self.client.post(reverse_lazy('Rating_delete', kwargs={'pk': Rating_pk}))

        # self.assertRedirects(post_response, reverse_lazy('Ratings_delete',kwargs={'pk':Ratings_pk}), status_code=302)

        self.assertEqual(response.status_code, 200)

        # check for Correct Template Used
        self.assertTemplateUsed(response, 'Rating/Rating_delete.html')


################################     View Testing End   #################################################


# ################################     Testing the URLs       ##############################################

class PagesTests(SimpleTestCase):

    # Check URL for list/ Home
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

# #-----------------------------------------------------------------------------------------------------#
# 
# #     # URL for new
# #     def test_new_page_status_code(self):
# #         # Login the user defined in SetUp
# #         # self.client.login(username='testuser', password='test')
# 
# #         # Get response
# #         response = self.client.get('/Ratingss/1/')
# 
# #         self.assertEqual(response.status_code, 200)
# 
# 
# # ------------------------------------------------------------------------------------------------------#
# 
# 
# #     # def test_update_page_status_code(self):
# #     #     # url = reverse('RatingsListView')
# #     #     response = self.client.get('/Ratingss/1/')
# #     #     self.assertEqual(response.status_code, 200)
# 
# # -------------------------------------------------------------------------------------------------------#
# 
# #     # def test_detail_page_status_code(self):
# #     #     response = self.client.get('/{1}/')
# #     #     self.assertEqual(response.status_code, 200)
# 
# # -------------------------------------------------------------------------------------------------------#
# 
# #     # def test_delete_page_status_code(self):
# #     #     response = self.client.get('/{1}/delete/')
#     #     self.assertEqual(response.status_code, 200)