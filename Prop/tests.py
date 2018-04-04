from django.test import TestCase, SimpleTestCase
from django.urls import reverse, reverse_lazy
from .models import Prop
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.forms.models import model_to_dict


#  Test Class for Prop Application

class PropTest(TestCase):

    ########################## Model Testing ############################

    # Prop object with dummy data
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='test'
        )

        self.Prop = Prop.objects.create(

            # Fields according to defined in Model
            Prop_Color='Prop_Color',
            Prop_Daily_Rent=1,

            Prop_Making_Year=timezone.now(),
            Prop_Modification_Allowed=True,
            Prop_Ownership_Status=True,
            Prop_ID = 1,
            Prop_Make = 'Prop_Make',
            Prop_Type = 'Prop_Type',
            Prop_Weekly_Rent = 1,
            Prop_Creator=self.user,
            Prop_Modified_Date=timezone.now(),
            Prop_Created_Date = timezone.now(),
        )

    # -----------------------------------------------------------------------------------------#

    # Check redirection URL
    def test_get_absolute_url(self):
        # Redirection goes to Prop details
        self.assertEquals(self.Prop.get_absolute_url(), '/prop/1')

    # -----------------------------------------------------------------------------------------#

    # Check Conent of Prop object created by create object query set
    def test_Prop_content(self):
        # Verify for each field
        self.assertEqual(f'{self.Prop.Prop_Color}', 'Prop_Color')
        self.assertEqual(f'{self.Prop.Prop_Daily_Rent}', '1')
        self.assertEqual(f'{self.Prop.Prop_Modification_Allowed}','True')
        self.assertEqual(f'{self.Prop.Prop_Ownership_Status}', 'True')
        self.assertEqual(f'{self.Prop.Prop_ID}', '1')
        self.assertEqual(f'{self.Prop.Prop_Make}', 'Prop_Make')
        self.assertEqual(f'{self.Prop.Prop_Type}', 'Prop_Type')
        self.assertEqual(f'{self.Prop.Prop_Weekly_Rent}', '1')

        self.assertEqual(f'{self.Prop.Prop_Creator}', self.user.username)

    # --------------------------------------------------------------------------------------------#

    # #############################   Model Test End   ###########################################

    # ###############################    Views Test       ########################################

    # Test Prop List View

    def test_PropList_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test')

        # Get respomse from defined URL namespace
        response = self.client.get(reverse('Prop_list'))
        self.assertEqual(response.status_code, 200)

        # Check Content of List View
        self.assertContains(response, self.user.username)

        # Check for Correct template used in template/Props
        self.assertTemplateUsed(response, 'Prop/Prop_list.html')

    # --------------------------------------------------------------------------------------------#

    # Test Prop Detail View

    def test_PropDetail_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test')

        # Find primary key of table
        Prop_pk = Prop.objects.get(Prop_Color='Prop_Color').pk

        # Get response
        response = self.client.get(reverse_lazy('Prop_details', kwargs={'pk': Prop_pk}))

        # Check for any invalid value
        no_response = self.client.get(reverse_lazy('Prop_details', kwargs={'pk': 10000}))

        # 202 for valid and 404 for invalid
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)

        # check for content of Detail Page

        # Check for Correct template used in template/Props
        self.assertTemplateUsed(response, 'Prop/Prop_detail.html')

    # -------------------------------------------------------------------------------------------#

    #Test Prop Create View

    def test_PropCreate_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test')

        # Generate response after creating an view using Http post method
        response = self.client.post('/prop/new/', {
            'Prop_Color': 'Prop_Color',
            'Prop_Daily_Rent': 1,
            'Prop_Modification_Allowed':True,
            'Prop_Ownership_Status':'Prop_Ownership_Status',
            'Prop_ID':1,
            'Prop_Make':'Prop_Make',
            'Prop_Type':'Prop_Type',
            'Prop_Weekly_Rent':'Prop_Weekly_Rent',
            'Prop_Creator': self.user,  # Defined in setup
            'Prop_Modified_Date': timezone.now(),
            'Prop_Created_Date': timezone.now(),
        })

        # Check for successful response
        self.assertEqual(response.status_code, 200)

        # Check response values
        self.assertContains(response, 'Prop_Color')
        self.assertContains(response, 1)
        self.assertContains(response, 'checked')
        self.assertContains(response, 'Prop_Ownership_Status')
        self.assertContains(response, 1)
        self.assertContains(response, 'Prop_Make')
        self.assertContains(response, 'Prop_Type')
        self.assertContains(response, 'Prop_Weekly_Rent')
        self.assertContains(response, self.user.username)  # Same as defined in SetUp

        # Check for correct template used in template/Props
        self.assertTemplateUsed(response, 'Prop/Prop_new.html')

    # ---------------------------------------------------------------------------------------#

    # Test Prop Update view

    def test_Propupdate_view(self):
        # Login the user
        self.client.login(username='testuser', password='test')

        # Find primary key of table
        Prop_pk = Prop.objects.get(Prop_Color='Prop_Color').pk

        # Get response using pk on details view
        response = self.client.get(reverse_lazy('Prop_details', kwargs={'pk': Prop_pk}), {
            'Prop_Color': 'Prop_Color',
            'Prop_Daily_Rent': 1,
            'Prop_Modification_Allowed':True,
            'Prop_Ownership_Status':'Prop_Ownership_Status',
            'Prop_ID':1,
            'Prop_Make':'Prop_Make',
            'Prop_Type':'Prop_Type',
            'Prop_Weekly_Rent':'Prop_Weekly_Rent',
            'Prop_Creator': self.user.username,
            'Prop_Modified_Date': timezone.now(),
            'Prop_Created_Date': timezone.now(),
        })
        # Check for successful response
        self.assertEqual(response.status_code, 200)

        # Check for correct templates
        self.assertTemplateUsed(response, 'Prop/Prop_detail.html')

    # --------------------------------------------------------------------------------------------#

    # Test Delete View of Prop views

    def test_Propdelete_view(self):
        # Login the user
        self.client.login(username='testuser', password='test')

        # Find primary key of table
        Prop_pk = Prop.objects.get(Prop_Color='Prop_Color').pk

        # Get response to delete

        response = self.client.get(reverse_lazy('Prop_delete', kwargs={'pk': Prop_pk}))
        self.assertContains(response, 'Are you sure you want to delete')  # THIS PART WORKS

        # Check deleted value , returns false i.e.302
        post_response = self.client.post(reverse_lazy('Prop_delete', kwargs={'pk': Prop_pk}))

        # self.assertRedirects(post_response, reverse_lazy('Prop_delete',kwargs={'pk':Prop_pk}), status_code=302)

        self.assertEqual(response.status_code, 200)

        # check for Correct Template Used
        self.assertTemplateUsed(response, 'Prop/Prop_delete.html')


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
# #         response = self.client.get('/Props/1/')
# 
# #         self.assertEqual(response.status_code, 200)
# 
# 
# # ------------------------------------------------------------------------------------------------------#
# 
# 
# #     # def test_update_page_status_code(self):
# #     #     # url = reverse('PropListView')
# #     #     response = self.client.get('/Props/1/')
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