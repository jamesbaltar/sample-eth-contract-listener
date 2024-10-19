from django.db import models


class Transfer(models.Model):
    transaction_hash = models.CharField(max_length=255, unique=True)
    token_id = models.BigIntegerField(db_index=True)
    from_address = models.CharField(max_length=255)
    to_address = models.CharField(max_length=255)
    block_number = models.BigIntegerField()
