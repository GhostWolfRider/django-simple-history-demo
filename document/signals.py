from django.dispatch import receiver
from django.db.models.signals import post_save
from simple_history.signals import (
    pre_create_historical_record,
    post_create_historical_record
)
from .models import Document


@receiver(post_save, sender=Document)
def update_changes(sender, instance, **kwargs):
    all_history = instance.history.all()
    latest_history = all_history[:2]
    new_record, old_record = latest_history
    delta = new_record.diff_against(old_record)
    all_changes = {}
    for change in delta.changes:
        print("{} changed from {} to {}".format(change.field, change.old, change.new))
        all_changes.update({change.field: change.new})
    latest_change = latest_history[0]
    latest_change.field_changed = all_changes
    latest_change.save()


@receiver(pre_create_historical_record)
def pre_create_historical_record_callback(sender, **kwargs):
    print("Sent before saving historical record")


@receiver(post_create_historical_record)
def post_create_historical_record_callback(sender, **kwargs):
    print("Sent after saving historical record")