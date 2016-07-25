<<<<<<< HEAD
from __future__ import unicode_literals

from django.db import models

from django.conf import settings

# Create your models here.

class Image(models.Model):
=======
from django.db import models

# Create your models here.


from django.conf import settings
from django.utils.text import slugify

class Image(models.Model):
    """
    In this model we are going to store images bookmarked from different websites.
    user: User object that bookmarked this image , it is a one-to-many relationship
    title = A title for image
    slug = a short letter containing only letters, numbers , underscores or hypens
            to be used for beautiful SEO friendly websites
    url = The original URL for this image
    image = The image file
    description = An optional description for the image
    created = Datetime field that tells us when the object was created in the database
    """
>>>>>>> 8e3bbc298c7cf01864cb4331255237e751fe8a62
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='images_created')
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, blank=True)
    url = models.URLField()
<<<<<<< HEAD
    image = models.ImageField(upload_to='images/%Y/%m/%d')
    description = models.TextField(blank=True)
    created = models.DateField(auto_now_add=True, db_index=True)

=======

    image = models.ImageField(upload_to='images/%Y/%m/%d')
    description = models.TextField(blank=True)
    # we have created db_index=True so that Django creates an index in the database
    # for this field
    created = models.DateField(auto_now_add=True, db_index=True)

    users_like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='images_liked', blank=True)

    # Override the save() method of the Image model to automaticatically
    # generate the slug field based on the value of the title field

    def save(self, *args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            super(Image,self).save(*args, **kwargs)

>>>>>>> 8e3bbc298c7cf01864cb4331255237e751fe8a62
    def __str__(self):
        return self.title

