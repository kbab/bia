import json
from operator import mul
from functools import reduce

from django.shortcuts import render, get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Image, ImageMetadata, ImageMetadataDict
from .serializers import ImageSerializer, ImageMetadataSerializer

# Create your views here.

@api_view(
    [
        "GET",
    ]
)
def get_accession_ids(request):
    """Get accession IDs of all images"""

    images = Image.objects.all()
    serializer = ImageSerializer(images, many=True)
    return Response(serializer.data)

@api_view(
    [
        "GET",
    ]
)
def get_metadata(request, id):
    """Get metadata associated with image having specified accession_id"""
    image = get_object_or_404(Image, accession_id=id)
    serializer = ImageMetadataSerializer(image)
    return Response(serializer.get_bia_formatted_data())

@api_view(
    [
        "GET",
    ]
)
def get_imagesize(request, id):
    """Get size of specified image in bytes"""

    image = get_object_or_404(Image, accession_id=id)
    voxel_size_bytes_key = get_object_or_404(ImageMetadataDict, key="voxel_size_bytes")
    dimensions_key = get_object_or_404(ImageMetadataDict, key="dimensions")
    voxel_size_bytes = int(
        ImageMetadata.objects.filter(image=image, metadata_key=voxel_size_bytes_key)[
            0
        ].metadata_value
    )
    dimensions = ImageMetadata.objects.filter(image=image, metadata_key=dimensions_key)[
        0
    ].metadata_value
    dimensions = [int(d) for d in dimensions.split(",")]
    imagesize = reduce(mul, dimensions) * voxel_size_bytes

    return Response({
        "accession_id": image.accession_id, 
        "imagesize": imagesize
        }
    )
