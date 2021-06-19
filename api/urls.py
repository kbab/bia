"""
API URL configuration
"""
from django.conf.urls import url
from django.urls import path, include
from . import views

urlpatterns = [
    path(
        "v1/images/",
        views.get_accession_ids,
        name="get_accession_ids",
    ),
    url(
        r"^v1/(?P<id>.+)/metadata/$",
        views.get_metadata,
        name="get_metadata",
    ),
    url(
        r"^v1/(?P<id>.+)/imagesize/$",
        views.get_imagesize,
        name="get_imagesize",
    ),
]
