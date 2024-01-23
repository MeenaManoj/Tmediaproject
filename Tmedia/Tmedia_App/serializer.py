
from rest_framework import serializers
from .models import Company_data

class CompanyDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company_data
        fields = ['id', 'company_name', 'company_location']
