from django.test import TestCase, SimpleTestCase
from django.urls import reverse, reverse_lazy
from .models import HelpQna
from django.contrib.auth import get_user_model
from django.utils import timezone



# Tests for help_Qna Application
class help_QnaTest(TestCase):

    ########################## Model Testing ############################

    # help_Qna object with dummy data
    def setUp(self):

        self.user = get_user_model().objects.create_user(
            username='ashish',
            email='test@email.com',
            password='test'
        )

        self.help_Qna = HelpQna.objects.create(
            Help_Qna_Answer = 'Help_Qna_Answer',
            Help_Qna_Article_Id = 1,
            Help_Qna_Question = 'Help_Qna_Question',
            Help_Qna_Creator = self.user,
            Help_Qna_Modified_Date=timezone.now(),
            Help_Qna_Created_Date= timezone.now()




        )
#
    #  # Check redirection URL
    def test_get_absolute_url(self):
         self.assertEquals(self.help_Qna.get_absolute_url(),'/help_Qna/1')

    # Check Conent of help_Qna object
    def test_help_Qna_content(self):
        self.assertEqual(f'{self.help_Qna.Help_Qna_Answer}','Help_Qna_Answer')
        self.assertEqual(f'{self.help_Qna.Help_Qna_Article_Id}', '1')
        self.assertEqual(f'{self.help_Qna.Help_Qna_Question}','Help_Qna_Question')
        self.assertEqual(f'{self.help_Qna.Help_Qna_Creator}',self.user.username)


    # #############################   Model Test End   ###########################################

    # ###############################    Views Test       ########################################

    # Test help_Qna List View
    def test_help_QnaList_view(self):
         response = self.client.get(reverse('helpQna_list'))
         self.client.login(username='ashish',email='test@email.com')
         print(response)
         self.assertEqual(response.status_code, 200)

         self.assertTemplateUsed(response, 'helpQna/helpQna_list.html')

     # Test help_Qna Detail View

#
    def test_helpcenterDetail_view(self):
        # Login the user defined in SetUp
        self.client.login(username='ashish', password='test')

        # Find primary key of table
        help_Qna_pk = HelpQna.objects.get(Help_Qna_Answer='Help_Qna_Answer').pk

        # Get response
        response = self.client.get(reverse_lazy('helpQna_details', kwargs={'pk': help_Qna_pk}))

        # Check for any invalid value
        no_response = self.client.get(reverse_lazy('helpQna_details', kwargs={'pk': 10000}))

        # 202 for valid and 404 for invalid
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)


        # Check for Correct template used in template/help_Qnas
        self.assertTemplateUsed(response, 'helpQna/helpQna_detail.html')

    def test_help_QnaCreate_view(self):
            # Login the user defined in SetUp
            self.client.login(username='ashish', password='test')

            # Generate response after creating an view using Http post method
            response = self.client.post('/help_Qna/new/', {
                'Help_Qna_Answer': 'Help_Qna_Answer',
                'Help_Qna_Article_id': 1,
                'Help_Qna_Question': 'Help_Qna_Question',
                'Help_Qna_Creater': self.user,  # Defined in setup
                'Help_Qna_Modified_Date': timezone.now(),
                'Help_Qna_Created_Date': timezone.now(),
            })


            # Check for successful response
            self.assertEqual(response.status_code, 200)

            # Check response values
            self.assertContains(response, 'Help_Qna_Answer')
            self.assertContains(response, '1')
            self.assertContains(response, 'Help_Qna_Question')
            self.assertContains(response, self.user.username)  # Same as defined in SetUp

            # Check for correct template used in template/help_Qnas
            self.assertTemplateUsed(response, 'helpQna/helpQna_new.html')

        # Test help_Qna Update view

    def test_help_Qnaupdate_view(self):
                # Login the user
                self.client.login(username='ashish', password='test')

                # Find primary key of table
                help_Qna_pk = HelpQna.objects.get(Help_Qna_Answer='Help_Qna_Answer').pk

                # Get response using pk on details view
                response = self.client.get(reverse_lazy('helpQna_details', kwargs={'pk': help_Qna_pk}), {
                    'Help_Qna_Answer': 'Help_Qna_Answer',
                    'Help_Qna_Article_id': 'Help_Qna_Article_id',
                    'Help_Qna_Question': 'Help_Qna_Question',
                    'Help_Qna_Creater': self.user.username,
                    'Help_Qna_Modified_Date': timezone.now(),
                    'Help_Qna_Created_Date': timezone.now(),
                })
                # Check for successful response
                self.assertEqual(response.status_code, 200)

                # Check for correct templates
                self.assertTemplateUsed(response, 'helpQna/helpQna_detail.html')


    def test_help_Qnadelete_view(self):
        # Login the user
        self.client.login(username='ashish', password='test')

        # Find primary key of table
        help_Qna_pk = HelpQna.objects.get(Help_Qna_Answer='Help_Qna_Answer').pk

        # Get response to delete

        response = self.client.get(reverse_lazy('helpQna_delete', kwargs={'pk': help_Qna_pk}))
        self.assertContains(response, 'Are you sure you want to delete')  # THIS PART WORKS

        # Check deleted value , returns false i.e.302
        post_response = self.client.post(reverse_lazy('helpQna_delete', kwargs={'pk': help_Qna_pk}))

        #self.assertRedirects(post_response, reverse_lazy('helpQna_delete',kwargs={'pk':help_Qna_pk}), status_code=302)

        self.assertEqual(response.status_code, 200)

        # check for Correct Template Used
        self.assertTemplateUsed(response, 'helpQna/helpQna_delete.html')

# # ################################     View Testing End   ##############################################
#
# # ################################     Testing URLs       ##############################################




class PagesTests(SimpleTestCase):

    # Check URL for list
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

# #URLfor update
# def test_new_page_status_code(self):
#         # Login the user defined in SetUp
#         self.client.login(username='testuser', password='test')
#
#         # Get response
#         response = self.client.get('/help_Qna/1/')
#
#         self.assertEqual(response.status_code, 200)
#
# def test_update_page_status_code(self):
#         url = reverse('help_QnaListView')
#         response = self.client.get('/help_Qna/1/')
#         self.assertEqual(response.status_code, 200)
#
# def test_detail_page_status_code(self):
#         response = self.client.get('/{1}/')
#         self.assertEqual(response.status_code, 200)
#
# def test_delete_page_status_code(self):
#                 response = self.client.get('/{1}/delete/')
#                 self.assertEqual(response.status_code, 200)
