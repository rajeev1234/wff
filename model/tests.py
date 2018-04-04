from django.test import TestCase,SimpleTestCase
from django.urls import reverse,reverse_lazy
from .models import Models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils import timezone


#  Test Class for Models Application

class ModelsTest(TestCase):

########################## Model Testing ############################


    # Models object with dummy data
    def setUp(self):

        # dummy user for login
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password = 'test'
        )

        self.Models =  Models.objects.create(

        # Fields according to defined in Model
        Models_Body_Type = 'Models_Body_Type',
        Models_Description='Models_Description',
        Models_Ethnicity='Models_Ethnicity',
        Models_Eye_Colour='Models_Eye_Colour',
        Models_Hair_Colour = 'Models_Hair_Colour',
        Models_Height = 'Models_Height',
        Models_Scene_Comfort = 'Models_Scene_Comfort',
        Models_Skin_Color = 'Models_Skin_Color',
        Models_Smoker = 'Models_Smoker',
        Models_Special_Skills = 'Models_Special_Skills',
        Models_Weight = 'Models_Weight',
        Models_Author = self.user,

        )

#-----------------------------------------------------------------------------------------#

    # Check redirection URL
    def test_get_absolute_url(self):
        # Redirection goes to Models details
        self.assertEquals(self.Models.get_absolute_url(), '/model/1')

#-----------------------------------------------------------------------------------------#

    # Check Conent of Models object created by create object query set
    def test_Models_content(self):
        # Verify for each field
        self.assertEqual(f'{self.Models.Models_Body_Type}', 'Models_Body_Type')
        self.assertEqual(f'{self.Models.Models_Description}', 'Models_Description')
        self.assertEqual(f'{self.Models.Models_Ethnicity}', 'Models_Ethnicity')
        self.assertEqual(f'{self.Models.Models_Eye_Colour}', 'Models_Eye_Colour')
        self.assertEqual(f'{self.Models.Models_Hair_Colour}', 'Models_Hair_Colour')
        self.assertEqual(f'{self.Models.Models_Height}', 'Models_Height')
        self.assertEqual(f'{self.Models.Models_Scene_Comfort}', 'Models_Scene_Comfort')
        self.assertEqual(f'{self.Models.Models_Skin_Color}', 'Models_Skin_Color')
        self.assertEqual(f'{self.Models.Models_Smoker}', 'Models_Smoker')
        self.assertEqual(f'{self.Models.Models_Special_Skills}', 'Models_Special_Skills')
        self.assertEqual(f'{self.Models.Models_Weight}', 'Models_Weight')
        self.assertEqual(f'{self.Models.Models_Author}', self.user.username)  # Defined in SetUp


#--------------------------------------------------------------------------------------------#

# #############################   Model Test End   ########################################### #


# ###############################    Views Test       ########################################


    # Test Models List View

    def test_ModelsList_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test')

        # Get response from defined URL namespace
        response = self.client.get(reverse('Model_list'))
        self.assertEqual(response.status_code, 200)

        # Check Content of List View
        self.assertContains(response, self.user.username)
        # Check for Correct template used in template/Modelss
        self.assertTemplateUsed(response, 'models/Model_list.html')

#--------------------------------------------------------------------------------------------#

    # Test Models Detail View

    def test_ModelsDetail_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test')

        # Find primary key of table
        Models_pk = Models.objects.get(Models_Body_Type = 'Models_Body_Type').pk

        # Get response
        response = self.client.get(reverse_lazy('Model_details',kwargs={'pk':Models_pk}))

        # Check for any invalid value
        no_response = self.client.get(reverse_lazy('Model_details',kwargs={'pk':10000}))

        # 202 for valid and 404 for invalid
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)

        # check for content of Detail Page
        self.assertContains(response, 'Models_Body_Type')

        # Check for Correct template used in template/Models
        self.assertTemplateUsed(response, 'models/Model_detail.html')

