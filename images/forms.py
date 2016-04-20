from django import forms
from .models import Image
from urllib import *
from django.core.files.base import ContentFile
from django.utils.text import slugify


class ImageCreateForm(forms.ModelForm):
    """
    ModelForm created from Image model including only title , url and description
    field
    """
    class Meta:
        model = Image
        fields = ('title', 'url', 'description')
        widgets = {
            'url': forms.HiddenInput,
        }

        def clean_url(self):
            """
            Django allows to define form methods to clean specific fields
            using the notation
            :return:
            """
            url = self.cleaned_data['url']
            valid_extensions = ['jpg','jpeg']
            extension = url.rsplit('.',1)[1].loswer()
            if extension not in valid_extensions:
                raise forms.ValidationError('The given URL does not match valid image extensions')
            return url

        def save(self, force_insert=False, force_update=False,commit=True):

            # we can new image instance by calling save method of the form with commit False
            image = super(ImageCreateForm,self).save(commit=False)
            # Get the url from the cleaned_data dictionary of the form
            image_url = self.cleaned_data['url']
            # Generate the image name by combining the image title slug with the original file
            image_name = '{}.{}'.format(slugify(image.title), image_url.rsplit('.',1)[1].lower())

            # download image from the given URL
            response = request.urlopen(image_url)
            image.image.save(image_name,ContentFile(response.read()), save=False)

            if commit:
                image.save()
            return image



