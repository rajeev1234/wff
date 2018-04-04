from django.test import TestCase, SimpleTestCase
from django.urls import reverse, reverse_lazy
from .models import HelpCenter
from django.contrib.auth import get_user_model
from django.utils import timezone



# Tests for help_center Application
class Help_CenterTest(TestCase):
     def setUp(self):
         self.user = get_user_model().objects.create_user(
            username='assissh',
            password='test'
         )
         self.help_center = HelpCenter.objects.create(
             Help_Center_Help_Name = 'Help_Center_Help_Name',
             Help_Center_Help_Id = 1,
             Help_Center_Creator = self.user,
             Help_Center_Modified_Date=timezone.now(),
             Help_Center_Created_Date= timezone.now()
        )
#
    #  # Check redirection URL
     def test_get_absolute_url(self):
         self.assertEquals(self.help_center.get_absolute_url(),'/help_center/1')

#     # Check Conent of help_center object
     def test_help_center_content(self):
        self.assertEqual(f'{self.help_center.Help_Center_Help_Name}','Help_Center_Help_Name')
        self.assertEqual(f'{self.help_center.Help_Center_Help_Id}','1')
        self.assertEqual(f'{self.help_center.Help_Center_Creator}',self.user.username)

#
# #     # #############################   Model Test End   ###########################################
# #
# #     # ###############################    Views Test       ########################################
# #
#     # Test help_center List View
     def test_help_centerList_view(self):
         response = self.client.get(reverse('helpcenter_list'))
         self.client.login(username='assissh',password='test')
         print(response)
         self.assertEqual(response.status_code, 200)
         self.assertEqual(f'{self.help_center.Help_Center_Creator}', self.user.username)
         self.assertTemplateUsed(response, 'helpcenter/helpcenter_list.html')

#      # Test help_center Detail View
#
#
     def test_helpcenterDetail_view(self):
        # Login the user defined in SetUp
         self.client.login(username='assissh', password='test')

        # Find primary key of table
         help_center_pk = HelpCenter.objects.get(Help_Center_Help_Name='Help_Center_Help_Name').pk

        # Get response
         response = self.client.get(reverse_lazy('helpcenter_details', kwargs={'pk': help_center_pk}))

        # Check for any invalid value
         no_response = self.client.get(reverse_lazy('helpcenter_details', kwargs={'pk': 10000}))

        # 202 for valid and 404 for invalid
         self.assertEqual(response.status_code, 200)
         self.assertEqual(no_response.status_code, 404)

        # check for content of Detail Page

        # Check for Correct template used in template/help_centers
         self.assertTemplateUsed(response, 'helpcenter/helpcenter_detail.html')

     def test_help_center_Create_view(self):
        # Login the user defined in SetUp
         self.client.login(username='assissh', password='test')

        # Generate response after creating an view using Http post method
         response = self.client.post('/help_center/new/', {
            'Help_Center_Help_Name': 'Help_Center_Help_Name',
            'Help_Center_Help_Id': 'Help_Center_Help_Id',
            'Help_Center_Creator': self.user,  # Defined in setup
            'Help_Center_Modified_Date': timezone.now(),
            'Help_Center_Created_Date': timezone.now(),
        })

        # Check for successful response
         self.assertEqual(response.status_code, 200)

        # Check response values
         self.assertContains(response, 'Help_Center_Help_Name')
         self.assertContains(response, 'Help_Center_Help_Id')
         self.assertContains(response, self.user.username)  # Same as defined in SetUp

        # Check for correct template used in template/help_centers
         self.assertTemplateUsed(response, 'helpcenter/helpcenter_new.html')

        # Test help_center Update view

     def help_center_update_view(self):
         print(self.user.username)
         # Login the user
         self.client.login(username='assissh', password='test')

         # Find primary key of table
         help_center_pk = HelpCenter.objects.get(Help_Center_Help_Name='Help_Center_Help_Name').pk

         # Get response using pk on details view
         response = self.client.get(reverse_lazy('helpcenter_details', kwargs={'pk': help_center_pk}), {
             'Help_Center_Help_Name': 'Help_Center_Help_Name',
             'Help_Center_Help_Id': 'Help_Center_Help_Id',
             'Help_Center_Creator': self.user.username,
             'Help_Center_Modified_Date': timezone.now(),
             'Help_Center_Created_Date': timezone.now(),
         })
         # Check for successful response
         self.assertEqual(response.status_code, 200)

         # Check for correct templates
         self.assertTemplateUsed(response, 'helpcenter/helpcenter_update.html')

#
     def test_help_centerdelete_view(self):
    # Login the user
         self.client.login(username='assissh', password='test')

     # Find primary key of table
         help_center_pk = HelpCenter.objects.get(Help_Center_Help_Name='Help_Center_Help_Name').pk

    # Get response to delete

         response = self.client.get(reverse_lazy('helpcenter_delete', kwargs={'pk': help_center_pk}))
         self.assertContains(response, 'Are you sure you want to delete')  # THIS PART WORKS

    # Check deleted value , returns false i.e.302
         post_response = self.client.post(reverse_lazy('helpcenter_delete', kwargs={'pk': help_center_pk}))

         # self.assertRedirects(post_response, reverse_lazy('helpcenter_delete',kwargs={'pk':help_center_pk}), status_code=302)

         self.assertEqual(response.status_code, 200)

    # check for Correct Template Used
         self.assertTemplateUsed(response, 'helpcenter/helpcenter_delete.html')

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
# #         response = self.client.get('/help_center/1/')
# #
# #         self.assertEqual(response.status_code, 200)
# #
# # # def test_update_page_status_code(self):
# #         url = reverse('help_centerListView')
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
