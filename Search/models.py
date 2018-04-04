
from django.conf import settings

from django.urls import reverse

# Create your Searchs here.


from django.db import models

class Search(models.Model):
 #Search_CATEGORY= models.ForeignKey(List_Of_Comments, on_delete=models.CASCADE)
 Search_City = models.CharField(max_length=100)
 Search_Key_Word = models.CharField(max_length=200)
 #Search_Search_List= models.ForeignKey(List_Of_Search, on_delete=models.CASCADE)
 Search_Range = models.IntegerField(max_length=200)
 #Search_SUB_CATEGORY= models.ForeignKey(List_Of_Search_Sub_Catagorys, on_delete=models.CASCADE)
 Search_Creator = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='Search',on_delete=models.CASCADE,null=True)
 Search_Created_Date = models.DateTimeField(auto_now_add=True)
 Search_Modified_Date = models.DateTimeField(auto_now_add=True)




 def __str__(self):
        return self.Search_City

 def get_absolute_url(self):
        return reverse('search_details', args=[str(self.id)])


# Create Searchs Comments here.


class Comment(models.Model):

    Search_Comment = models.CharField(max_length=150, null=False)
    Comment_Search = models.ForeignKey(Search, null=False,related_name='commentSearch', on_delete=models.CASCADE)
    Search_Comment_Author = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='SearchcommentSearch', on_delete=models.CASCADE)

    # Search_Comment_Created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Search_Comment_Author

    def get_absolute_url(self):
        return reverse('search_list')
