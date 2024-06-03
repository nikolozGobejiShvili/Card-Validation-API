from rest_framework import viewsets
from .models import Card
from .serializers import CardSerializer
from rest_framework.permissions import IsAuthenticated

class CardViewSet(viewsets.ModelViewSet):
    serializer_class = CardSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Card.objects.filter(user=self.request.user).order_by('created_at')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user) 

