from django.db import models

from django.conf import settings

from django.urls import reverse

# Create your Letter_pdfs here.


from django.db import models


from django.db import models

class Letter_pdf(models.Model):
    Letter_pdf_Addressing_Officer = models.CharField(max_length=100)
    Letter_pdf_Project = models.CharField(max_length=100)
    Letter_pdf_Creator = models.ForeignKey(settings.AUTH_USER_MODEL , related_name='letterpdfs', on_delete=models.CASCADE)
    Letter_pdf_Modified_Date = models.DateField(auto_now_add=True)
    Letter_pdf_Created_Date = models.DateField(auto_now_add=True)





    def __str__(self):
        return self.Letter_pdf_Project

    def get_absolute_url(self):
        return reverse('Letter_pdf_details', args=[str(self.id)])


# Create Letter_pdfs Comments here.


class Comment(models.Model):

    Letter_pdf_Comment = models.CharField(max_length=150, null=False)
    Comment_Letter_pdf = models.ForeignKey(Letter_pdf, null=False, on_delete=models.CASCADE)
    Letter_pdf_Comment_Author = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='commentletterpdf', on_delete=models.CASCADE)

    # Letter_pdf_Comment_Created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Letter_pdf_Comment

    def get_absolute_url(self):
        return reverse('Letter_pdf_list')
