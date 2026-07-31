from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Alert(models.Model):
    CONDITION_CHOICES = [
        ('ABOVE', 'Price reaches or goes above target.'),
        ('BELOW', 'Price reaches or goes below target.'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='alerts')
    symbol = models.CharField(max_length=20)
    target_price = models.DecimalField(max_digits=12, decimal_places=4)
    condition = models.CharField(max_length=10, choices=CONDITION_CHOICES)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.symbol} {self.condition} {self.target_price} {self.user.username}"

    
    
