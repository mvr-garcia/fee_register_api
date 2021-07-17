from rest_framework import serializers
from customfee.models import CustomFeeInfo


class CustomFeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomFeeInfo
        fields = '__all__'
