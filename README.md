# django-simple-history Demo

### What are the benefits of using the django-simple-history?

- Querying history on a model instance.

- Querying history on a model class.

- Getting previous and next historical record.

- Reverting the Model.

- most_recent history.

- Save without a historical record.

- Filtering data and prefetching using a relationship to the model.

_________________________________________________________________________________

### What is django-simple-history Doing Behind the Scenes?

The table with historical prepended to document are a table created by django-simple-history. These tables store every change that you make to the document table. Every time a create, update, or delete occurs on Document a new row is created in the historical document table including all of the fields in the instance of the document model, as well as other metadata:

 
    history_user: the user that made the create/update/delete
    history_date: the DateTime at which the create/update/delete occurred
    history_change_reason: the reason the create/update/delete occurred (null by default)
    history_id: the primary key for the historical table (note the base table’s primary key is not unique on the historical table since there are multiple    versions of it on the historical table)
    history_type: + for create, ~ for update, and - for delete

#### Install:
```
pip install django-simple-history
```
#### settings.py:
```
INSTALLED_APPS = [...
                  'simple_history',
                  ...
                  ]

MIDDLEWARE = [...
              'simple_history.middleware.HistoryRequestMiddleware',
              ...
              ]
SIMPLE_HISTORY_HISTORY_ID_USE_UUID = True
```

#### models.py:
```
from simple_history.models import HistoricalRecords

class Document(models.Model):
    ...
    history = HistoricalRecords(
                  history_id_field=models.UUIDField(default=uuid.uuid4)
              )
```
By adding HistoricalRecords to a model or registering a model using the register, you automatically start tracking any create, update, or delete that occurs on that model.

#### Track History for a Third-Party Model:
```
from simple_history import register
from django.contrib.auth.models import User

register(User)
```

#### Run Migrations:
```
python manage.py makemigrations
python manage.py migrate
```

#### Existing Projects:
```
python manage.py populate_history --auto
```
It creates the document_historicaldocument table for the document model.

    document_document

    document_historicaldocument

__________________________________________________________________________________

### For more reference:
- Documentation https://django-simple-history.readthedocs.io/en/latest/
