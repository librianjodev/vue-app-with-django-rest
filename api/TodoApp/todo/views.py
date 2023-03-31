from django.shortcuts import render
from .models import WorkTodo
from .serializers import WorkSerializer

from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class WorkViewSet(viewsets.ModelViewSet):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = WorkTodo.objects.all()
    serializer_class = WorkSerializer