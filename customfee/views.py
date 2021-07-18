from datetime import datetime

from rest_framework.response import Response
from rest_framework.views import APIView

from customfee.historic import Historic
from customfee.models import CustomFeeHistoric
from customfee.serializers import CustomFeeSerializer


class CustomFeeCreate(APIView):

    def post(self, request, *args, **kwargs):

        Historic(request)._historic_register()

        return Response({
            "timestamp": datetime.now(),
            "response_data":"success"
        })


class CustomFeeListView(APIView):

    def get(self, request, *args, **kwargs):
    
        all = CustomFeeHistoric.objects.all()
        serializer = CustomFeeSerializer(all, many=True)

        return Response(serializer.data)
