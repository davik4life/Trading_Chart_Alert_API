import re
from rest_framework import serializers
from .models import Alert

class AlertSerializer(serializers.ModelSerializer):
    # Explicitly display the username instead of a raw ID number
    user = serializers.ReadOnlyField(source='user.username')
    
    # Remove validators here so they don't block lowercase inputs
    symbol = serializers.CharField(max_length=6)

    class Meta:
        model = Alert
        fields = ['id', 'user', 'symbol', 'target_price', 'condition', 'is_active', 'created_at']
        read_only_fields = ['id', 'created_at']
    # Handle uppercase conversion BEFORE running regex validation
    def validate_symbol(self, value):
        # Transform input immediately to uppercase
        clean_value = value.upper()
        
        # Run your specific forex/stock regex check manually
        ticker_pattern = re.compile(r'^([A-Z]{6}|[A-Z]{1,5})$')
        if not ticker_pattern.match(clean_value):
            raise serializers.ValidationError(
                "Symbol must be a valid Forex ticker (e.g., EURUSD) or Stock ticker (e.g., AAPL)."
            )
            
        # Return the clean, uppercase value to be saved safely
        return clean_value

    def validate_target_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Target price must be greater than zero.")
        return value
