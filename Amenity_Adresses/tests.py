from django.test import TestCase,SimpleTestCase
from django.urls import reverse,reverse_lazy
from .models import Amenity_Adresses
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils import timezone



#  Test Class for Amenity_Adresses Application

class Amenity_AdressesTest(TestCase):

########################## Model Testing ############################
  

    # Amenity_Adresses object with dummy data 
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password = 'test'
        )

        self.Amenity_Adresses =  Amenity_Adresses.objects.create(
        Amenity_Adresses_Car_Parking='Car_Parking',
		Amenity_Adresses_Catering_Base='Catering_Base',
		Amenity_Adresses_Genset_Parking='Genset_Parking',
		Amenity_Adresses_Location_Id='Location_Id',
		Amenity_Adresses_Truck_Parking='Truck_Parking',
		Amenity_Adresses_Vanity_Parking='Vanity_Parking',# Fields according to defined in Model    
        )
#
    #Check redirection URL
    def test_get_absolute_url(self):
        # Redirection goes to Amenity_Adresses details
        self.assertEquals(self.Amenity_Adresses.get_absolute_url(), '/amenity_adresses/1')

# #-----------------------------------------------------------------------------------------#

#     # Check Conent of Amenity_Adresses object
    def test_Amenity_Adresses_content(self):
        self.assertEqual(str(self.Amenity_Adresses.Amenity_Adresses_Car_Parking),'Car_Parking')
        self.assertEqual(str(self.Amenity_Adresses.Amenity_Adresses_Catering_Base), 'Catering_Base')
        self.assertEqual(str(self.Amenity_Adresses.Amenity_Adresses_Genset_Parking), 'Genset_Parking')
        self.assertEqual(str(self.Amenity_Adresses.Amenity_Adresses_Location_Id), 'Location_Id')
        self.assertEqual(str(self.Amenity_Adresses.Amenity_Adresses_Truck_Parking),'Truck_Parking')
        self.assertEqual(str(self.Amenity_Adresses.Amenity_Adresses_Vanity_Parking), 'Vanity_Parking')
       
# #--------------------------------------------------------------------------------------------#

# # #############################   Model Test End   ###########################################







# ###############################    Views Test       ########################################

    def test_Amenity_AdressesCreate_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test') 

    #     # Generate response after creating an view using Http post method
        response = self.client.post('/amenity_adresses/new/',{
        'Amenity_Adresses_Car_Parking':'Car_Parking',
		'Amenity_Adresses_Catering_Base':'Catering_Base',
		'Amenity_Adresses_Genset_Parking':'Genset_Parking',
		'Amenity_Adresses_Location_Id':'Location_Id',
		'Amenity_Adresses_Truck_Parking':'Truck_Parking',
		'Amenity_Adresses_Vanity_Parking':'Vanity_Parking',
        })

    #     # Check for successful response
        self.assertEqual(response.status_code, 200)
    #     print(response)
        # Check response values
        self.assertContains(response, 'Car_Parking')
        self.assertContains(response, 'Catering_Base')
        self.assertContains(response, 'Genset_Parking')
        self.assertContains(response, 'Location_Id')
        self.assertContains(response, 'Truck_Parking')
        self.assertContains(response, 'Vanity_Parking')
         # Same as defined in SetUp
         # Same as defined in SetUp

        # Check for correct template used in template/Amenity_Adressess
        self.assertTemplateUsed(response, 'amenity_adresses/amenity_adresses_new.html')
    # Test Amenity_Adresses List View
    
    def test_Amenity_AdressesList_view(self):
        # Get respomse from defined URL namespace
        response = self.client.get(reverse('amenity_adresses_list'))
        self.assertEqual(response.status_code, 200)

        # Check Content of List View
        #self.assertContains(response,self.user.username)
        # Check for Correct template used in template/Amenity_Adressess
        self.assertTemplateUsed(response, 'amenity_adresses/amenity_adresses_list.html')

# #--------------------------------------------------------------------------------------------#
    

#     # Test Amenity_Adresses Detail View

    def test_Amenity_AdressesDetail_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test')
        
        # Find primary key of table
        Amenity_Adresses_pk = Amenity_Adresses.objects.get(Amenity_Adresses_Car_Parking='Car_Parking').pk
        
        # Get response
        response = self.client.get(reverse_lazy('amenity_adresses_details',kwargs={'pk':Amenity_Adresses_pk}))

        # Check for any invalid value
        no_response = self.client.get(reverse_lazy('amenity_adresses_details',kwargs={'pk':10000}))

        # 202 for valid and 404 for invalid
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)

        # check for content of Detail Page
        self.assertContains(response, 'Car_Parking')

        # Check for Correct template used in template/Amenity_Adressess
        self.assertTemplateUsed(response, 'amenity_adresses/amenity_adresses_detail.html')

# #-------------------------------------------------------------------------------------------#    


#     # Test Amenity_Adresses Create View
    


# #---------------------------------------------------------------------------------------#


#     # # Test Amenity_Adresses Update view 

    def test_Amenity_Adressesupdate_view(self):
        # Login the user
        self.client.login(username='testuser', password='test')
        
        # Find primary key of table
        Amenity_Adresses_pk = Amenity_Adresses.objects.get(Amenity_Adresses_Car_Parking='Car_Parking').pk
        
        # Get response using pk on details view
        response = self.client.get(reverse_lazy('amenity_adresses_details',kwargs={'pk':Amenity_Adresses_pk}), {
        'Amenity_Adresses_Car_Parking':'Car_Parking',
		'Amenity_Adresses_Catering_Base':'Catering_Base',
		'Amenity_Adresses_Genset_Parking':'Genset_Parking',
		'Amenity_Adresses_Location_Id':'Location_Id',
		'Amenity_Adresses_Truck_Parking':'Truck_Parking',
		'Amenity_Adresses_Vanity_Parking':'Vanity_Parking',
        })
        # Check for successful response
        self.assertEqual(response.status_code, 200)
