
from django.test import TestCase, SimpleTestCase
from django.urls import reverse, reverse_lazy
from .models import Review
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.forms.models import model_to_dict


#  Test Class for Review Application

class ReviewTest(TestCase):

    ########################## Model Testing ############################

    # Review object with dummy data
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='test'
        )

        self.Review = Review.objects.create(

            # Fields according to defined in Model
            Review_Rating=1,
            Review_Text='Review_Text',
            Review_Creator=self.user,
            Review_Modified_Date=timezone.now(),
            Review_Create_Date = timezone.now(),
        )

    # -----------------------------------------------------------------------------------------#

    # Check redirection URL
    def test_get_absolute_url(self):
        # Redirection goes to Review details
        self.assertEquals(self.Review.get_absolute_url(), '/review/1')

    # -----------------------------------------------------------------------------------------#

    # Check Conent of Review object created by create object query set
    def test_Review_content(self):
        # Verify for each field
        self.assertEqual(f'{self.Review.Review_Rating}', '1')
        self.assertEqual(f'{self.Review.Review_Text}', 'Review_Text')
        self.assertEqual(f'{self.Review.Review_Creator}', self.user.username)

    # --------------------------------------------------------------------------------------------#

    # #############################   Model Test End   ###########################################

    # ###############################    Views Test       ########################################

    # Test Review List View

    def test_ReviewList_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test')

        # Get respomse from defined URL namespace
        response = self.client.get(reverse('Review_list'))
        self.assertEqual(response.status_code, 200)

        # Check Content of List View
        self.assertContains(response, self.user.username)

        # Check for Correct template used in template/Reviews
        self.assertTemplateUsed(response, 'Review/Review_list.html')

    # --------------------------------------------------------------------------------------------#

    # Test Review Detail View

    def test_ReviewDetail_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test')

        # Find primary key of table
        Review_pk = Review.objects.get(Review_Rating='1').pk

        # Get response
        response = self.client.get(reverse_lazy('Review_details', kwargs={'pk': Review_pk}))

        # Check for any invalid value
        no_response = self.client.get(reverse_lazy('Review_details', kwargs={'pk': 10000}))

        # 202 for valid and 404 for invalid
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        # check for content of Detail Page

        # Check for Correct template used in template/Reviews
        self.assertTemplateUsed(response, 'Review/Review_detail.html')

    # -------------------------------------------------------------------------------------------#

    #Test Review Create View

    def test_ReviewCreate_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test')

        # Generate response after creating an view using Http post method
        response = self.client.post('/review/new/', {
            'Review_Rating': 1,
            'Review_Text': 'Review_Text',
            'Review_Creator': self.user,  # Defined in setup
            'Review_Modified_Date': timezone.now(),
            'Review_Create_Date': timezone.now(),
        })

        # Check for successful response
        self.assertEqual(response.status_code, 200)

        # Check response values
        self.assertContains(response, 1)
        self.assertContains(response, 'Review_Text')
        self.assertContains(response, self.user.username)  # Same as defined in SetUp

        # Check for correct template used in template/Reviews
        self.assertTemplateUsed(response, 'Review/Review_new.html')

    # ---------------------------------------------------------------------------------------#

    # Test Review Update view

    def test_Reviewupdate_view(self):
        # Login the user
        self.client.login(username='testuser', password='test')

        # Find primary key of table
        Review_pk = Review.objects.get(Review_Rating='1').pk

        # Get response using pk on details view
        response = self.client.get(reverse_lazy('Review_details', kwargs={'pk': Review_pk}), {
            'Review_Rating': 1,
            'Review_Text': 'Review_Text',
            'Review_Creator': self.user.username,
            'Review_Modified_Date': timezone.now(),
            'Review_Create_Date': timezone.now(),
        })
        # Check for successful response
        self.assertEqual(response.status_code, 200)

        # Check for correct templates
        self.assertTemplateUsed(response, 'Review/Review_detail.html')

    # --------------------------------------------------------------------------------------------#

    # Test Delete View of Review views

    def test_Reviewdelete_view(self):
        # Login the user
        self.client.login(username='testuser', password='test')

        # Find primary key of table
        Review_pk = Review.objects.get(Review_Rating='1').pk

        # Get response to delete

        response = self.client.get(reverse_lazy('Review_delete', kwargs={'pk': Review_pk}))
        self.assertContains(response, 'Are you sure you want to delete')  # THIS PART WORKS

        # Check deleted value , returns false i.e.302
        post_response = self.client.post(reverse_lazy('Review_delete', kwargs={'pk': Review_pk}))

        # self.assertRedirects(post_response, reverse_lazy('Review_delete',kwargs={'pk':Review_pk}), status_code=302)

        self.assertEqual(response.status_code, 200)

        # check for Correct Template Used
        self.assertTemplateUsed(response, 'Review/Review_delete.html')


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
# #         response = self.client.get('/Reviews/1/')
#
# #         self.assertEqual(response.status_code, 200)
#
#
# # ------------------------------------------------------------------------------------------------------#
#
#
# #     # def test_update_page_status_code(self):
# #     #     # url = reverse('ReviewListView')
# #     #     response = self.client.get('/Reviews/1/')
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