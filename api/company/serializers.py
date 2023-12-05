from rest_framework import serializers
from api.company.models import Company 


class CompanySerializer(serializers.ModelSerializer):
    city = serializers.CharField(source='get_city_display', read_only=True)
    class Meta:
        model = Company
        fields = '__all__'