from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Alert
from .serializers import AlertSerializer
from .permissions import IsOwner

class AlertViewSet(viewsets.ModelViewSet):
    serializer_class = AlertSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        # Return only the alerts that belong to the authenticated user
        return Alert.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)