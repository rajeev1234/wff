from django.test import TestCase,SimpleTestCase
from django.urls import reverse,reverse_lazy
from .models import MimicryArtist
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.forms.models import model_to_dict


#  Test Class for Costume Application

class MimicryArtistTest(TestCase):

########################## Model Testing ############################


    # Costume object with dummy data
    def setUp(self):
        # User for login
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password = 'test'
        )

        self.MimicryArtist =  MimicryArtist.objects.create(

        # Fields according to defined in Model
        MimicryArtist_Daily_Financials = 'MimicryArtist_Daily_Financials', #Defined above in get_user_model
        MimicryArtist_Description = 'MimicryArtist_Description',
        MimicryArtist_Financials_Available = True,
        MimicryArtist_Voices = 'MimicryArtist_Voices',
        MimicryArtist_Author = self.user,
        MimicryArtist_Created_Date = timezone.now(),

        )

#-----------------------------------------------------------------------------------------#

    # Check redirection URL
    def test_get_absolute_url(self):
        # Redirection goes to costume details
        self.assertEquals(self.MimicryArtist.get_absolute_url(), '/mimicry_artist/1')

#-----------------------------------------------------------------------------------------#

    # Check Conent of costume object created by create object query set
    def test_MimicryArtist_content(self):
        # Verify for each field
        self.assertEqual(f'{self.MimicryArtist.MimicryArtist_Daily_Financials}', 'MimicryArtist_Daily_Financials')
        self.assertEqual(f'{self.MimicryArtist.MimicryArtist_Description}', 'MimicryArtist_Description')
        self.assertEqual(bool(f'{self.MimicryArtist.MimicryArtist_Financials_Available}'), True)   #Defined in SetUp
        self.assertEqual(f'{self.MimicryArtist.MimicryArtist_Voices}', 'MimicryArtist_Voices')
        self.assertEqual(f'{self.MimicryArtist.MimicryArtist_Author}', self.user.username)


#--------------------------------------------------------------------------------------------#

# #############################   Model Test End   ###########################################







# ###############################    Views Test       ########################################


    # Test Costume List View

    def test_MimicryArtistList_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test')

        # Get respomse from defined URL namespace
        response = self.client.get(reverse('mimicry_artist_list'))
        self.assertEqual(response.status_code, 200)

        # Check Content of List View
        self.assertContains(response,self.user.username)
        # Check for Correct template used in template/Costumes
        self.assertTemplateUsed(response, 'mimicry_artists/mimicry_artist_list.html')

#--------------------------------------------------------------------------------------------#


    # Test LocationFinancial Detail View

    def test_MimicryArtistDetail_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test')

        # Find primary key of table
        MimicryArtist_pk = MimicryArtist.objects.get(MimicryArtist_Description = 'MimicryArtist_Description').pk

        # Get response
        response = self.client.get(reverse_lazy('mimicry_artist_details',kwargs={'pk':MimicryArtist_pk}))

        # Check for any invalid value
        no_response = self.client.get(reverse_lazy('mimicry_artist_details',kwargs={'pk':10000}))

        # 202 for valid and 404 for invalid
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)

        # check for content of Detail Page
        self.assertContains(response, 'MimicryArtist_Description')

        # Check for Correct template used in template/LocationFinancials
        self.assertTemplateUsed(response, 'mimicry_artists/mimicry_artist_detail.html')

#-------------------------------------------------------------------------------------------#


    # Test Costume Create View

    def test_MimicryArtistCreate_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test')

        # Generate response after creating an view using Http post method
        response = self.client.post('/mimicry_artist/new/', {
        'MimicryArtist_Daily_Financials' : 'MimicryArtist_Daily_Financials', #Defined above in get_user_model
        'MimicryArtist_Description' : 'MimicryArtist_Description',
        'MimicryArtist_Financials_Available' : True,
        'MimicryArtist_Voices' : 'MimicryArtist_Voices',
        'MimicryArtist_Author' : self.user,
        'MimicryArtist_Created_Date' : timezone.now(),
        })

        print(response.content)
        # Check for successful response
        self.assertEqual(response.status_code, 200)

        # Check response values
        self.assertContains(response, 'MimicryArtist_Daily_Financials')
        self.assertContains(response, 'MimicryArtist_Description')
        self.assertContains(response, 'checked')    # Same as defined in SetUp
        self.assertContains(response, 'MimicryArtist_Voices')
        self.assertContains(response, self.user.username)

        # Check for correct template used in template/message
        self.assertTemplateUsed(response, 'mimicry_artists/mimicry_artist_new.html')

