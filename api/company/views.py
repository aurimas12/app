# from django.shortcuts import render
from rest_framework import generics
from api.company.models import Company
from api.company.serializers import CompanySerializer


class CompanyCreateView(generics.CreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

# class CompanyDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Company.objects.all()
#     serializer_class = CompanySerializer
