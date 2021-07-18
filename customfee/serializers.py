from rest_framework import serializers
from customfee.models import CustomFeeHistoric


class CustomFeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomFeeHistoric
        fields = '__all__'
