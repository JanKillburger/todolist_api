
from rest_framework import permissions, viewsets, serializers
from django.contrib.auth.models import User
from .models import Todo
from .serializers import TodoSerializer

# Create your views here.


class TodoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows todos to be viewed or edited.
    """
    queryset = Todo.objects.all().order_by('-created_at')
    serializer_class = TodoSerializer
    # permission_classes = [permissions.IsAuthenticated]