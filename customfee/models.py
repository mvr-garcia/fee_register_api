from django.db import models


class CustomFeeHistoric(models.Model):
    custom_fee_id = models.IntegerField(null=False)
    client_id = models.CharField(max_length=6, null=False)
    taker_fee = models.DecimalField(decimal_places=8, max_digits=8, null=False)
    maker_fee = models.DecimalField(decimal_places=8, max_digits=8, null=False)
    created_at = models.DateTimeField(null=False)
    expires_at = models.DateTimeField(null=False)
    staff_email = models.EmailField(null=False)
    register_type = models.CharField(max_length=10, null=False)
    observation = models.CharField(max_length=200, null=False)
