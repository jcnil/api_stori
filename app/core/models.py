from datetime import datetime

from mongoengine.fields import (
    EmailField,
    StringField,
    DictField,
    DateTimeField,
    ListField
)
from mongoengine import Document


class BaseDocument:
    """Document base to inherit all models

    Attributes:
        updated_at (datetime.datetime)
        created_at (datetime.datetime)
        deleted_at (datetime.datetime)
        deleted_by (DictField)
    """
    updated_at = DateTimeField(required=False)
    created_at = DateTimeField(default=lambda: datetime.now())
    deleted_at = DateTimeField(required=False)
    deleted_by = DictField(required=False)

    def update(self):
        self.updated_at = datetime.now()
        self.save()


class EmailModel(BaseDocument, Document):
    meta = {
        "collection": "emails",
        "indexes": ["email_customer"]
    }
    email_customer = EmailField(
        required=True
    )
    path = StringField(default="")
    filename = StringField(default="")
    account_balance = DictField(default={})
    historical = ListField(default=[])

    def to_json(self):

        return {
            "email_customer": self.email_customer,
            "path": self.path,
            "filename": self.filename,
            "account_balance": self.account_balance,
            "historical": [row.to_json() for row in self.historical]
        }
