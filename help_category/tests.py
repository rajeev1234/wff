from django.test import TestCase, SimpleTestCase
from django.urls import reverse, reverse_lazy
from .models import Help_Category
from django.contrib.auth import get_user_model
from django.utils import timezone



# Tests for Help_Category Application
class Help_CategoryTest(TestCase):

    ########################## Model Testing ############################

    # Help_Category object with dummy data
    def setUp(self):

        self.user = get_user_model().objects.create_user(
            username='ashish',
            email='test@email.com',
            password='test'
        )

        self.Help_Category = Help_Category.objects.create(
            Help_Category_Name= 'Help_Category_Name',
            Help_Category_Header_Id = 1,
            Help_Category_Creator = self.user,
            Help_Category_Created_Date=timezone.now(),
            Help_Category_Modified_Date= timezone.now()




        )

     # Check redirection URL
    def test_get_absolute_url(self):
         self.assertEquals(self.Help_Category.get_absolute_url(),'/help_category/1')

    # Check Conent of Help_Category object
    def test_Help_Category_content(self):
        self.assertEqual(f'{self.Help_Category.Help_Category_Name}','Help_Category_Name')
        self.assertEqual(f'{self.Help_Category.Help_Category_Header_Id}','1')
        self.assertEqual(f'{self.Help_Category.Help_Category_Creator}',self.user.username)


    # #############################   Model Test End   ###########################################

    # ###############################    Views Test       ########################################

     # Test Help_Category List View
    def test_Help_CategoryList_view(self):
         response = self.client.get(reverse('helpcategory_list'))
         self.client.login(username='ashish',email='test@email.com')
         print(response)
         self.assertEqual(response.status_code, 200)
         self.assertEqual(f'{self.Help_Category.Help_Category_Creator}', self.user.username)
         self.assertTemplateUsed(response, 'helpcategorys/helpcategory_list.html')

     # Test Help_Category Detail View


    def test_helpcenterDetail_view(self):
        # Login the user defined in SetUp
        self.client.login(username='ashish', password='test')

        # Find primary key of table
        Help_Category_pk = Help_Category.objects.get(Help_Category_Name='Help_Category_Name').pk

        # Get response
        response = self.client.get(reverse_lazy('helpcategory_details', kwargs={'pk': Help_Category_pk}))

        # Check for any invalid value
        no_response = self.client.get(reverse_lazy('helpcategory_details', kwargs={'pk': 10000}))

        # 202 for valid and 404 for invalid
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)

        # check for content of Detail Page
       # self.assertContains(response, 'helpcategory_Message')

        # Check for Correct template used in template/Costumes
        self.assertTemplateUsed(response, 'helpcategorys/helpcategory_detail.html')

    def test_Help_CategoryCreate_view(self):
            # Login the user defined in SetUp
            self.client.login(username='ashish', password='test')

            # Generate response after creating an view using Http post method
            response = self.client.post('/help_category/new/', {
                'Help_Category_Name': 'Help',
                'Help_Category_Id': 1,
                'Help_Category_Creator': self.user,  # Defined in setup
                'Help_Category_Modified_Date': timezone.now(),
                'Help_Category_Created_Date': timezone.now(),
            })

            # Check for successful response
            self.assertEqual(response.status_code, 200)

            # Check response values
            self.assertContains(response, 'Help')
            self.assertContains(response,1)
            self.assertContains(response, self.user.username)  # Same as defined in SetUp

            # Check for correct template used in template/Costumes
            self.assertTemplateUsed(response, 'helpcategorys/helpcategory_new.html')

            # Test Costume Update view

    def test_Help_Categoryupdate_view(self):
                # Login the user
                self.client.login(username='ashish', password='test')

                # Find primary key of table
                Help_Category_pk = Help_Category.objects.get(Help_Category_Name='Help_Category_Name').pk

                # Get response using pk on details view
                response = self.client.get(reverse_lazy('helpcategory_details', kwargs={'pk': Help_Category_pk}), {
                    'Help_Category_Name': 'Help_Category_Name',
                    'Help_Category_Id': 'Help_Category_Id',
                    'Help_Category_Creator': self.user.username,
                    'Help_Category_Modified_Date': timezone.now(),
                    'Help_Category_Created_Date': timezone.now(),
                })
                # Check for successful response
                self.assertEqual(response.status_code, 200)

                # Check for correct templates
                self.assertTemplateUsed(response, 'helpcategorys/helpcategory_detail.html')


    def Test_Help_Categorydelete_view(self):
        # Login the user
        self.client.login(username='ashish', password='test')

        # Find primary key of table
        Help_Category_pk = Help_Category.objects.get(category_name='category_name').pk

        # Get response to delete

        response = self.client.get(reverse_lazy('helpcategory_delete', kwargs={'pk': Help_Category_pk}))
        self.assertContains(response, 'Are you sure you want to delete')  # THIS PART WORKS

        # Check deleted value , returns false i.e.302
        post_response = self.client.post(reverse_lazy('helpcategory_delete', kwargs={'pk': Help_Category_pk}))

        self.assertRedirects(post_response, reverse_lazy('helpcategory_delete',kwargs={'pk':Help_Category_pk}), status_code=302)

        self.assertEqual(response.status_code, 200)

        # check for Correct Template Used
        self.assertTemplateUsed(response, 'helpcategorys/helpcategory_delete.html')

# ################################     View Testing End   ##############################################

# ################################     Testing URLs       ##############################################

class PagesTests(SimpleTestCase):

#Check URL for list
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

#
# #URLfor update
# def test_new_page_status_code(self):
#         # Login the user defined in SetUp
#         self.client.login(username='testuser', password='test')
#
#         # Get response
#         response = self.client.get('/helpcenter/1/')
#
#         self.assertEqual(response.status_code, 200)
#

#
# def test_update_page_status_code(self):
#                 url = reverse('helpcenterListView')
#                 response = self.client.get('/helpcenter/1/')
#                 self.assertEqual(response.status_code, 200)
#
# def test_detail_page_status_code(self):
#                         response = self.client.get('/{1}/')
#                         self.assertEqual(response.status_code, 200)