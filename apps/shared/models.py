from uuid import uuid4

from django.db import models


class FeaturedBaseModel(models.Model):
    """
    Base class to be used by other models
    """

    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
