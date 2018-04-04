from django.test import TestCase,SimpleTestCase
from django.urls import reverse,reverse_lazy
from .models import Booking
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils import timezone



#  Test Class for Booking Application

class BookingTest(TestCase):

########################## Model Testing ############################
  

    # Booking object with dummy data 
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password = 'test'
        )

        self.Booking =  Booking.objects.create(
        Booking_Status='Status',
        Booking_Modified_Date='Modified_Date',
		Booking_Created_Date='Created_Date',# Fields according to defined in Model    
        )
#
    #Check redirection URL
    def test_get_absolute_url(self):
        # Redirection goes to Booking details
        self.assertEquals(self.Booking.get_absolute_url(), '/booking/1')

# #-----------------------------------------------------------------------------------------#

#     # Check Conent of Booking object
    def test_Booking_content(self):
        self.assertEqual(str(self.Booking.Booking_Status),'Status')
        #self.assertEqual(str(self.Booking.Modified_Date), 'Modified_Date')
        #self.assertEqual(str(self.Booking.Created_Date), 'Created_Date')

       
# #--------------------------------------------------------------------------------------------#

# # #############################   Model Test End   ###########################################







# ###############################    Views Test       ########################################

    def test_BookingCreate_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test') 

    #     # Generate response after creating an view using Http post method
        response = self.client.post('/booking/new/',{
		'Booking_Status':'Status',
        })

    #     # Check for successful response
        self.assertEqual(response.status_code, 200)
    #     print(response)
        # Check response values
        self.assertContains(response, 'Status')
         # Same as defined in SetUp

        # Check for correct template used in template/Bookings
        self.assertTemplateUsed(response, 'booking/booking_new.html')
#     # Test Booking List View
    
    def test_BookingList_view(self):
        # Get respomse from defined URL namespace
        response = self.client.get(reverse('booking_list'))
        self.assertEqual(response.status_code, 200)

        # Check Content of List View
        #self.assertContains(response,self.user.username)
        # Check for Correct template used in template/Bookings
        self.assertTemplateUsed(response, 'booking/booking_list.html')

# # #--------------------------------------------------------------------------------------------#
    

# #     # Test Booking Detail View

    def test_BookingDetail_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test')
        
        # Find primary key of table
        Booking_pk = Booking.objects.get(Booking_Status='Status').pk
        
        # Get response
        response = self.client.get(reverse_lazy('booking_details',kwargs={'pk':Booking_pk}))

        # Check for any invalid value
        no_response = self.client.get(reverse_lazy('booking_details',kwargs={'pk':10000}))

        # 202 for valid and 404 for invalid
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)

        # check for content of Detail Page
        self.assertContains(response, 'Status')

        # Check for Correct template used in template/Bookings
        self.assertTemplateUsed(response, 'booking/booking_detail.html')

# # #-------------------------------------------------------------------------------------------#    


# #     # Test Booking Create View
    


# # #---------------------------------------------------------------------------------------#


# #     # # Test Booking Update view 

    def test_Bookingupdate_view(self):
        # Login the user
        self.client.login(username='testuser', password='test')
        
        # Find primary key of table
        Booking_pk = Booking.objects.get(Booking_Status='Status').pk
        
        # Get response using pk on details view
        response = self.client.get(reverse_lazy('booking_details',kwargs={'pk':Booking_pk}), {
        'Booking_Status':'Status',
        })
        # Check for successful response
        self.assertEqual(response.status_code, 200)
