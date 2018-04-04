from django.test import TestCase,SimpleTestCase
from django.urls import reverse,reverse_lazy
from .models import Comments
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils import timezone



#  Test Class for Comments Application

class CommentsTest(TestCase):

########################## Model Testing ############################
  

    # Comments object with dummy data 
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password = 'test'
        )

        self.Comments =  Comments.objects.create(# Fields according to defined in Model    
        Comments_Comment='Comments_Comment',
Comments_Helpfull='Comments_Helpfull')

#
    #Check redirection URL
    def test_get_absolute_url(self):
        # Redirection goes to Comments details
        self.assertEquals(self.Comments.get_absolute_url(), '/comments/1')

# #-----------------------------------------------------------------------------------------#

#     # Check Conent of Comments object
    def test_Comments_content(self):
        self.assertEqual(str(self.Comments.Comments_Comment),'Comments_Comment')
        self.assertEqual(str(self.Comments.Comments_Helpfull), 'Comments_Helpfull')

# #--------------------------------------------------------------------------------------------#

# # #############################   Model Test End   ###########################################







# ###############################    Views Test       ########################################

    
    # Test Comments List View
    
    def test_CommentsList_view(self):
        # Get respomse from defined URL namespace
        response = self.client.get(reverse('comments_list'))
        self.assertEqual(response.status_code, 200)

        # Check Content of List View
        #self.assertContains(response,self.user.username)
        # Check for Correct template used in template/Commentss
        self.assertTemplateUsed(response, 'comments/comments_list.html')

#--------------------------------------------------------------------------------------------#
    

    # Test Comments Detail View

    def test_CommentsDetail_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test')
        
        # Find primary key of table
        Comments_pk = Comments.objects.get(Comments_Comment='Comments_Comment').pk
        
        # Get response
        response = self.client.get(reverse_lazy('comments_details',kwargs={'pk':Comments_pk}))

        # Check for any invalid value
        no_response = self.client.get(reverse_lazy('comments_details',kwargs={'pk':10000}))

        # 202 for valid and 404 for invalid
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)

        # check for content of Detail Page
        self.assertContains(response, 'Comments_Comment')
        self.assertContains(response, 'Comments_Helpfull')
        # Check for Correct template used in template/Commentss
        self.assertTemplateUsed(response, 'comments/comments_detail.html')

#-------------------------------------------------------------------------------------------#    


    # Test Comments Create View
    
    def test_CommentsCreate_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test') 

        # Generate response after creating an view using Http post method
        response = self.client.post('/comments/new/',{
        'Comments_Comment':'Comments_Comment',
        'Comments_Helpfull':'Comments_Helpfull',
        })

        # Check for successful response
        self.assertEqual(response.status_code, 200)

        # Check response values
        self.assertContains(response, 'Comments_Comment')
        self.assertContains(response, 'Comments_Helpfull')
         # Same as defined in SetUp
         # Same as defined in SetUp

        # Check for correct template used in template/Commentss
        self.assertTemplateUsed(response, 'comments/comments_new.html')

#---------------------------------------------------------------------------------------#


    # Test Comments Update view 

    def test_Commentsupdate_view(self):
        # Login the user
        self.client.login(username='testuser', password='test')
        
        # Find primary key of table
        Comments_pk = Comments.objects.get(Comments_Comment='Comments_Comment').pk
        
        # Get response using pk on details view
        response = self.client.get(reverse_lazy('comments_details',kwargs={'pk':Comments_pk}), {
'Comments_Comment':'Comments_Comment',
        'Comments_Helpfull':'Comments_Helpfull',
        })
        # Check for successful response
        self.assertEqual(response.status_code, 200)
