from django.db import models


class CustomFeeInfo(models.Model):
    user_id = models.CharField(unique=True, max_length=6, null=False)
    taker_fee = models.DecimalField(decimal_places=8, max_digits=8, null=False)
    maker_fee = models.DecimalField(decimal_places=8, max_digits=8, null=False)
    expires_at = models.DateTimeField(null=False)
    staff_email = models.EmailField(null=False)