#-------------------------------------------------------------------------------------------#


    # Test EducationInfo Create View

    def test_ModelsCreate_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test')

        # Generate response after creating an view using Http post method
        response = self.client.post('/model/new/', {
        'Models_Body_Type' : 'Models_Body_Type',
        'Models_Description':'Models_Description',
        'Models_Ethnicity':'Models_Ethnicity',
        'Models_Eye_Colour':'Models_Eye_Colour',
        'Models_Hair_Colour' : 'Models_Hair_Colour',
        'Models_Height' : 'Models_Height',
        'Models_Scene_Comfort' : 'Models_Scene_Comfort',
        'Models_Skin_Color' : 'Models_Skin_Color',
        'Models_Smoker' : 'Models_Smoker',
        'Models_Special_Skills' : 'Models_Special_Skills',
        'Models_Weight' : 'Models_Weight',
        'Models_Author' : self.user,
        },follow = True)

        # print(response.content)
        # Check for successful response
        self.assertEqual(response.status_code, 200)
        # self.assertContains(response, False)
        self.assertContains(response, 'Models_Body_Type')
        self.assertContains(response, 'Models_Description')
        self.assertContains(response, 'Models_Ethnicity')
        self.assertContains(response, 'Models_Eye_Colour')
        self.assertContains(response, 'Models_Hair_Colour')
        self.assertContains(response, 'Models_Height')
        self.assertContains(response, 'Models_Skin_Color')
        self.assertContains(response, 'Models_Smoker')
        self.assertContains(response, 'Models_Special_Skills')
        self.assertContains(response, 'Models_Weight')
        self.assertContains(response, self.user.username)     # Same as defined in SetUp


        # Check for correct template used in template/EducationInfos
        self.assertTemplateUsed(response, 'models/Model_detail.html')

#---------------------------------------------------------------------------------------#


    # Test EducationInfo Update view

    def test_Modelsupdate_view(self):
        # Login the user
        self.client.login(username='testuser', password='test')

        # Find primary key of table
        Models_pk = Models.objects.get(Models_Body_Type='Models_Body_Type').pk

        # Get response using pk on details view
        response = self.client.get(reverse_lazy('Model_details',kwargs={'pk':Models_pk}), {
        'Models_Body_Type' : 'Models_Body_Type',
        'Models_Description':'Models_Description',
        'Models_Ethnicity':'Models_Ethnicity',
        'Models_Eye_Colour':'Models_Eye_Colour',
        'Models_Hair_Colour' : 'Models_Hair_Colour',
        'Models_Height' : 'Models_Height',
        'Models_Scene_Comfort' : 'Models_Scene_Comfort',
        'Models_Skin_Color' : 'Models_Skin_Color',
        'Models_Smoker' : 'Models_Smoker',
        'Models_Special_Skills' : 'Models_Special_Skills',
        'Models_Weight' : 'Models_Weight',
        'Models_Author' : self.user,
        },follow = True)

        # Check for successful response
        self.assertEqual(response.status_code, 200)

        # Check for correct templates
        self.assertTemplateUsed(response,'models/Model_detail.html')


#--------------------------------------------------------------------------------------------#


# Test Delete View of EducationInfo views

    def test_Modelsdelete_view(self):
        # Login the user
        self.client.login(username='testuser', password='test')

        # Find primary key of table
        Models_pk = Models.objects.get(Models_Body_Type='Models_Body_Type').pk

        # Get response to delete

        response = self.client.get(reverse_lazy('Model_delete',kwargs={'pk':Models_pk}))
        self.assertContains(response, 'Are you sure you want to delete') # THIS PART WORKS

        # Check deleted value , returns false i.e.302
        post_response = self.client.post(reverse_lazy('Model_delete',kwargs={'pk':Models_pk}))

        # self.assertRedirects(post_response, reverse_lazy('EducationInfo_delete',kwargs={'pk':EducationInfo_pk}), status_code=302)


        self.assertEqual(response.status_code, 200)

        # check for Correct Template Used
        self.assertTemplateUsed(response, 'models/Model_delete.html')




# ################################     View Testing End   #################################################


# ################################     Testing the URLs       ##############################################

class PagesTests(SimpleTestCase):

    # Check URL for list/ Home
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

# #-----------------------------------------------------------------------------------------------------#
