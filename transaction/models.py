from django.db import models

class Transaction(models.Model):
    type = models.CharField(max_length=6, choices=(('input',"INPUT"), ('output', "OUTPUT")))
    amount = models.IntegerField()
    note = models.CharField(max_length=100, null=True, blank=True)
    action_datetime = models.DateTimeField()
 
