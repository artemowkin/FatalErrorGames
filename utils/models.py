from uuid import uuid4

from django.db import models


class UUIDModel(models.Model):

    """Abstract model with uuid primary key field"""

    uuid = models.UUIDField(primary_key=True, editable=False, default=uuid4)

    class Meta:
        abstract = True

