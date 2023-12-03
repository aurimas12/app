from rest_framework import serializers
from api.company.models import Company 


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'