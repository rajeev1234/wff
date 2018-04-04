from django.test import TestCase,SimpleTestCase
from django.urls import reverse,reverse_lazy
from .models import Actors
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils import timezone



#  Test Class for actors Application

class ActorsTest(TestCase):

########################## Model Testing ############################
  

    # actors object with dummy data 
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password = 'test'
        )

        self.actors =  Actors.objects.create(# Fields according to defined in Model    
        Actor_Id='actorid',
        Actor_Body_Type='bodytype',
        Actor_Description='description',
        Actor_Ethnicity='ethnicity',
        Actor_Eye_Color ='eyecolor',
        Actor_Favorite_Acting_Styles='favorite_acting_styles',
        Actor_Height= 'height',
        Actor_Rates='rates',
        Actor_SceneComfort='scenecomfort', # Defined above in get_user_model
        Actor_Skin_Color= 'skincolor',
        Actor_Smoker =  True,
        Actor_Weight='weight',
        )
#
    #Check redirection URL
    def test_get_absolute_url(self):
        # Redirection goes to actors details
        self.assertEquals(self.actors.get_absolute_url(), '/actors/1')

# #-----------------------------------------------------------------------------------------#

# #     # Check Conent of actors object
    def test_actors_content(self):
        self.assertEqual(str(self.actors.Actor_Id),'actorid')
        self.assertEqual(str(self.actors.Actor_Body_Type), 'bodytype')
        self.assertEqual(str(self.actors.Actor_Description), 'description')
        self.assertEqual(str(self.actors.Actor_Ethnicity), 'ethnicity')
        self.assertEqual(str(self.actors.Actor_Eye_Color),'eyecolor')
        self.assertEqual(str(self.actors.Actor_Favorite_Acting_Styles), 'favorite_acting_styles')
        self.assertEqual(str(self.actors.Actor_Height),'height')
        self.assertEqual(str(self.actors.Actor_Rates),'rates')
        self.assertEqual(str(self.actors.Actor_SceneComfort),'scenecomfort') # Defined in SetUp
        self.assertEqual(str(self.actors.Actor_Skin_Color),'skincolor')
        self.assertEqual(bool(str(self.actors.Actor_Smoker)),True)
        self.assertEqual(str(self.actors.Actor_Weight),'weight')
# #--------------------------------------------------------------------------------------------#

# # #############################   Model Test End   ###########################################







# ###############################    Views Test       ########################################

    def test_actorsCreate_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test') 

    #     # Generate response after creating an view using Http post method
        response = self.client.post('/actors/new/',{
        'Actor_Id':'actorid',
        'Actor_Body_Type':'bodytype',
        'Actor_Description':'description',
        'Actor_Ethnicity':'ethnicity',
        'Actor_Eye_Color ':'eyecolor',
        'Actor_Favorite_Acting_Styles':'favorite_acting_styles',
        'Actor_Height':'height',
        'Actor_Rates':'rates',
        'Actor_SceneComfort':'scenecomfort', # Defined above in get_user_model
        'Actor_Skin_Color': 'skincolor',
        'Actor_Smoker ': True,
        'Actor_Weight':'weight',
        })

    #     # Check for successful response
        self.assertEqual(response.status_code, 200)
    #     print(response)
        # Check response values
        self.assertContains(response, 'actorid')
        self.assertContains(response, 'bodytype')
        self.assertContains(response, 'description')
        self.assertContains(response, 'ethnicity')
        self.assertContains(response, 'eyecolor')
        self.assertContains(response, 'favorite_acting_styles')
        self.assertContains(response, 'height')
        self.assertContains(response, 'rates')
        self.assertContains(response, 'scenecomfort')
        self.assertContains(response, 'skincolor')
        self.assertContains(response, 'checked')
        self.assertContains(response, 'weight')
         # Same as defined in SetUp
         # Same as defined in SetUp

        # Check for correct template used in template/actorss
        self.assertTemplateUsed(response, 'actors/actors_new.html')
    #Test actors List View
    
    def test_actorsList_view(self):
        # Get respomse from defined URL namespace
        response = self.client.get(reverse('actors_list'))
        self.assertEqual(response.status_code, 200)

        # Check Content of List View
        #self.assertContains(response,self.user.username)
        # Check for Correct template used in template/actorss
        self.assertTemplateUsed(response, 'actors/actors_list.html')

# # #--------------------------------------------------------------------------------------------#
    

# #     # Test actors Detail View

    def test_actorsDetail_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test')
        
        # Find primary key of table
        actors_pk = Actors.objects.get(Actor_Id='actorid').pk
        
        # Get response
        response = self.client.get(reverse_lazy('actors_details',kwargs={'pk':actors_pk}))

        # Check for any invalid value
        no_response = self.client.get(reverse_lazy('actors_details',kwargs={'pk':10000}))

        # 202 for valid and 404 for invalid
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)

        # check for content of Detail Page
        self.assertContains(response, 'actorid')

        # Check for Correct template used in template/actorss
        self.assertTemplateUsed(response, 'actors/actors_detail.html')

# #-------------------------------------------------------------------------------------------#    


#     # Test actors Create View
    


# #---------------------------------------------------------------------------------------#


#     # # Test actors Update view 

    def test_actorsupdate_view(self):
        # Login the user
        self.client.login(username='testuser', password='test')
        
        # Find primary key of table
        actors_pk = Actors.objects.get(Actor_Id='actorid').pk
        
        # Get response using pk on details view
        response = self.client.get(reverse_lazy('actors_details',kwargs={'pk':actors_pk}), {
        'Actor_Id':'actorid',
        'Actor_Body_Type':'bodytype',
        'Actor_Description':'description',
        'Actor_Ethnicity':'ethnicity',
        'Actor_Eye_Color ':'eyecolor',
        'Actor_Favorite_Acting_Styles':'favorite_acting_styles',
        'Actor_Height=':'height',
        'Actor_Rates':'rates',
        'Actor_SceneComfort':'scenecomfort', # Defined above in get_user_model
        'Actor_Skin_Color': 'skincolor',
        'Actor_Smoker ': True,
        'Actor_Weight':'weight',
        })
        # Check for successful response
        self.assertEqual(response.status_code, 200)
