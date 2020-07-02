from shop.models import RentRecords
from .rent import RentSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class RentViewSet(viewsets.ModelViewSet):
    queryset = RentRecords.objects.all()
    serializer_class = RentSerializer
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)

    @action(methods=['get'], detail=True)
    def newest(self, request):
        newest = self.get_queryset() # .order_by('created').last()
        serializer = self.get_serializer_class()(newest)
        return Response(serializer.data)
