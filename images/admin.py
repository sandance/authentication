from django.contrib import admin
from .models import Image


#Registering the image model in the administrator site
class ImageAdmin(admin.ModelAdmin):
    list_display = [ 'title', 'slug', 'image', 'created' ]
    list_filter = [ 'created']

# Register your models here.
admin.site.register(Image, ImageAdmin)

