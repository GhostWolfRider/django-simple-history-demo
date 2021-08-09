import uuid
from django.contrib.auth.models import User
from django.db import models

# For django-simple-history
from simple_history.models import HistoricalRecords


# Create your models here.
class Profile(models.Model):
    """
    Extending the User model to create extra fields.
    """
    # UUID of profile
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # A user shall have only one profile and a profile shall represent only one user
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # User profile image
    image = models.CharField(max_length=1024, blank=True, null=True)

    # User Image Url from s3
    image_url = models.CharField(max_length=1024, blank=True, null=True)

    # User mobile number
    mobile_number = models.CharField(max_length=15, null=True, blank=True)

    # Soft delete a user
    is_deleted = models.BooleanField(default=False)

    # User can be created by Admin.
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile_created_by')

    # Timestamp for when the profile was created
    created_ts = models.DateTimeField(auto_now_add=True)

    # user who modifies the document
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile_modified_by')

    # Timestamp for when the profile was last modified
    modified_ts = models.DateTimeField(auto_now_add=True)

    # For django-simple-history
    history = HistoricalRecords(
        history_id_field=models.UUIDField(default=uuid.uuid4)
    )

    def __str__(self):
        return f'{self.user.first_name + " " + self.user.last_name}'
