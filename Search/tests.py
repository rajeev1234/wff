from django.test import TestCase, SimpleTestCase
from django.urls import reverse, reverse_lazy
from .models import Search
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.forms.models import model_to_dict


#  Test Class for Search Application

class SearchTest(TestCase):

    ########################## Model Testing ############################

    # Search object with dummy data
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='test'
        )

        self.Search = Search.objects.create(

            # Fields according to defined in Model
            Search_City='Search_City',
            Search_Key_Word='Search_Key_Word',
            Search_Range= 1,
            Search_Creator=self.user,
            Search_Modified_Date=timezone.now(),
            Search_Created_Date = timezone.now(),
        )

    # -----------------------------------------------------------------------------------------#

    # Check redirection URL
    def test_get_absolute_url(self):
        # Redirection goes to Search details
        self.assertEquals(self.Search.get_absolute_url(), '/search/1')

    # -----------------------------------------------------------------------------------------#

    # Check Conent of Search object created by create object query set
    def test_Search_content(self):
        # Verify for each field
        self.assertEqual(f'{self.Search.Search_City}', 'Search_City')
        self.assertEqual(f'{self.Search.Search_Key_Word}', 'Search_Key_Word')
        self.assertEqual(f'{self.Search.Search_Range}','1')
        self.assertEqual(f'{self.Search.Search_Creator}', self.user.username)

    # --------------------------------------------------------------------------------------------#

    # #############################   Model Test End   ###########################################

    # ###############################    Views Test       ########################################

    # Test Search List View

    def test_SearchList_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test')

        # Get respomse from defined URL namespace
        response = self.client.get(reverse('search_list'))
        self.assertEqual(response.status_code, 200)

        # Check Content of List View
        self.assertContains(response, self.user.username)

        # Check for Correct template used in template/Searchs
        self.assertTemplateUsed(response, 'search/search_list.html')

    # --------------------------------------------------------------------------------------------#

    # Test Search Detail View

    def test_SearchDetail_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test')

        # Find primary key of table
        Search_pk = Search.objects.get(Search_City='Search_City').pk

        # Get response
        response = self.client.get(reverse_lazy('search_details', kwargs={'pk': Search_pk}))

        # Check for any invalid value
        no_response = self.client.get(reverse_lazy('search_details', kwargs={'pk': 10000}))

        # 202 for valid and 404 for invalid
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)

        # check for content of Detail Page

        # Check for Correct template used in template/Searchs
        self.assertTemplateUsed(response, 'search/search_detail.html')

    # -------------------------------------------------------------------------------------------#

    #Test Search Create View

    def test_SearchCreate_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test')

        # Generate response after creating an view using Http post method
        response = self.client.post('/search/new/', {
            'Search_City': 'Search_City',
            'Search_Key_Word': 'Search_Key_Word',
            'Search_Range':1,
            'Search_Creator': self.user,  # Defined in setup
            'Search_Modified_Date': timezone.now(),
            'Search_Created_Date': timezone.now(),
        })

        # Check for successful response
        self.assertEqual(response.status_code, 200)

        # Check response values
        self.assertContains(response, 'Search_City')
        self.assertContains(response, 'Search_Key_Word')
        self.assertContains(response, 1)
        self.assertContains(response, self.user.username)  # Same as defined in SetUp

        # Check for correct template used in template/Searchs
        self.assertTemplateUsed(response, 'search/search_new.html')

    # ---------------------------------------------------------------------------------------#

    # Test Search Update view

    def test_Searchupdate_view(self):
        # Login the user
        self.client.login(username='testuser', password='test')

        # Find primary key of table
        Search_pk = Search.objects.get(Search_City='Search_City').pk

        # Get response using pk on details view
        response = self.client.get(reverse_lazy('search_details', kwargs={'pk': Search_pk}), {
            'Search_City': 'Search_City',
            'Search_Key_Word': 'Search_Key_Word',
            'Search_Range':1,
            'Search_Creator': self.user.username,
            'Search_Modified_Date': timezone.now(),
            'Search_Created_Date': timezone.now(),
        })
        # Check for successful response
        self.assertEqual(response.status_code, 200)

        # Check for correct templates
        self.assertTemplateUsed(response, 'search/search_detail.html')

    # --------------------------------------------------------------------------------------------#

    # Test Delete View of Search views

    def test_Searchdelete_view(self):
        # Login the user
        self.client.login(username='testuser', password='test')

        # Find primary key of table
        Search_pk = Search.objects.get(Search_City='Search_City').pk

        # Get response to delete

        response = self.client.get(reverse_lazy('search_delete', kwargs={'pk': Search_pk}))
        self.assertContains(response, 'Are you sure you want to delete')  # THIS PART WORKS

        # Check deleted value , returns false i.e.302
        post_response = self.client.post(reverse_lazy('search_delete', kwargs={'pk': Search_pk}))

        # self.assertRedirects(post_response, reverse_lazy('Search_delete',kwargs={'pk':Search_pk}), status_code=302)

        self.assertEqual(response.status_code, 200)

        # check for Correct Template Used
        self.assertTemplateUsed(response, 'search/search_delete.html')


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
# #         response = self.client.get('/Searchs/1/')
# 
# #         self.assertEqual(response.status_code, 200)
# 
# 
# # ------------------------------------------------------------------------------------------------------#
# 
# 
# #     # def test_update_page_status_code(self):
# #     #     # url = reverse('SearchListView')
# #     #     response = self.client.get('/Searchs/1/')
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