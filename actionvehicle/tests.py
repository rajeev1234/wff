from django.test import TestCase,SimpleTestCase
from django.urls import reverse,reverse_lazy
from .models import ActionVehicle
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils import timezone



#  Test Class for actionvehicle Application

class actionvehicleTest(TestCase):

########################## Model Testing ############################
  

    # actionvehicle object with dummy data 
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password = 'test'
        )

        self.actionvehicle =  ActionVehicle.objects.create(# Fields according to defined in Model    
        ActionVehicle_Action_Vehicle_Id='actionvehicleid',
        ActionVehicle_Color='color',
        ActionVehicle_Company='company',
        ActionVehicle_Daily_Rent='dailyrent',
        ActionVehicle_Description ='description',
        ActionVehicle_Model='model',
        ActionVehicle_Modification= True,
        ActionVehicle_Monthly_Rent='monthly_rent',
        ActionVehicle_Ownership=True, # Defined above in get_user_model
        ActionVehicle_Registration_Number= 'registrationnumber',
        ActionVehicle_Rigging =  True,
        ActionVehicle_Weekly_Rent='weekly_rent',
        )

#
    #Check redirection URL
    def test_get_absolute_url(self):
        # Redirection goes to actionvehicle details
        self.assertEquals(self.actionvehicle.get_absolute_url(), '/actionvehicle/1')

# #-----------------------------------------------------------------------------------------#

#     # Check Conent of actionvehicle object
    def test_actionvehicle_content(self):
        self.assertEqual(str(self.actionvehicle.ActionVehicle_Action_Vehicle_Id),'actionvehicleid')
        self.assertEqual(str(self.actionvehicle.ActionVehicle_Color), 'color')
        self.assertEqual(str(self.actionvehicle.ActionVehicle_Company), 'company')
        self.assertEqual(str(self.actionvehicle.ActionVehicle_Daily_Rent), 'dailyrent')
        self.assertEqual(str(self.actionvehicle.ActionVehicle_Description), 'description')
        self.assertEqual(str(self.actionvehicle.ActionVehicle_Model), 'model')
        self.assertEqual(bool(str(self.actionvehicle.ActionVehicle_Modification)),True)
        self.assertEqual(str(self.actionvehicle.ActionVehicle_Monthly_Rent), 'monthly_rent')
        self.assertEqual(bool(str(self.actionvehicle.ActionVehicle_Ownership)),True)
        self.assertEqual(str(self.actionvehicle.ActionVehicle_Registration_Number),'registrationnumber')
        self.assertEqual(bool(str(self.actionvehicle.ActionVehicle_Rigging)),True) # Defined in SetUp
        self.assertEqual(str(self.actionvehicle.ActionVehicle_Weekly_Rent),'weekly_rent')
# #--------------------------------------------------------------------------------------------#

# # #############################   Model Test End   ###########################################







# ###############################    Views Test       ########################################

    
    # Test actionvehicle List View
    
    def test_actionvehicleList_view(self):
        # Get respomse from defined URL namespace
        response = self.client.get(reverse('actionvehicle_list'))
        self.assertEqual(response.status_code, 200)

        # Check Content of List View
        #self.assertContains(response,self.user.username)
        # Check for Correct template used in template/actionvehicles
        self.assertTemplateUsed(response, 'actionvehicle/actionvehicle_list.html')

#--------------------------------------------------------------------------------------------#
    

    # Test actionvehicle Detail View

    def test_actionvehicleDetail_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test')
        
        # Find primary key of table
        actionvehicle_pk = ActionVehicle.objects.get(ActionVehicle_Color='color').pk
        
        # Get response
        response = self.client.get(reverse_lazy('actionvehicle_details',kwargs={'pk':actionvehicle_pk}))

        # Check for any invalid value
        no_response = self.client.get(reverse_lazy('actionvehicle_details',kwargs={'pk':10000}))

        # 202 for valid and 404 for invalid
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)

        # check for content of Detail Page
        self.assertContains(response, 'color')

        # Check for Correct template used in template/actionvehicles
        self.assertTemplateUsed(response, 'actionvehicle/actionvehicle_detail.html')

# #-------------------------------------------------------------------------------------------#    


#     # Test actionvehicle Create View
    
    def test_actionvehicleCreate_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test') 

        # Generate response after creating an view using Http post method
        response = self.client.post('/actionvehicle/new/',{
        'ActionVehicle_Action_Vehicle_Id':'actionvehicleid',
        'ActionVehicle_Color':'color',
        'ActionVehicle_Company':'company',
        'ActionVehicle_Daily_Rent':'dailyrent',
        'ActionVehicle_Description ':'description',
        'ActionVehicle_Model':'model',
        'ActionVehicle_Modification':True,
        'ActionVehicle_Monthly_Rent':'monthly_rent',
        'ActionVehicle_Ownership':True, # Defined above in get_user_model
        'ActionVehicle_Registration_Number':'registrationnumber',
        'ActionVehicle_Rigging ':True,
        'ActionVehicle_Weekly_Rent':'weekly_rent',
        })

        # Check for successful response
        self.assertEqual(response.status_code, 200)

        # Check response values
        self.assertContains(response, 'actionvehicleid')
        self.assertContains(response, 'color')
        self.assertContains(response, 'company')
        self.assertContains(response, 'dailyrent')
        self.assertContains(response, 'description')
        self.assertContains(response, 'model')
        self.assertContains(response, 'checked')
        self.assertContains(response, 'monthly_rent')
        self.assertContains(response, 'checked')
        self.assertContains(response, 'registrationnumber')
        self.assertContains(response, 'checked')
        self.assertContains(response, 'weekly_rent')
         # Same as defined in SetUp
         # Same as defined in SetUp

        # Check for correct template used in template/actionvehicles
        self.assertTemplateUsed(response, 'actionvehicle/actionvehicle_new.html')

#---------------------------------------------------------------------------------------#


    # Test actionvehicle Update view 

    def test_actionvehicleupdate_view(self):
        # Login the user
        self.client.login(username='testuser', password='test')
        
        # Find primary key of table
        actionvehicle_pk = ActionVehicle.objects.get(ActionVehicle_Color='color').pk
        
        # Get response using pk on details view
        response = self.client.get(reverse_lazy('actionvehicle_details',kwargs={'pk':actionvehicle_pk}), {
        'ActionVehicle_Action_Vehicle_Id':'actionvehicleid',
        'ActionVehicle_Color':'color',
        'ActionVehicle_Company':'company',
        'ActionVehicle_Daily_Rent':'dailyrent',
        'ActionVehicle_Description ':'description',
        'ActionVehicle_Model':'model',
        'ActionVehicle_Modification':True,
        'ActionVehicle_Monthly_Rent':'monthly_rent',
        'ActionVehicle_Ownership':True, # Defined above in get_user_model
        'ActionVehicle_Registration_Number':'registrationnumber',
        'ActionVehicle_Rigging ':True,
        'ActionVehicle_Weekly_Rent':'weekly_rent',
        })
        # Check for successful response
        self.assertEqual(response.status_code, 200)
