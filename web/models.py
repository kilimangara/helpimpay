from django.db import models

class HelpImPayment(models.Model):
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField()
