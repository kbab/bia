from django.test import TestCase, Client
from django.urls import reverse

from rest_framework import status

from .models import(
    Image,
    ImageMetadataDict,
    ImageMetadata,
)

# Test functionality associated with REST API

class GetAllDataTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create Image a test image with associated metadata
        Image.objects.create(accession_id="BIA-99")
        image = Image.objects.create(accession_id="BIA-00")
        
        author_key = ImageMetadataDict.objects.create(key="author")
        species_key = ImageMetadataDict.objects.create(key="species")
        tissue_key = ImageMetadataDict.objects.create(key="tissue")
        vsb_key = ImageMetadataDict.objects.create(key="voxel_size_bytes")
        dims_key = ImageMetadataDict.objects.create(key="dimensions")

        ImageMetadata.objects.create(image=image, metadata_key=author_key, metadata_value="test author")
        ImageMetadata.objects.create(image=image, metadata_key=species_key, metadata_value="test species")
        ImageMetadata.objects.create(image=image, metadata_key=tissue_key, metadata_value="test tissue")
        ImageMetadata.objects.create(image=image, metadata_key=vsb_key, metadata_value="16")
        ImageMetadata.objects.create(image=image, metadata_key=dims_key, metadata_value="2,3,4,5,6")

    def _get_expected_accession_id_results(self):
        """Return results expected for '/images' api call"""

        return [
            {
                "accession_id": "BIA-00"
            },
            {
                "accession_id": "BIA-99"
            },
        ]

    def _get_expected_metadata_results(self):
       """Return results expected for '/accessions/<accession_id>/metadata' api call"""        
       return {
            "accession_id": "BIA-00",
            "author": "test author",
            "species": "test species",
            "tissue": "test tissue",
            "voxel_size_bytes": 16,
            "dimensions": [2,3,4,5,6]
        }

    def _get_expected_imagesize_results(self):
        """Return results expected for '/accessions/<accession_id>/imagesize' api call"""
        return {
            "accession_id": "BIA-00",
            "imagesize": 11520,
        }

    def test_get_images(self):
        """Test the '/images' api call"""
        response = self.client.get(reverse("get_accession_ids"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, self._get_expected_accession_id_results())

    def test_get_metadata(self):
        """Test the '/<accession_id>/metadata' api call"""
        response = self.client.get(reverse("get_metadata", kwargs={"id":"BIA-00"}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, self._get_expected_metadata_results())

    def test_get_imagesize(self):
        """Test the '/<accession_id>/imagesize' api call"""
        response = self.client.get(reverse("get_imagesize", kwargs={"id":"BIA-00"}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, self._get_expected_imagesize_results())

