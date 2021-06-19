from django.contrib import admin
from .models import Image, ImageMetadataDict, ImageMetadata

# Register your models here.
admin.site.register(Image)
admin.site.register(ImageMetadataDict)
admin.site.register(ImageMetadata)
