from django.test import TestCase, SimpleTestCase
from django.urls import reverse, reverse_lazy
from .models import Letter_pdf
from django.contrib.auth import get_user_model
from django.utils import timezone



# Tests for help_Qna Application
class help_QnaTest(TestCase):

    ########################## Model Testing ############################

    # help_Qna object with dummy data
    def setUp(self):

        self.user = get_user_model().objects.create_user(
            username='assissh',
            password='test'
        )

        self.Letter_pdf = Letter_pdf.objects.create(
            Letter_pdf_Addressing_Officer = 'Letter_pdf_Addressing_Officer',
            Letter_pdf_Project = 'Letter_pdf_Project',
            Letter_pdf_Creator = self.user,
            Letter_pdf_Modified_Date=timezone.now(),
            Letter_pdf_Created_Date= timezone.now()




        )
# #
    #  # Check redirection URL
    def test_get_absolute_url(self):
         self.assertEquals(self.Letter_pdf.get_absolute_url(),'/Letter_pdf/1')

#     # Check Conent of help_Qna object
    def test_help_Qna_content(self):
        self.assertEqual(f'{self.Letter_pdf.Letter_pdf_Addressing_Officer}','Letter_pdf_Addressing_Officer')
        self.assertEqual(f'{self.Letter_pdf.Letter_pdf_Project}','Letter_pdf_Project')
        self.assertEqual(f'{self.Letter_pdf.Letter_pdf_Creator}',self.user.username)

#
#     # #############################   Model Test End   ###########################################
#
#     # ###############################    Views Test       ########################################
#
#     # Test help_Qna List View
    def test_help_QnaList_view(self):
         response = self.client.get(reverse('Letter_pdf_list'))
         self.client.login(username='assissh',password='test')
         print(response)
         self.assertEqual(response.status_code, 200)
         self.assertEqual(f'{self.Letter_pdf.Letter_pdf_Creator}', self.user.username)
         self.assertTemplateUsed(response, 'Letter_pdf/Letter_pdf_list.html')

     # Test help_Qna Detail View


    def test_helpcenterDetail_view(self):
        # Login the user defined in SetUp
        self.client.login(username='assissh', password='test')

        # Find primary key of table
        Letter_pdf_pk = Letter_pdf.objects.get(Letter_pdf_Addressing_Officer='Letter_pdf_Addressing_Officer').pk

        # Get response
        response = self.client.get(reverse_lazy('Letter_pdf_details', kwargs={'pk': Letter_pdf_pk}))

        # Check for any invalid value
        no_response = self.client.get(reverse_lazy('Letter_pdf_details', kwargs={'pk': 10000}))
        # 202 for valid and 404 for invalid
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)

        # Check for Correct template used in template/help_Qnas
        self.assertTemplateUsed(response, 'Letter_pdf/Letter_pdf_detail.html')
## Test Location_Amenitie Create View
    def test_Letter_pdf_Create_view(self):
            # Login the user defined in SetUp
            self.client.login(username='assissh', password='test')

            # Generate response after creating an view using Http post method
            response = self.client.post('/Letter_pdf/new/', {
                'Letter_pdf_Addressing_Officer': 'Letter_pdf_Addressing_Officer',
                'Letter_pdf_Project': 'Letter_pdf_Project',
                'Letter_pdf_Creator': self.user,  # Defined in setup
                'Help_pdf_Modified_Date': timezone.now(),
                'Help_Qna_Created_Date': timezone.now(),
            })

            # Check for successful response
            self.assertEqual(response.status_code, 200)

            # Check response values
            self.assertContains(response, 'Letter_pdf_Addressing_Officer')
            self.assertContains(response, 'Letter_pdf_Project')
            self.assertContains(response, self.user.username)  # Same as defined in SetUp
            # Check for correct template used in template/help_Qnas
            self.assertTemplateUsed(response, 'Letter_pdf/Letter_pdf_new.html')

        # Test help_Qna Update view

    def Letter_pdf_update_view(self):
                # Login the user
                self.client.login(username='assissh', password='test')

                # Find primary key of table
                Letter_pdf_pk = Letter_pdf.objects.get(Letter_pdf_Addressing_Officer='Letter_pdf_Addressing_Officer').pk

                # Get response using pk on details view
                response = self.client.get(reverse_lazy('Letter_pdf_details', kwargs={'pk': Letter_pdf_pk}), {
                    'Letter_pdf_Addressing_Officer': 'Letter_pdf_Addressing_Officer',
                    'Letter_pdf_Project': 'Letter_pdf_Project',
                    'Letter_pdf_Creator': self.user.username,
                    'Help_pdf_Modified_Date': timezone.now(),
                    'Help_Qna_Created_Date': timezone.now(),
                })
                # Check for successful response
                self.assertEqual(response.status_code, 200)

                # Check for correct templates
                self.assertTemplateUsed(response, 'Letter_pdf/Letter_pdf_update.html')


    def test_help_Qnadelete_view(self):
        # Login the user
        self.client.login(username='assissh', password='test')

        # Find primary key of table
        help_Qna_pk = Letter_pdf.objects.get(Letter_pdf_Addressing_Officer='Letter_pdf_Addressing_Officer').pk

        # Get response to delete

        response = self.client.get(reverse_lazy('Letter_pdf_delete', kwargs={'pk': help_Qna_pk}))
        self.assertContains(response, 'Are you sure you want to delete')  # THIS PART WORKS

        # Check deleted value , returns false i.e.302
        post_response = self.client.post(reverse_lazy('Letter_pdf_delete', kwargs={'pk': help_Qna_pk}))

        self.assertEqual(response.status_code, 200)
        # check for Correct Template Used
        self.assertTemplateUsed(response, 'Letter_pdf/Letter_pdf_delete.html')

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
# #URLfor update
# def test_new_page_status_code(self):
#         # Login the user defined in SetUp
#         self.client.login(username='assissh', password='test')
#
#         # Get response
#         response = self.client.get('/Letter_pdf/1/')
#
#         self.assertEqual(response.status_code, 200)
#
# # def test_update_page_status_code(self):
# #         url = reverse('Letter_pdfListView')
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
