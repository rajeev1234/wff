from django.db import models

from django.conf import settings

from django.urls import reverse

# Create your helpsubcategorys here.
from django.db import models



class HelpSubCategory(models.Model):
   # qna_list =models.ForeignKey(qna_lists, related_name='helpsubcategory', on_delete=models.CASCADE)
   Help_SubCategory_Name = models.CharField(max_length=100)
   Help_SubCategory_Topic_Id = models.CharField(max_length=100)
   Help_SubCategory_Creator = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='helpsubcategorys', on_delete=models.CASCADE,null=True)
   Help_SubCategory_Modified_Date = models.DateField(auto_now_add=True)
   Help_SubCategory_Created_Date = models.DateField(auto_now_add=True)



   def __str__(self):
      return self.Help_SubCategory_Name

   def get_absolute_url(self):
        return reverse('helpsubcategory_details', args=[str(self.id)])


# Create helpsubcategorys Comments here.


class Comment(models.Model):
    Help_SubCategory_Comment = models.CharField(max_length=150, null=False)
    Comment_Help_SubCategory = models.ForeignKey(HelpSubCategory, null=False, on_delete=models.CASCADE)
    Help_SubCategory_Comment_Author = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='commenthelpsubcategorys', on_delete=models.CASCADE,null=True)

    # helpsubcategory_Comment_Created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Help_SubCategory_Comment_Author

    def get_absolute_url(self):
        return reverse('helpsubcategory_list')
