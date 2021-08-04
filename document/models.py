import uuid
from django.contrib.auth.models import User
from django.db import models

try:
    from django.db.models import JSONField
except ImportError:
    from django.contrib.postgres.fields import JSONField

# For django-simple-history
from simple_history.models import HistoricalRecords


class Document(models.Model):
    # UUID of the document
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # name of the document
    title = models.CharField(max_length=128)

    # JSON value of the entire Abstract
    abstract_json = JSONField()

    # True if document is moved to archives
    is_archive = models.BooleanField(default=False)

    # True when document is moved to Trash
    in_trash = models.BooleanField(default=False)

    # creator of the document
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='document_created_by')

    # timestamp for when the document was created
    created_ts = models.DateTimeField(auto_now_add=True)

    # user who modifies the document
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='document_modified_by')

    # timestamp for when the document was last modified
    modified_ts = models.DateTimeField(auto_now=True)

    # For django-simple-history
    history = HistoricalRecords(
        history_id_field=models.UUIDField(default=uuid.uuid4)
    )

    def __str__(self):
        return self.title
