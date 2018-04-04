from django.test import TestCase, SimpleTestCase
from django.urls import reverse, reverse_lazy
from .models import HelpSubCategory
from django.contrib.auth import get_user_model
from django.utils import timezone



# Tests for help_subcategory Application
class help_subcategoryTest(TestCase):

    ######################### Model Testing ############################

    # help_subcategory object with dummy data
    def setUp(self):

        self.user = get_user_model().objects.create_user(
            username='assissh',
            password='test'
        )

        self.help_subcategory = HelpSubCategory.objects.create(
            Help_SubCategory_Name = 'Help_SubCategory_Name',
            Help_SubCategory_Topic_Id = 'Help_SubCategory_Topic_Id',
            Help_SubCategory_Creator = self.user,
            Help_SubCategory_Modified_Date=timezone.now(),
            Help_SubCategory_Created_Date= timezone.now()




        )
    #  # Check redirection URL
    def test_get_absolute_url(self):
         self.assertEquals(self.help_subcategory.get_absolute_url(),'/help_subcategory/1')

#     # Check Conent of help_subcategory object
    def test_help_subcategory_content(self):
        self.assertEqual(f'{self.help_subcategory.Help_SubCategory_Name}','Help_SubCategory_Name')
        self.assertEqual(f'{self.help_subcategory.Help_SubCategory_Topic_Id}','Help_SubCategory_Topic_Id')
        self.assertEqual(f'{self.help_subcategory.Help_SubCategory_Creator}',self.user.username)

#
#     # #############################   Model Test End   ###########################################
#
#     # ###############################    Views Test       ########################################
#
#     # Test help_subcategory List View
    def test_help_subcategoryList_view(self):
         response = self.client.get(reverse('helpsubcategory_list'))
         self.client.login(username='assissh',password='test')
         print(response)
         self.assertEqual(response.status_code, 200)
         self.assertEqual(f'{self.help_subcategory.Help_SubCategory_Creator}', self.user.username)
         self.assertTemplateUsed(response, 'helpsubcategory/helpsubcategory_list.html')

     # Test help_subcategory Detail View

    #
    def test_helpcenterDetail_view(self):
        # Login the user defined in SetUp
        self.client.login(username='assissh', password='test')

        # Find primary key of table
        help_subcategory_pk = HelpSubCategory.objects.get(Help_SubCategory_Name='Help_SubCategory_Name').pk

        # Get response
        response = self.client.get(reverse_lazy('helpsubcategory_details', kwargs={'pk': help_subcategory_pk}))

        # Check for any invalid value
        no_response = self.client.get(reverse_lazy('helpsubcategory_details', kwargs={'pk': 10000}))

        # 202 for valid and 404 for invalid
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)

        # Check for Correct template used in template/help_subcategorys
        self.assertTemplateUsed(response, 'helpsubcategory/helpsubcategory_detail.html')

    def test_help_subcategory_Create_view(self):
            # Login the user defined in SetUp
            self.client.login(username='assissh', password='test')

            # Generate response after creating an view using Http post method
            response = self.client.post('/help_subcategory/new/', {
                'Help_SubCategory_Name': 'Help_SubCategory_Name',
                'Help_SubCategory_Topic_Id': 'Help_SubCategory_Topic_Id',
                'Help_SubCategory_Creater': self.user,  # Defined in setup
                'Help_SubCategory_Modified_Date': timezone.now(),
                'Help_SubCategory_Created_Date': timezone.now(),
            })

            # Check for successful response
            self.assertEqual(response.status_code, 200)

            # Check response values
            self.assertContains(response, 'Help_SubCategory_Name')
            self.assertContains(response, 'Help_SubCategory_Topic_Id')
            self.assertContains(response, self.user.username)  # Same as defined in SetUp
            # Check for correct template used in template/help_subcategorys
            self.assertTemplateUsed(response, 'helpsubcategory/helpsubcategory_new.html')

            # Test help_subcategory Update view

    def help_subcategory_update_view(self):
                # Login the user
                self.client.login(username='assissh', password='test')

                # Find primary key of table
                help_subcategory_pk = HelpSubCategory.objects.get(Help_SubCategory_Name='Help_SubCategory_Name').pk
                print(self.user.username)##user is not defined

                # Get response using pk on details view
                response = self.client.get(reverse_lazy('helpsubcategory_details', kwargs={'pk': help_subcategory_pk}), {
                    'Help_SubCategory_Name': 'Help_SubCategory_Name',
                    'Help_SubCategory_Topic_Id': 'Help_SubCategory_Topic_Id',
                    'help_subcategory_Creator': self.user.username,
                    'Help_Subcategory_Modified_Date': timezone.now(),
                    'Help_Subcategory_Created_Date': timezone.now(),
                })
                # Check for successful response
                self.assertEqual(response.status_code, 200)

                # Check for correct templates
                self.assertTemplateUsed(response, 'helpsubcategory/helpsubcategory_update.html')


    def test_help_subcategorydelete_view(self):
        # Login the user
        self.client.login(username='assissh', password='test')

        # Find primary key of table
        help_subcategory_pk = HelpSubCategory.objects.get(Help_SubCategory_Name='Help_SubCategory_Name').pk

        # Get response to delete

        response = self.client.get(reverse_lazy('helpsubcategory_delete', kwargs={'pk': help_subcategory_pk}))
        self.assertContains(response, 'Are you sure you want to delete')  # THIS PART WORKS

        # Check deleted value , returns false i.e.302
        post_response = self.client.post(reverse_lazy('helpsubcategory_delete', kwargs={'pk': help_subcategory_pk}))



        self.assertEqual(response.status_code, 200)

        # check for Correct Template Used
        self.assertTemplateUsed(response, 'helpsubcategory/helpsubcategory_delete.html')

# # # # ################################     View Testing End   ##############################################
# # #
# # # # ################################     Testing URLs       ##############################################
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
# # def test_new_page_status_code(self):
# #         # Login the user defined in SetUp
# #         self.client.login(username='assissh', password='test')
# #
# #         # Get response
# #         response = self.client.get('/help_subcategory/1/')
# #
# #         self.assertEqual(response.status_code, 200)
# #
# # # def test_update_page_status_code(self):
# # #         url = reverse('help_subcategoryListView')
# # #         response = self.client.get('/Lettzkxudh/1/')
# # #         self.assertEqual(response.status_code, 200)
# # # #
# # # def test_detail_page_status_code(self):
# # #         response = self.client.get('/{1}/')
# # #         self.assertEqual(response.status_code, 200)
# # #
# # # def test_delete_page_status_code(self):
# # #                 response = self.client.get('/{1}/delete/')
# # #                 self.assertEqual(response.status_code, 200)
