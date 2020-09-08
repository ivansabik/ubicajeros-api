import os
from datetime import datetime

from pynamodb.attributes import NumberAttribute, UnicodeAttribute, UTCDateTimeAttribute
from pynamodb.models import Model

dynamodb_host = os.getenv("DYNAMODB_HOST")


def create_tables_if_not_exist():
    if not Cajero.exists():
        Cajero.create_table(read_capacity_units=5, write_capacity_units=2, wait=True)


class Cajero(Model):
    class Meta:
        table_name = "ubicajeros_cajeros"
        host = dynamodb_host

    address = UnicodeAttribute()
    id = UnicodeAttribute(hash_key=True)
    lat = NumberAttribute(null=True)
    lon = NumberAttribute(null=True)
    open_hours = UnicodeAttribute(null=True)
    org_code = NumberAttribute(null=True)
    org_name = UnicodeAttribute(null=True)
    state = UnicodeAttribute(null=True)
    updated_at = UTCDateTimeAttribute(default=datetime.utcnow())
    zip_code = UnicodeAttribute(null=True)

    def to_dict(self):
        return self.__dict__["attribute_values"]
