from django.db import models



from django.conf import settings

from django.urls import reverse

# Create your help_categorys here.

class Help_Category(models.Model):
    Help_Category_Name = models.CharField(max_length=100)
    Help_Category_Header_Id = models.IntegerField()
    #help_subcatagory =models.ForeignKey(helpsubcategory , related_name='helpsubcategorys', on_delete=models.CASCADE)
    Help_Category_Creator = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='helpcategorys',on_delete=models.CASCADE,null=True)
    Help_Category_Modified_Date = models.DateField(auto_now_add=True)
    Help_Category_Created_Date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.Help_Category_Name

    def get_absolute_url(self):
        return reverse('helpcategory_details', args=[str(self.id)])


# Create help_categorys Comments here.


class Comment(models.Model):

    Help_Category_Comment = models.CharField(max_length=150, null=False)
    Comment_Help_Category = models.ForeignKey(Help_Category, null=False, on_delete=models.CASCADE)
    Help_Category_Comment_Author = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='help_category_Comment_Author', on_delete=models.CASCADE,null=True)

    # help_category_Comment_Created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Help_Category_Comment

    def get_absolute_url(self):
        return reverse('helpcategory_list')
