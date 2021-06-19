from rest_framework import serializers
from .models import (
    Image,
    ImageMetadata,
)


class ImageSerializer(serializers.ModelSerializer):
    """Serializer to return accession_ids of all images"""
    accession_id = serializers.CharField()

    class Meta:
        model = Image
        fields = ("accession_id",)

class MetadataValueSerializer(serializers.ModelSerializer):
    """Class for all metadata for a single image"""
    metadata_key = serializers.CharField(source="metadata_key.key", read_only=True)
    metadata_value = serializers.CharField()

    class Meta:
        model = ImageMetadata
        fields = (
            "metadata_key",
            "metadata_value",
        )


class ImageMetadataSerializer(serializers.ModelSerializer):
    """Wrapper class for image metadata - used to help with formatting"""
    accession_id = serializers.CharField()
    # Formats metadata for single image returned by MetadataValueSerializer
    metadata = serializers.SerializerMethodField("get_metadata_values")

    class Meta:
        model = Image
        fields = (
            "accession_id",
            "metadata",
        )

    def get_metadata_values(self, image):
        """Get metadata for single image as key value pairs"""
        metadata_values = ImageMetadata.objects.filter(image=image)
        return MetadataValueSerializer(metadata_values, many=True).data

    def get_bia_formatted_data(self):
        """Format the metadata to appear as in the interview spec"""
        bia_formatted_data = {"accession_id": self.data["accession_id"]}
        for m in self.data["metadata"]:
            key = m["metadata_key"]
            value = m["metadata_value"]
            if key == "dimensions":
                value = [int(v) for v in value.split(",")]
            elif key == "voxel_size_bytes":
                value = int(m["metadata_value"])

            bia_formatted_data[key] = value
        return bia_formatted_data
