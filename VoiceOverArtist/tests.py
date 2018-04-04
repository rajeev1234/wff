from django.test import TestCase,SimpleTestCase
from django.urls import reverse,reverse_lazy
from .models import VoiceOverArtist
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils import timezone



#  Test Class for VoiceOverArtist Application

class VoiceOverArtistTest(TestCase):

########################## Model Testing ############################
  

    # VoiceOverArtist object with dummy data 
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password = 'test'
        )

        self.VoiceOverArtist =  VoiceOverArtist.objects.create(# Fields according to defined in Model    
        VoiceOverArtist_Voice_Over_Artist='VoiceOverArtist_Voice_Over_Artist',
VoiceOverArtist_Charges_Available=True,
VoiceOverArtist_Daily_Charges=125,
VoiceOverArtist_Description='VoiceOverArtist_Description',
VoiceOverArtist_Language='VoiceOverArtist_Language',
VoiceOverArtist_Voice_Over_Artist_ID=125,
VoiceOverArtist_Voice_Scale='VoiceOverArtist_Voice_Scale',
VoiceOverArtist_Voice_Over_Artist_Message='VoiceOverArtist_Voice_Over_Artist_Message')

#
    #Check redirection URL
    def test_get_absolute_url(self):
        # Redirection goes to VoiceOverArtist details
        self.assertEquals(self.VoiceOverArtist.get_absolute_url(), '/voiceoverartist/1')

# #-----------------------------------------------------------------------------------------#

#     # Check Conent of VoiceOverArtist object
    def test_VoiceOverArtist_content(self):
        self.assertEqual(str(self.VoiceOverArtist.VoiceOverArtist_Voice_Over_Artist),'VoiceOverArtist_Voice_Over_Artist')
        self.assertEqual(bool(str(self.VoiceOverArtist.VoiceOverArtist_Charges_Available)),True)
        self.assertEqual(int(str(self.VoiceOverArtist.VoiceOverArtist_Daily_Charges)),125)
        self.assertEqual(str(self.VoiceOverArtist.VoiceOverArtist_Description), 'VoiceOverArtist_Description')
        self.assertEqual(str(self.VoiceOverArtist.VoiceOverArtist_Language),'VoiceOverArtist_Language')
        self.assertEqual(int(str(self.VoiceOverArtist.VoiceOverArtist_Voice_Over_Artist_ID)),125)
        self.assertEqual(str(self.VoiceOverArtist.VoiceOverArtist_Voice_Scale),'VoiceOverArtist_Voice_Scale')
        self.assertEqual(str(self.VoiceOverArtist.VoiceOverArtist_Voice_Over_Artist_Message),'VoiceOverArtist_Voice_Over_Artist_Message')
       

# # # #############################   Model Test End   ###########################################







# # ###############################    Views Test       ########################################

    
#     # Test VoiceOverArtist List View
    
    def test_VoiceOverArtistList_view(self):
        # Get respomse from defined URL namespace
        response = self.client.get(reverse('voiceoverartist_list'))
        self.assertEqual(response.status_code, 200)

        # Check Content of List View
        #self.assertContains(response,self.user.username)
        # Check for Correct template used in template/VoiceOverArtists
        self.assertTemplateUsed(response, 'voiceoverartist/voiceoverartist_list.html')

# #--------------------------------------------------------------------------------------------#
    

#     # Test VoiceOverArtist Detail View

    def test_VoiceOverArtistDetail_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test')
        
        # Find primary key of table
        VoiceOverArtist_pk = VoiceOverArtist.objects.get(VoiceOverArtist_Voice_Over_Artist='VoiceOverArtist_Voice_Over_Artist').pk
        
        # Get response
        response = self.client.get(reverse_lazy('voiceoverartist_details',kwargs={'pk':VoiceOverArtist_pk}))

        # Check for any invalid value
        no_response = self.client.get(reverse_lazy('voiceoverartist_details',kwargs={'pk':10000}))

        # 202 for valid and 404 for invalid
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)

        # check for content of Detail Page
        self.assertContains(response, 'VoiceOverArtist_Voice_Over_Artist')

        # Check for Correct template used in template/VoiceOverArtists
        self.assertTemplateUsed(response, 'voiceoverartist/voiceoverartist_detail.html')

# #-------------------------------------------------------------------------------------------#    


#     # Test VoiceOverArtist Create View
    
    def test_VoiceOverArtistCreate_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test') 

        # Generate response after creating an view using Http post method
        response = self.client.post('/voiceoverartist/new/',{
        	'VoiceOverArtist_Voice_Over_Artist':'VoiceOverArtist_Voice_Over_Artist',
            'VoiceOverArtist_Charges_Available':True,
            'VoiceOverArtist_Daily_Charges':125,
            'VoiceOverArtist_Description':'VoiceOverArtist_Description',
            'VoiceOverArtist_Language':'VoiceOverArtist_Language',
            'VoiceOverArtist_Voice_Over_Artist_ID':125,
            'VoiceOverArtist_Voice_Scale':'VoiceOverArtist_Voice_Scale',
            'VoiceOverArtist_Voice_Over_Artist_Message':'VoiceOverArtist_Voice_Over_Artist_Message',
        },follow=True)

        # Check for successful response
        print(response.content)
        self.assertEqual(response.status_code, 200)

        # Check response values
        self.assertContains(response, 'VoiceOverArtist_Voice_Over_Artist')
        self.assertContains(response, 'True')
        self.assertContains(response, 125)
        self.assertContains(response, 'VoiceOverArtist_Description')
        self.assertContains(response, 'VoiceOverArtist_Language')
        self.assertContains(response, 125)
        self.assertContains(response, 'VoiceOverArtist_Voice_Scale')
        self.assertContains(response, 'VoiceOverArtist_Voice_Over_Artist_Message')
         # Same as defined in SetUp
         # Same as defined in SetUp

        # Check for correct template used in template/VoiceOverArtists
        self.assertTemplateUsed(response, 'voiceoverartist/voiceoverartist_detail.html')

# #---------------------------------------------------------------------------------------#


#     # Test VoiceOverArtist Update view 

    def test_VoiceOverArtistupdate_view(self):
        # Login the user
        self.client.login(username='testuser', password='test')
        
        # Find primary key of table
        VoiceOverArtist_pk = VoiceOverArtist.objects.get(VoiceOverArtist_Voice_Over_Artist='VoiceOverArtist_Voice_Over_Artist').pk
        
        # Get response using pk on details view
        response = self.client.get(reverse_lazy('voiceoverartist_details',kwargs={'pk':VoiceOverArtist_pk}), {
'VoiceOverArtist_Voice_Over_Artist':'VoiceOverArtist_Voice_Over_Artist',
'VoiceOverArtist_Charges_Available':True,
'VoiceOverArtist_Daily_Charges':125,
'VoiceOverArtist_Description':'VoiceOverArtist_Description',
'VoiceOverArtist_Language':'VoiceOverArtist_Language',
'VoiceOverArtist_Voice_Over_Artist_ID':125,
'VoiceOverArtist_Voice_Scale':'VoiceOverArtist_Voice_Scale',
'VoiceOverArtist_Voice_Over_Artist_Message':'VoiceOverArtist_Voice_Over_Artist_Message',
        })
        # Check for successful response
        self.assertEqual(response.status_code, 200)
