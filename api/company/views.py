from django.shortcuts import render
from .models import Company
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import CompanySerializer


class CompanyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Company.objects.all().order_by('-date_joined')
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAuthenticated]

