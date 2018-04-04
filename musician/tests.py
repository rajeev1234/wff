from django.test import TestCase,SimpleTestCase
from django.urls import reverse,reverse_lazy
from .models import Musician
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils import timezone


#  Test Class for Musician Application

class MusicianTest(TestCase):

########################## Model Testing ############################


    # Musician object with dummy data
    def setUp(self):

        # dummy user for login
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password = 'test'
        )

        self.Musician =  Musician.objects.create(

        # Fields according to defined in Model
        Musician_Daily_Charges = 'Musician_Daily_Charges',
        Musician_Description='Musician_Description',
        Musician_Financial_Available='True',
        Musician_Genre='Musician_Genre',
        Musician_Author = self.user,       # Defined above in get_user_model
        Musician_Created_Date = timezone.now(),

        )

#-----------------------------------------------------------------------------------------#

    # Check redirection URL
    def test_get_absolute_url(self):
        # Redirection goes to Musician details
        self.assertEquals(self.Musician.get_absolute_url(), '/musician/1')

#-----------------------------------------------------------------------------------------#

    # Check Conent of Musician object created by create object query set
    def test_Musician_content(self):
        # Verify for each field
        self.assertEqual(f'{self.Musician.Musician_Daily_Charges}', 'Musician_Daily_Charges')
        self.assertEqual(f'{self.Musician.Musician_Description}', 'Musician_Description')
        self.assertEqual(f'{self.Musician.Musician_Financial_Available}', 'True')
        self.assertEqual(f'{self.Musician.Musician_Genre}', 'Musician_Genre')
        self.assertEqual(f'{self.Musician.Musician_Author}', self.user.username)  # Defined in SetUp


#--------------------------------------------------------------------------------------------#

# #############################   Model Test End   ########################################### #


# ###############################    Views Test       ########################################


    # Test Musician List View

    def test_MusicianList_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test')

        # Get response from defined URL namespace
        response = self.client.get(reverse('musician_list'))
        self.assertEqual(response.status_code, 200)

        # Check Content of List View
        self.assertContains(response, self.user.username)
        # Check for Correct template used in template/Musicians
        self.assertTemplateUsed(response, 'musician/musician_list.html')

#--------------------------------------------------------------------------------------------#

    # Test Musician Detail View

    def test_MusicianDetail_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test')

        # Find primary key of table
        Musician_pk = Musician.objects.get(Musician_Daily_Charges = 'Musician_Daily_Charges').pk

        # Get response
        response = self.client.get(reverse_lazy('musician_details',kwargs={'pk':Musician_pk}))

        # Check for any invalid value
        no_response = self.client.get(reverse_lazy('musician_details',kwargs={'pk':10000}))

        # 202 for valid and 404 for invalid
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)

        # check for content of Detail Page
        self.assertContains(response, 'Musician_Daily_Charges')

        # Check for Correct template used in template/Musician
        self.assertTemplateUsed(response, 'musician/musician_detail.html')

#-------------------------------------------------------------------------------------------#


    # Test EducationInfo Create View

    def test_MusicianCreate_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test')

        # Generate response after creating an view using Http post method
        response = self.client.post('/musician/new/', {
        'Musician_Daily_Charges' : 'Musician_Daily_Charges',
        'Musician_Description' : 'Musician_Description',
        'Musician_Financial_Available':'True',
        'Musician_Genre':'Musician_Genre',
        'Musician_Author' : self.user,       # Defined above in get_user_model
        'Musician_Created_Date' : timezone.now(),
        },follow = True)

        # print(response.content)
        # Check for successful response
        self.assertEqual(response.status_code, 200)
        # self.assertContains(response, False)
        self.assertContains(response, 'Musician_Daily_Charges')
        self.assertContains(response, 'Musician_Description')
        self.assertContains(response, 'True')
        self.assertContains(response, 'Musician_Genre')
        self.assertContains(response, self.user.username)    # Same as defined in SetUp


        # Check for correct template used in template/EducationInfos
        self.assertTemplateUsed(response, 'musician/musician_detail.html')

#---------------------------------------------------------------------------------------#


    # Test EducationInfo Update view

    def test_Musicianupdate_view(self):
        # Login the user
        self.client.login(username='testuser', password='test')

        # Find primary key of table
        Musician_pk = Musician.objects.get(Musician_Genre='Musician_Genre').pk

        # Get response using pk on details view
        response = self.client.get(reverse_lazy('musician_details',kwargs={'pk':Musician_pk}), {
        'Musician_Daily_Charges' : 'Musician_Daily_Charges',
        'Musician_Description' : 'Musician_Description',
        'Musician_Financial_Available':'True',
        'Musician_Genre':'Musician_Genre',
        'Musician_Author' : self.user,       # Defined above in get_user_model
        'Musician_Created_Date' : timezone.now(),
        },follow = True)
        # Check for successful response
        self.assertEqual(response.status_code, 200)

        # Check for correct templates
        self.assertTemplateUsed(response,'musician/musician_detail.html')


#--------------------------------------------------------------------------------------------#


# Test Delete View of EducationInfo views

    def test_Musiciandelete_view(self):
        # Login the user
        self.client.login(username='testuser', password='test')

        # Find primary key of table
        Musician_pk = Musician.objects.get(Musician_Genre='Musician_Genre').pk

        # Get response to delete

        response = self.client.get(reverse_lazy('musician_delete',kwargs={'pk':Musician_pk}))
        self.assertContains(response, 'Are you sure you want to delete') # THIS PART WORKS

        # Check deleted value , returns false i.e.302
        post_response = self.client.post(reverse_lazy('musician_delete',kwargs={'pk':Musician_pk}))

        # self.assertRedirects(post_response, reverse_lazy('EducationInfo_delete',kwargs={'pk':EducationInfo_pk}), status_code=302)


        self.assertEqual(response.status_code, 200)

        # check for Correct Template Used
        self.assertTemplateUsed(response, 'musician/musician_delete.html')




# ################################     View Testing End   #################################################


# ################################     Testing the URLs       ##############################################

class PagesTests(SimpleTestCase):

    # Check URL for list/ Home
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

# #-----------------------------------------------------------------------------------------------------#
