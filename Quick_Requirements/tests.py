from django.test import TestCase, SimpleTestCase
from django.urls import reverse, reverse_lazy
from .models import Quick_Requirements
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.forms.models import model_to_dict


#  Test Class for Quick_Requirements Application

class Quick_RequirementsTest(TestCase):

    ########################## Model Testing ############################

    # Quick_Requirements object with dummy data
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='test'
        )

        self.Quick_Requirements = Quick_Requirements.objects.create(

            # Fields according to defined in Model
            Quick_Requirements_Crew_Size=1,
            Quick_Requirements_From_User=self.user,
            Quick_Requirements_New_Requirement=True,
            Quick_Requirements_Recipient =self.user,
            Quick_Requirements_Requirement_Description='Quick_Requirements_Requirement_Description',
            Quick_Requirements_Shoot_Category= 'Quick_Requirements_Shoot_Category',
            Quick_Requirements_Shooting_Region= 'Quick_Requirements_Shooting_Region',
            Quick_Requirements_Creator=self.user,
            Quick_Requirements_Created_Date=timezone.now(),
            Quick_Requirements_Modified_Date= timezone.now(),
        )


    # -----------------------------------------------------------------------------------------#

    # Check redirection URL
    def test_get_absolute_url(self):
        # Redirection goes to Quick_Requirements details
        self.assertEquals(self.Quick_Requirements.get_absolute_url(), '/quick_requirments/1')


    # -----------------------------------------------------------------------------------------#

    # Check Conent of Quick_Requirements object created by create object query set
    def test_Quick_Requirements_content(self):
        # Verify for each field
        self.assertEqual(f'{self.Quick_Requirements.Quick_Requirements_Crew_Size}', '1')
        self.assertEqual(f'{self.Quick_Requirements.Quick_Requirements_From_User}', self.user.username)
        self.assertEqual(f'{self.Quick_Requirements.Quick_Requirements_New_Requirement}','True')
        self.assertEqual(f'{self.Quick_Requirements.Quick_Requirements_Recipient}', self.user.username)
        self.assertEqual(f'{self.Quick_Requirements.Quick_Requirements_Requirement_Description}', 'Quick_Requirements_Requirement_Description')
        self.assertEqual(f'{self.Quick_Requirements.Quick_Requirements_Shoot_Category}', 'Quick_Requirements_Shoot_Category')
        self.assertEqual(f'{self.Quick_Requirements.Quick_Requirements_Shooting_Region}', 'Quick_Requirements_Shooting_Region')


        self.assertEqual(f'{self.Quick_Requirements.Quick_Requirements_Creator}', self.user.username)


    # --------------------------------------------------------------------------------------------#

    # #############################   Model Test End   ###########################################

    # ###############################    Views Test       ########################################

    # Test Quick_Requirements List View

    def test_Quick_RequirementsList_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test')

        # Get respomse from defined URL namespace
        response = self.client.get(reverse('Quick_Requirements_list'))
        self.assertEqual(response.status_code, 200)
        # Check Content of List View
        self.assertContains(response, self.user.username)

        # Check for Correct template used in template/Quick_Requirementss
        self.assertTemplateUsed(response, 'Quick_Requirements/Quick_Requirements_list.html')

    # --------------------------------------------------------------------------------------------#

    # Test Quick_Requirements Detail View

    def test_Quick_RequirementsDetail_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test')

        # Find primary key of table
        Quick_Requirements_pk = Quick_Requirements.objects.get(Quick_Requirements_Shoot_Category='Quick_Requirements_Shoot_Category').pk

        # Get response
        response = self.client.get(reverse_lazy('Quick_Requirements_details', kwargs={'pk': Quick_Requirements_pk}))

        # Check for any invalid value
        no_response = self.client.get(reverse_lazy('Quick_Requirements_details', kwargs={'pk': 10000}))

        # 202 for valid and 404 for invalid
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)

        # check for content of Detail Page

        # Check for Correct template used in template/Quick_Requirementss
        self.assertTemplateUsed(response, 'Quick_Requirements/Quick_Requirements_detail.html')

    # -------------------------------------------------------------------------------------------#

    #Test Quick_Requirements Create View

    def test_Quick_RequirementsCreate_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test')

        # Generate response after creating an view using Http post method
        response = self.client.post('/quick_requirments/new/', {
            'Quick_Requirements_Crew_Size': 1,
            'Quick_Requirements_From_User': self.user,
            'Quick_Requirements_New_Requirement':True,
            'Quick_Requirements_Recipient':self.user,
            'Quick_Requirements_Requirement_Description':'Quick_Requirements_Requirement_Description',
            'Quick_Requirements_Shoot_Category':'Quick_Requirements_Shoot_Category',
            'Quick_Requirements_Shooting_Region':'Quick_Requirements_Shooting_Region',
            'Quick_Requirements_Creator': self.user,  # Defined in setup
            'Quick_Requirements_Modified_Date': timezone.now(),
            'Quick_Requirements_Created_Date': timezone.now(),
        })

        # Check for successful response
        self.assertEqual(response.status_code, 200)

        # Check response values
        self.assertContains(response, '1')
        self.assertContains(response, self.user.username)
        self.assertContains(response, 'checked')
        self.assertContains(response, self.user.username)
        self.assertContains(response, 'Quick_Requirements_Requirement_Description')
        self.assertContains(response, 'Quick_Requirements_Shoot_Category')
        self.assertContains(response, 'Quick_Requirements_Shooting_Region')
        self.assertContains(response, self.user.username)  # Same as defined in SetUp

        # Check for correct template used in template/Quick_Requirementss
        self.assertTemplateUsed(response, 'Quick_Requirements/Quick_Requirements_new.html')

    # ---------------------------------------------------------------------------------------#

    # Test Quick_Requirements Update view

    def test_Quick_Requirementsupdate_view(self):
        # Login the user
        self.client.login(username='testuser', password='test')

        # Find primary key of table
        Quick_Requirements_pk = Quick_Requirements.objects.get(Quick_Requirements_Requirement_Description='Quick_Requirements_Requirement_Description').pk

        # Get response using pk on details view
        response = self.client.get(reverse_lazy('Quick_Requirements_details', kwargs={'pk': Quick_Requirements_pk}), {
            'Quick_Requirements_Crew_Size': '1',
            'Quick_Requirements_From_User': self.user.username,
            'Quick_Requirements_New_Requirement':True,
            'Quick_Requirements_Recipient':self.user.username,
            'Quick_Requirements_Requirement_Description':'Quick_Requirements_Requirement_Description',
            'Quick_Requirements_Shoot_Category':'Quick_Requirements_Shoot_Category',
            'Quick_Requirements_Shooting_Region':'Quick_Requirements_Shooting_Region',
            'Quick_Requirements_Creator': self.user.username,
            'Quick_Requirements_Modified_Date': timezone.now(),
            'Quick_Requirements_Created_Date': timezone.now(),
        })
        # Check for successful response
        self.assertEqual(response.status_code, 200)
        print(response.content)
        # Check for correct templates
        self.assertTemplateUsed(response, 'Quick_Requirements/Quick_Requirements_detail.html')

    # --------------------------------------------------------------------------------------------#

    # Test Delete View of Quick_Requirements views

    def test_Quick_Requirementsdelete_view(self):
        # Login the user
        self.client.login(username='testuser', password='test')

        # Find primary key of table
        Quick_Requirements_pk = Quick_Requirements.objects.get(Quick_Requirements_Requirement_Description='Quick_Requirements_Requirement_Description').pk

        # Get response to delete

        response = self.client.get(reverse_lazy('Quick_Requirements_delete', kwargs={'pk': Quick_Requirements_pk}))
        self.assertContains(response, 'Are you sure you want to delete')  # THIS PART WORKS

        # Check deleted value , returns false i.e.302
        post_response = self.client.post(reverse_lazy('Quick_Requirements_delete', kwargs={'pk': Quick_Requirements_pk}))

        # self.assertRedirects(post_response, reverse_lazy('Quick_Requirements_delete',kwargs={'pk':Quick_Requirements_pk}), status_code=302)

        self.assertEqual(response.status_code, 200)

        # check for Correct Template Used
        self.assertTemplateUsed(response, 'Quick_Requirements/Quick_Requirements_delete.html')


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
# #         response = self.client.get('/Quick_Requirementss/1/')
#
# #         self.assertEqual(response.status_code, 200)
#
#
# # ------------------------------------------------------------------------------------------------------#
#
#
# #     # def test_update_page_status_code(self):
# #     #     # url = reverse('Quick_RequirementsListView')
# #     #     response = self.client.get('/Quick_Requirementss/1/')
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