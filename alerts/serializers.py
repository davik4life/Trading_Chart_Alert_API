from rest_framework import serializers
from .models import Alert

class AlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alert
        fields = ['id', 'user', 'symbol', 'target_price', 'condition', 'is_active', 'created_at']
        read_only_fields = ['id', 'user', 'created_at']

    def validate_target_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Target price must be greater than zero.")
        return value