from django.shortcuts import render
from restapi.models import Todo
from restapi.serializers import TodoSerializer
from rest_framework.viewsets import ModelViewSet

# Create your views here.

class TodoViewSet(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
