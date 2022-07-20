from rest_framework import serializers
from .models import TsRecord

class TsRecordSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TsRecord
        fields = '__all__'