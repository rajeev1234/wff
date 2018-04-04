from django.test import TestCase,SimpleTestCase
from django.urls import reverse,reverse_lazy
from .models import ChildArtist
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils import timezone



#  Test Class for ChildArtist Application

class ChildArtistTest(TestCase):

########################## Model Testing ############################
  

    # ChildArtist object with dummy data 
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password = 'test'
        )

        self.ChildArtist =  ChildArtist.objects.create(
        	ChildArtist_Body_Type='Body_Type',
ChildArtist_Child_Artist_Id='Child_Artist_Id',
ChildArtist_Daily_Charges='Daily_Charges',
ChildArtist_Date_Of_Birth='Date_Of_Birth',
ChildArtist_Description='Description',
ChildArtist_Ethnicity='Ethnicity',
ChildArtist_Eye_Color='Eye_Color',
ChildArtist_Financial_Available=True,
ChildArtist_Gender='Gender',
ChildArtist_Height='Height',
ChildArtist_Relation_With_Artist='Relation_With_Artist',
ChildArtist_Skin_Color='Skin_Color',
ChildArtist_Special_Skills='Special_Skills',
ChildArtist_Weight='Weight',
)
#
    #Check redirection URL
    def test_get_absolute_url(self):
        # Redirection goes to ChildArtist details
        self.assertEquals(self.ChildArtist.get_absolute_url(), '/childartist/1')

# #-----------------------------------------------------------------------------------------#

#     # Check Conent of ChildArtist object
    def test_ChildArtist_content(self):
        self.assertEqual(str(self.ChildArtist.ChildArtist_Body_Type),'Body_Type')
        self.assertEqual(str(self.ChildArtist.ChildArtist_Child_Artist_Id), 'Child_Artist_Id')
        self.assertEqual(str(self.ChildArtist.ChildArtist_Daily_Charges), 'Daily_Charges')
        #self.assertEqual(str(self.ChildArtist.Date_Of_Birth),'Date_Of_Birth')
        self.assertEqual(str(self.ChildArtist.ChildArtist_Description), 'Description')
        self.assertEqual(str(self.ChildArtist.ChildArtist_Ethnicity), 'Ethnicity')
        self.assertEqual(str(self.ChildArtist.ChildArtist_Eye_Color), 'Eye_Color')
        self.assertEqual(bool(str(self.ChildArtist.ChildArtist_Financial_Available)),True)
        self.assertEqual(str(self.ChildArtist.ChildArtist_Gender), 'Gender')
        self.assertEqual(str(self.ChildArtist.ChildArtist_Height), 'Height')
        self.assertEqual(str(self.ChildArtist.ChildArtist_Relation_With_Artist),'Relation_With_Artist')
        self.assertEqual(str(self.ChildArtist.ChildArtist_Skin_Color), 'Skin_Color')
        self.assertEqual(str(self.ChildArtist.ChildArtist_Special_Skills), 'Special_Skills')
        self.assertEqual(str(self.ChildArtist.ChildArtist_Weight), 'Weight')


       
# #--------------------------------------------------------------------------------------------#

# # #############################   Model Test End   ###########################################







# ###############################    Views Test       ########################################

    def test_ChildArtistCreate_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test') 

    #     # Generate response after creating an view using Http post method
        response = self.client.post('/childartist/new/',{
		'ChildArtist_Body_Type':'Body_Type',
'ChildArtist_Child_Artist_Id':'Child_Artist_Id',
'ChildArtist_Daily_Charges':'Daily_Charges',
'ChildArtist_Description':'Description',
'ChildArtist_Ethnicity':'Ethnicity',
'ChildArtist_Eye_Color':'Eye_Color',
'ChildArtist_Financial_Available':True,
'ChildArtist_Gender':'Gender',
'ChildArtist_Height':'Height',
'ChildArtist_Relation_With_Artist':'Relation_With_Artist',
'ChildArtist_Skin_Color':'Skin_Color',
'ChildArtist_Special_Skills':'Special_Skills',
'ChildArtist_Weight':'Weight',
        })

    #     # Check for successful response
        self.assertEqual(response.status_code, 200)
        print(response.content)
        # Check response values
        self.assertContains(response, 'Body_Type')
        self.assertContains(response, 'Child_Artist_Id')
        self.assertContains(response, 'Daily_Charges')
        #self.assertContains(response, 'Date_Of_Birth')
        self.assertContains(response, 'Description')
        self.assertContains(response, 'Ethnicity')
        self.assertContains(response, 'Eye_Color')
        self.assertContains(response, 'checked')
        self.assertContains(response, 'Gender')
        self.assertContains(response, 'Height')
        self.assertContains(response, 'Relation_With_Artist')
        self.assertContains(response, 'Skin_Color')
        self.assertContains(response, 'Special_Skills')
        self.assertContains(response, 'Weight')
         # Same as defined in SetUp

        # Check for correct template used in template/ChildArtists
        self.assertTemplateUsed(response, 'childartist/childartist_new.html')
# #     # Test ChildArtist List View
    
    def test_ChildArtistList_view(self):
        # Get respomse from defined URL namespace
        response = self.client.get(reverse('childartist_list'))
        self.assertEqual(response.status_code, 200)

        # Check Content of List View
        #self.assertContains(response,self.user.username)
        # Check for Correct template used in template/ChildArtists
        self.assertTemplateUsed(response, 'childartist/childartist_list.html')

# # # #--------------------------------------------------------------------------------------------#
    

# # #     # Test ChildArtist Detail View

    def test_ChildArtistDetail_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test')
        
        # Find primary key of table
        ChildArtist_pk = ChildArtist.objects.get(ChildArtist_Body_Type='Body_Type').pk
        
        # Get response
        response = self.client.get(reverse_lazy('childartist_details',kwargs={'pk':ChildArtist_pk}))

        # Check for any invalid value
        no_response = self.client.get(reverse_lazy('childartist_details',kwargs={'pk':10000}))

        # 202 for valid and 404 for invalid
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)

        # check for content of Detail Page
        self.assertContains(response, 'Body_Type')

        # Check for Correct template used in template/ChildArtists
        self.assertTemplateUsed(response, 'childartist/childartist_detail.html')

# # #-------------------------------------------------------------------------------------------#    


# #     # Test ChildArtist Create View
    


# # #---------------------------------------------------------------------------------------#


# #     # # Test ChildArtist Update view 

    def test_ChildArtistupdate_view(self):
        # Login the user
        self.client.login(username='testuser', password='test')
        
        # Find primary key of table
        ChildArtist_pk = ChildArtist.objects.get(ChildArtist_Body_Type='Body_Type').pk
        
        # Get response using pk on details view
        response = self.client.get(reverse_lazy('childartist_details',kwargs={'pk':ChildArtist_pk}), {
            'ChildArtist_Body_Type':'Body_Type',
'ChildArtist_Child_Artist_Id':'Child_Artist_Id',
'ChildArtist_Daily_Charges':'Daily_Charges',
'ChildArtist_Description':'Description',
'ChildArtist_Ethnicity':'Ethnicity',
'ChildArtist_Eye_Color':'Eye_Color',
'ChildArtist_Financial_Available':True,
'ChildArtist_Gender':'Gender',
'ChildArtist_Height':'Height',
'ChildArtist_Relation_With_Artist':'Relation_With_Artist',
'ChildArtist_Skin_Color':'Skin_Color',
'ChildArtist_Special_Skills':'Special_Skills',
'ChildArtist_Weight':'Weight',
        })
        # Ch
        # Check for successful response
        self.assertEqual(response.status_code, 200)
