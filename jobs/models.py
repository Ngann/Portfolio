from django.db import models

# Create your models here.
class Job(models.Model):
    # Images
    # property of image that of image type and path for the image to be saved in DB
    image = models.ImageField(upload_to='images/')
    # Summary and what is the max length got the images
    summary = models.CharField(max_length=200)

    def __str__(self):
        return self.summary