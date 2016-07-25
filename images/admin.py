from django.contrib import admin
<<<<<<< HEAD

# Register your models here.
=======
from .models import Image


#Registering the image model in the administrator site
class ImageAdmin(admin.ModelAdmin):
    list_display = [ 'title', 'slug', 'image', 'created' ]
    list_filter = [ 'created']

# Register your models here.
admin.site.register(Image, ImageAdmin)

>>>>>>> 8e3bbc298c7cf01864cb4331255237e751fe8a62
