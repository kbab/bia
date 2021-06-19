from django.db import models

# Create your models here.


class Image(models.Model):
    """Class containing unique info about images - in this case accession id"""

    accession_id = models.CharField(max_length=10, unique=True)

    class Meta:
        ordering = [
            "accession_id",
        ]

    def __str__(self):
        return f"AccessionID:{self.accession_id}"


class ImageMetadataDict(models.Model):
    """Intermediate class to allow flexible mapping of metadata to images"""

    key = models.CharField(max_length=100)
    description = models.CharField(max_length=255, null=True)

    def __str__(self):
        return ", ".join(
            [
                "Metadata Key:" + self.key,
                "Description:" + self.description,
            ]
        )


class ImageMetadata(models.Model):
    """Class representing metadata associated with images"""

    class Meta:
        unique_together = (("image", "metadata_key"),)
        ordering = [
            "image",
            "metadata_key",
        ]

    image = models.ForeignKey(
        Image, related_name="image_metadata", on_delete=models.CASCADE
    )
    metadata_key = models.ForeignKey(ImageMetadataDict, on_delete=models.CASCADE)
    metadata_value = models.CharField(max_length=255)

    def __str__(self):
        if self.metadata_key.key == "dimensions":
            return f"{self.metadata_key.key}: [{self.metadata_value}]"
        else:
            return f"{self.metadata_key.key}: {self.metadata_value}"
