from django.test import TestCase,SimpleTestCase
from django.urls import reverse,reverse_lazy
from .models import PermitQuery
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils import timezone


#  Test Class for PermitQuery Application

class PermitQueryTest(TestCase):

########################## Model Testing ############################


    # PermitQuery object with dummy data
    def setUp(self):

        # dummy user for login
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password = 'test'
        )

        self.PermitQuery =  PermitQuery.objects.create(

        # Fields according to defined in Model
        PermitQuery_API_Address = 'PermitQuery_API_Address',
        PermitQuery_City_State_Country='PermitQuery_City_State_Country',
        PermitQuery_Latitude=1,
        PermitQuery_Location='PermitQuery_Location',
        PermitQuery_Longitude = 1,
        PermitQuery_Map_Address = 'PermitQuery_Map_Address',
        Permit_Query_Number = 1,
        PermitQuery_Query_Mode = 'PermitQuery_Query_Mode',
        PermitQuery_Street_Address = 'PermitQuery_Street_Address',
        PermitQuery_Author = self.user,      # Defined above in get_user_model
        PermitQuery_Created_Date = timezone.now(),

        )

#-----------------------------------------------------------------------------------------#

    # Check redirection URL
    def test_get_absolute_url(self):
        # Redirection goes to PermitQuery details
        self.assertEquals(self.PermitQuery.get_absolute_url(), '/permit_query/1')

#-----------------------------------------------------------------------------------------#

    # Check Conent of PermitQuery object created by create object query set
    def test_PermitQuery_content(self):
        # Verify for each field
        self.assertEqual(f'{self.PermitQuery.PermitQuery_API_Address}', 'PermitQuery_API_Address')
        self.assertEqual(f'{self.PermitQuery.PermitQuery_City_State_Country}', 'PermitQuery_City_State_Country')
        self.assertEqual(f'{self.PermitQuery.PermitQuery_Latitude}', '1')
        self.assertEqual(f'{self.PermitQuery.PermitQuery_Location}', 'PermitQuery_Location')
        self.assertEqual(f'{self.PermitQuery.PermitQuery_Longitude}', '1')
        self.assertEqual(f'{self.PermitQuery.PermitQuery_Map_Address}', 'PermitQuery_Map_Address')
        self.assertEqual(f'{self.PermitQuery.Permit_Query_Number}', '1')
        self.assertEqual(f'{self.PermitQuery.PermitQuery_Query_Mode}', 'PermitQuery_Query_Mode')
        self.assertEqual(f'{self.PermitQuery.PermitQuery_Street_Address}', 'PermitQuery_Street_Address')
        self.assertEqual(f'{self.PermitQuery.PermitQuery_Author}', self.user.username)   # Defined in SetUp


#--------------------------------------------------------------------------------------------#

# #############################   Model Test End   ########################################### #


# ###############################    Views Test       ########################################


    # Test PermitQuery List View

    def test_PermitQueryList_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test')

        # Get response from defined URL namespace
        response = self.client.get(reverse('permit_query_list'))
        self.assertEqual(response.status_code, 200)

        # Check Content of List View
        self.assertContains(response, self.user.username)
        # Check for Correct template used in template/PermitQuery
        self.assertTemplateUsed(response, 'permit_query/permit_query_list.html')

#--------------------------------------------------------------------------------------------#

    # Test PermitQuery Detail View

    def test_PermitQueryDetail_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test')

        # Find primary key of table
        PermitQuery_pk = PermitQuery.objects.get(PermitQuery_Location = 'PermitQuery_Location').pk

        # Get response
        response = self.client.get(reverse_lazy('permit_query_details',kwargs={'pk':PermitQuery_pk}))

        # Check for any invalid value
        no_response = self.client.get(reverse_lazy('permit_query_details',kwargs={'pk':10000}))

        # 202 for valid and 404 for invalid
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)

        # check for content of Detail Page
        self.assertContains(response, 'PermitQuery_Location')

        # Check for Correct template used in template/PermitQuery
        self.assertTemplateUsed(response, 'permit_query/permit_query_detail.html')

