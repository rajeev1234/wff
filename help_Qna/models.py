from django.db import models

from django.conf import settings

from django.urls import reverse

# Create your helpQna here.


class HelpQna(models.Model):
    Help_Qna_Answer = models.CharField(max_length=100)
    Help_Qna_Article_Id = models.IntegerField()
    #Hel_Qna_comment = models.ForeignKey(comments, related_name='helpqnas', on_delete=models.CASCADE)
    Help_Qna_Question = models.CharField(max_length=100)
    Help_Qna_Creator = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='helpqna', on_delete=models.CASCADE,null=True)
    Help_Qna_Modified_Date = models.DateField(auto_now_add=True)
    Help_Qna_Created_Date = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.Help_Qna_Article_Id

    def get_absolute_url(self):
        return reverse('helpQna_details', args=[str(self.id)])


# Create helpQnas Comments here.


class Comment(models.Model):
    Help_Qna_Comment = models.CharField(max_length=150, null=False)
    Comment_Help_Qna = models.ForeignKey(HelpQna, null=False, on_delete=models.CASCADE)
    Help_Qna_Comment_Author = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='commentqna', on_delete=models.CASCADE,null=True)

    # helpQna_Comment_Created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Help_Qna_Comment_Author

    def get_absolute_url(self):
        return reverse('helpQna_list')
