from datetime import datetime

from rest_framework.response import Response
from rest_framework.views import APIView

from customfee.models import CustomFeeInfo
from customfee.serializers import CustomFeeSerializer


class CustomFeeCreate(APIView):

    def post(self, request, *args, **kwargs):

        expires_at = request.data.get("expires_at")
        expires_at = datetime.strptime(expires_at, '%d-%m-%Y')

        try:

            info = CustomFeeInfo(
                user_id=request.data.get("client"),
                taker_fee=request.data.get("taker"),
                maker_fee=request.data.get("maker"),
                expires_at=expires_at,
                staff_email=request.data.get("staff_email")
            )
            info.save()

        except:
            return Response({
                "timestamp": datetime.now(),
                "error":"user already exists"
            })

        return Response({
            "timestamp": datetime.now(),
            "response_data":"success"
        })


class CustomFeeListView(APIView):

    def get(self, request, *args, **kwargs):
    
        all = CustomFeeInfo.objects.all()
        serializer = CustomFeeSerializer(all, many=True)

        return Response(serializer.data)
