from django.urls import path
from customfee.views import CustomFeeCreate, CustomFeeListView


urlpatterns = [
    path('create/', CustomFeeCreate.as_view(), name='create_customfee'),
    path('list/', CustomFeeListView.as_view(), name='list_customfee'),
]