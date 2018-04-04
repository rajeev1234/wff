from django.db import models

from django.conf import settings

from django.urls import reverse

# Create your portfolio_elements here.


class PortfolioElement(models.Model):
    PortfolioElement_Category = models.CharField(max_length=200)
    PortfolioElement_Director = models.CharField(max_length=200)
    PortfolioElement_Production_House = models.CharField(max_length=200)
    PortfolioElement_Title = models.CharField(max_length=200)

    # PortfolioElement_Audio = models.FileField(upload_to=u'mp3/', max_length=200)
    PortfolioElement_Creator = models.CharField(max_length=200)
    PortfolioElement_Image = models.ImageField(max_length=200)
    # PortfolioElement_Material_Tags = models.ForeignKey(List_Of_Tags, on_delete=models.CASCADE)
    # PortfolioElement_Performance_Video = models.FileField()

    # portfolio_element_Message = models.CharField(max_length=280)
    PortfolioElement_Author = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='portfolio_element', on_delete=models.CASCADE)
    PortfolioElement_Created_Date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.PortfolioElement_Category

    def get_absolute_url(self):
        return reverse('portfolio_element_details', args=[str(self.id)])


# Create portfolio_elements Comments here.


class Comment(models.Model):

    portfolio_element_Comment = models.CharField(max_length=150, null=False)
    # Comment_portfolio_element = models.ForeignKey(portfolio_element, null=False, on_delete=models.CASCADE)
    portfolio_element_Comment_Author = models.ForeignKey(PortfolioElement, on_delete=models.CASCADE)

    # portfolio_element_Comment_Created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.portfolio_element_Comment

    def get_absolute_url(self):
        return reverse('portfolio_element_list')
