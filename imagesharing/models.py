from django.db import models

# Create your models here.

class Image(models.Model):

    image = models.ImageField(upload_to="memes/")
    title = models.CharField(max_length = 100)
    slug = models.SlugField(unique = True, max_length = 80)
    
    add_timestamp = models.DateTimeField(auto_now = False, auto_now_add = True)

    class Meta:
        ordering = ['-add_timestamp']
