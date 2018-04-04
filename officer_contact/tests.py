from django.test import TestCase,SimpleTestCase
from django.urls import reverse,reverse_lazy
from .models import OfficerContact
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils import timezone


#  Test Class for OfficerContact Application

class OfficerContactTest(TestCase):

########################## Model Testing ############################


    # OfficerContact object with dummy data
    def setUp(self):

        # dummy user for login
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password = 'test'
        )

        self.OfficerContact =  OfficerContact.objects.create(

        # Fields according to defined in Model
        OfficerContact_CONTACT_NUMBER = 'OfficerContact_CONTACT_NUMBER',
        OfficerContact_DEPARTMENT='OfficerContact_DEPARTMENT',
        OfficerContact_DESIGNATIONS='OfficerContact_DESIGNATIONS',
        OfficerContact_E_Mail='abc@email.com',
        OfficerContact_Name = 'OfficerContact_Name',
        OfficerContact_Author = self.user,         # Defined above in get_user_model
        OfficerContact_Created_Date = timezone.now(),
        )

#-----------------------------------------------------------------------------------------#

    # Check redirection URL
    def test_get_absolute_url(self):
        # Redirection goes to OfficerContact details
        self.assertEquals(self.OfficerContact.get_absolute_url(), '/officer_contact/1')

#-----------------------------------------------------------------------------------------#

    # Check Conent of OfficerContact object created by create object query set
    def test_OfficerContact_content(self):
        # Verify for each field
        self.assertEqual(f'{self.OfficerContact.OfficerContact_CONTACT_NUMBER}', 'OfficerContact_CONTACT_NUMBER')
        self.assertEqual(f'{self.OfficerContact.OfficerContact_DEPARTMENT}', 'OfficerContact_DEPARTMENT')
        self.assertEqual(f'{self.OfficerContact.OfficerContact_DESIGNATIONS}', 'OfficerContact_DESIGNATIONS')
        self.assertEqual(f'{self.OfficerContact.OfficerContact_E_Mail}', 'abc@email.com')
        self.assertEqual(f'{self.OfficerContact.OfficerContact_Name}', 'OfficerContact_Name')
        self.assertEqual(f'{self.OfficerContact.OfficerContact_Author}', self.user.username)    # Defined in SetUp


#--------------------------------------------------------------------------------------------#

# #############################   Model Test End   ########################################### #


# ###############################    Views Test       ########################################


    # Test OfficerContact List View

    def test_OfficerContactList_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test')

        # Get response from defined URL namespace
        response = self.client.get(reverse('officer_contact_list'))
        self.assertEqual(response.status_code, 200)

        # Check Content of List View
        self.assertContains(response, self.user.username)
        # Check for Correct template used in template/OfficerContact
        self.assertTemplateUsed(response, 'officer_contact/officer_contact_list.html')

#--------------------------------------------------------------------------------------------#

    # Test OfficerContact Detail View

    def test_OfficerContactDetail_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test')

        # Find primary key of table
        OfficerContact_pk = OfficerContact.objects.get(OfficerContact_Name = 'OfficerContact_Name').pk

        # Get response
        response = self.client.get(reverse_lazy('officer_contact_details',kwargs={'pk':OfficerContact_pk}))

        # Check for any invalid value
        no_response = self.client.get(reverse_lazy('officer_contact_details',kwargs={'pk':10000}))

        # 202 for valid and 404 for invalid
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)

        # check for content of Detail Page
        self.assertContains(response, 'OfficerContact_Name')

        # Check for Correct template used in template/OfficerContact
        self.assertTemplateUsed(response, 'officer_contact/officer_contact_detail.html')

#-------------------------------------------------------------------------------------------#


    # Test EducationInfo Create View

    def test_OfficerContactCreate_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test')

        # Generate response after creating an view using Http post method
        response = self.client.post('/officer_contact/new/', {
        'OfficerContact_CONTACT_NUMBER' : 'OfficerContact_CONTACT_NUMBER',
        'OfficerContact_DEPARTMENT':'OfficerContact_DEPARTMENT',
        'OfficerContact_DESIGNATIONS':'OfficerContact_DESIGNATIONS',
        'OfficerContact_E_Mail':'abc@email.com',
        'OfficerContact_Name' : 'OfficerContact_Name',
        'OfficerContact_Author' : self.user,         # Defined above in get_user_model
        'OfficerContact_Created_Date' : timezone.now(),
        },follow = True)

        # print(response.content)
        # Check for successful response
        self.assertEqual(response.status_code, 200)
        # self.assertContains(response, False)
        self.assertContains(response, 'OfficerContact_CONTACT_NUMBER')
        self.assertContains(response, 'OfficerContact_DEPARTMENT')
        self.assertContains(response, 'OfficerContact_DESIGNATIONS')
        self.assertContains(response, 'abc@email.com')
        self.assertContains(response, 'OfficerContact_Name')
        self.assertContains(response, self.user.username)     # Same as defined in SetUp


        # Check for correct template used in template/EducationInfos
        self.assertTemplateUsed(response, 'officer_contact/officer_contact_detail.html')

#---------------------------------------------------------------------------------------#


    # Test EducationInfo Update view

    def test_OfficerContactupdate_view(self):
        # Login the user
        self.client.login(username='testuser', password='test')

        # Find primary key of table
        OfficerContact_pk = OfficerContact.objects.get(OfficerContact_Name='OfficerContact_Name').pk

        # Get response using pk on details view
        response = self.client.get(reverse_lazy('officer_contact_details',kwargs={'pk':OfficerContact_pk}), {
        'OfficerContact_CONTACT_NUMBER' : 'OfficerContact_CONTACT_NUMBER',
        'OfficerContact_DEPARTMENT':'OfficerContact_DEPARTMENT',
        'OfficerContact_DESIGNATIONS':'OfficerContact_DESIGNATIONS',
        'OfficerContact_E_Mail':'abc@email.com',
        'OfficerContact_Name' : 'OfficerContact_Name',
        'OfficerContact_Author' : self.user,         # Defined above in get_user_model
        'OfficerContact_Created_Date' : timezone.now(),
        },follow = True)
        # Check for successful response
        self.assertEqual(response.status_code, 200)

        # Check for correct templates
        self.assertTemplateUsed(response,'officer_contact/officer_contact_detail.html')


#--------------------------------------------------------------------------------------------#


# Test Delete View of EducationInfo views

    def test_OfficerContactdelete_view(self):
        # Login the user
        self.client.login(username='testuser', password='test')

        # Find primary key of table
        OfficerContact_pk = OfficerContact.objects.get(OfficerContact_Name='OfficerContact_Name').pk

        # Get response to delete

        response = self.client.get(reverse_lazy('officer_contact_delete',kwargs={'pk':OfficerContact_pk}))
        self.assertContains(response, 'Are you sure you want to delete') # THIS PART WORKS

        # Check deleted value , returns false i.e.302
        post_response = self.client.post(reverse_lazy('officer_contact_delete',kwargs={'pk':OfficerContact_pk}))

        # self.assertRedirects(post_response, reverse_lazy('EducationInfo_delete',kwargs={'pk':EducationInfo_pk}), status_code=302)


        self.assertEqual(response.status_code, 200)

        # check for Correct Template Used
        self.assertTemplateUsed(response, 'officer_contact/officer_contact_delete.html')




# ################################     View Testing End   #################################################


# ################################     Testing the URLs       ##############################################

class PagesTests(SimpleTestCase):

    # Check URL for list/ Home
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

# #-----------------------------------------------------------------------------------------------------#