#-------------------------------------------------------------------------------------------#


    # Test PermitQuery Create View

    def test_PermitQueryCreate_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test')

        # Generate response after creating an view using Http post method
        response = self.client.post('/permit_query/new/', {
        'PermitQuery_API_Address' : 'PermitQuery_API_Address',
        'PermitQuery_City_State_Country':'PermitQuery_City_State_Country',
        'PermitQuery_Latitude':1,
        'PermitQuery_Location':'PermitQuery_Location',
        'PermitQuery_Longitude' : 1,
        'PermitQuery_Map_Address' : 'PermitQuery_Map_Address',
        'Permit_Query_Number' : 1,
        'PermitQuery_Query_Mode' : 'PermitQuery_Query_Mode',
        'PermitQuery_Street_Address' : 'PermitQuery_Street_Address',
        'PermitQuery_Author' : self.user,      # Defined above in get_user_model
        'PermitQuery_Created_Date' : timezone.now(),
        },follow = True)

        # print(response.content)
        # Check for successful response
        self.assertEqual(response.status_code, 200)
        # self.assertContains(response, False)
        self.assertContains(response, 'PermitQuery_API_Address')
        self.assertContains(response, 'PermitQuery_City_State_Country')
        self.assertContains(response, '1')
        self.assertContains(response, 'PermitQuery_Location')
        self.assertContains(response, '1')
        self.assertContains(response, 'PermitQuery_Map_Address')
        self.assertContains(response, '1')
        self.assertContains(response, 'PermitQuery_Query_Mode')
        self.assertContains(response, 'PermitQuery_Street_Address')
        self.assertContains(response, self.user.username)    # Same as defined in SetUp


        # Check for correct template used in template/EducationInfos
        self.assertTemplateUsed(response, 'permit_query/permit_query_detail.html')

#---------------------------------------------------------------------------------------#


    # Test EducationInfo Update view

    def test_PermitQueryupdate_view(self):
        # Login the user
        self.client.login(username='testuser', password='test')

        # Find primary key of table
        PermitQuery_pk = PermitQuery.objects.get(PermitQuery_Location='PermitQuery_Location').pk

        # Get response using pk on details view
        response = self.client.get(reverse_lazy('permit_query_details',kwargs={'pk':PermitQuery_pk}), {
        'PermitQuery_API_Address' : 'PermitQuery_API_Address',
        'PermitQuery_City_State_Country':'PermitQuery_City_State_Country',
        'PermitQuery_Latitude':1,
        'PermitQuery_Location':'PermitQuery_Location',
        'PermitQuery_Longitude' : 1,
        'PermitQuery_Map_Address' : 'PermitQuery_Map_Address',
        'Permit_Query_Number' : 1,
        'PermitQuery_Query_Mode' : 'PermitQuery_Query_Mode',
        'PermitQuery_Street_Address' : 'PermitQuery_Street_Address',
        'PermitQuery_Author' : self.user,      # Defined above in get_user_model
        'PermitQuery_Created_Date' : timezone.now(),
        },follow = True)

        # Check for successful response
        self.assertEqual(response.status_code, 200)

        # Check for correct templates
        self.assertTemplateUsed(response,'permit_query/permit_query_detail.html')


#--------------------------------------------------------------------------------------------#


# Test Delete View of PermitQuery views

    def test_PermitQuerydelete_view(self):
        # Login the user
        self.client.login(username='testuser', password='test')

        # Find primary key of table
        PermitQuery_pk = PermitQuery.objects.get(PermitQuery_Location='PermitQuery_Location').pk

        # Get response to delete

        response = self.client.get(reverse_lazy('permit_query_delete',kwargs={'pk':PermitQuery_pk}))
        self.assertContains(response, 'Are you sure you want to delete') # THIS PART WORKS

        # Check deleted value , returns false i.e.302
        post_response = self.client.post(reverse_lazy('permit_query_delete',kwargs={'pk':PermitQuery_pk}))

        # self.assertRedirects(post_response, reverse_lazy('PermitQuery_delete',kwargs={'pk':PermitQuery_pk}), status_code=302)


        self.assertEqual(response.status_code, 200)

        # check for Correct Template Used
        self.assertTemplateUsed(response, 'permit_query/permit_query_delete.html')




# ################################     View Testing End   #################################################


# ################################     Testing the URLs       ##############################################

class PagesTests(SimpleTestCase):

    # Check URL for list/ Home
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

# #-----------------------------------------------------------------------------------------------------#