#---------------------------------------------------------------------------------------#


    # Test Messages_Subject Update view

    def test_MimicryArtistupdate_view(self):
        # Login the user
        self.client.login(username='testuser', password='test')

        # Find primary key of table
        MimicryArtist_pk = MimicryArtist.objects.get(MimicryArtist_Description='MimicryArtist_Description').pk

        # Get response using pk on details view
        response = self.client.get(reverse_lazy('mimicry_artist_details',kwargs={'pk':MimicryArtist_pk}), {
        'MimicryArtist_Daily_Financials' : 'MimicryArtist_Daily_Financials', #Defined above in get_user_model
        'MimicryArtist_Description' : 'MimicryArtist_Description',
        'MimicryArtist_Financials_Available' : 'True',
        'MimicryArtist_Voices' : 'MimicryArtist_Voices',
        'MimicryArtist_Author' : self.user,
        'MimicryArtist_Created_Date' : timezone.now(),
        },follow = True)
        #Check for successful response
        self.assertEqual(response.status_code, 200)

        # Check for correct templates
        self.assertTemplateUsed(response,'mimicry_artists/mimicry_artist_detail.html')


#--------------------------------------------------------------------------------------------#


# Test Delete View of message views

    def test_MimicryArtistdelete_view(self):
        # Login the user
        self.client.login(username='testuser', password='test')

        # Find primary key of table
        MimicryArtist_pk = MimicryArtist.objects.get(MimicryArtist_Description='MimicryArtist_Description').pk

        # Get response to delete

        response = self.client.get(reverse_lazy('mimicry_artist_delete',kwargs={'pk':MimicryArtist_pk}))
        self.assertContains(response, 'Are you sure you want to delete') # THIS PART WORKS

        # Check deleted value , returns false i.e.302
        post_response = self.client.post(reverse_lazy('mimicry_artist_delete',kwargs={'pk':MimicryArtist_pk}))

        # self.assertRedirects(post_response, reverse_lazy('Costume_delete',kwargs={'pk':Costume_pk}), status_code=302)


        self.assertEqual(response.status_code, 200)

        # check for Correct Template Used
        self.assertTemplateUsed(response, 'mimicry_artists/mimicry_artist_delete.html')




# ################################     View Testing End   #################################################



# ################################     Testing the URLs       ##############################################

class PagesTests(SimpleTestCase):

    # Check URL for list/ Home
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

# #-----------------------------------------------------------------------------------------------------#

#     # URL for new
#     def test_new_page_status_code(self):
#         # Login the user defined in SetUp
#         # self.client.login(username='testuser', password='test')

#         # Get response
#         response = self.client.get('/costumes/1/')

#         self.assertEqual(response.status_code, 200)


#------------------------------------------------------------------------------------------------------#


#     # def test_update_page_status_code(self):
#     #     # url = reverse('CostumeListView')
#     #     response = self.client.get('/costumes/1/')
#     #     self.assertEqual(response.status_code, 200)

#-------------------------------------------------------------------------------------------------------#

#     # def test_detail_page_status_code(self):
#     #     response = self.client.get('/{1}/')
#     #     self.assertEqual(response.status_code, 200)

#-------------------------------------------------------------------------------------------------------#

#     # def test_delete_page_status_code(self):
#     #     response = self.client.get('/{1}/delete/')
#     #     self.assertEqual(response.status_code, 200)
