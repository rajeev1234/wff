from django.db import models

from django.conf import settings

from django.urls import reverse

# Create your helpsubcategorys here.


from django.db import models


from django.db import models
class images(models.Model):
    my_image = models.ImageField()
    owned_by = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)



    def __str__(self):
        return self.my_image

    def get_absolute_url(self):
        return reverse('images_details', args=[str(self.id)])


# Create helpsubcategorys Comments here.


class Comment(models.Model):

    image_Comment = models.CharField(max_length=150, null=False)
    # Comment_helpsubcategory = models.ForeignKey(images, null=False, on_delete=models.CASCADE)
    helpsubcategory_Comment_Author = models.ForeignKey(images,related_name='image', on_delete=models.CASCADE,null=True)

    # helpsubcategory_Comment_Created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image_Comment

    def get_absolute_url(self):
        return reverse('image_list')
