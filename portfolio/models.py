from django.db import models


class Image(models.Model):
    filename = models.CharField(max_length=255)
    thumbnail_filename = models.CharField(max_length=255)
    caption = models.CharField(max_length=255)  # This is where you add the caption field

    def __str__(self):
        return self.filename