from .models import Transaction
from rest_framework import serializers

class TransactionSerializer(serializers.ModelSerializer):
    action_datetime = serializers.DateTimeField(format="%d/%m/%Y")

    class Meta:
        model = Transaction
        fields = "__all__"
