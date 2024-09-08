from rest_framework import generics
from rest_framework import throttling
from django.core.cache import cache
from .models import VehicleData
from .dto import VehicleDataSerializer
class VehicleDataListView(generics.ListCreateAPIView):
    queryset = VehicleData.objects.all()
    serializer_class = VehicleDataSerializer
    throttle_classes = [throttling.UserRateThrottle]
    def get_queryset(self):
        vehicles = cache.get('vehicle_data_list')
        if not vehicles:
            vehicles = super().get_queryset()
            cache.set('vehicle_data_list', vehicles, timeout=60*15)
        return vehicles
    class VehicleDataDetailView(generics.RetrieveAPIView):
        queryset = VehicleData.objects.all()
        serializer_class = VehicleDataSerializer

# class VehicleDataListView(generics.ListAPIView):
#     queryset = VehicleData.objects.all()
#     serializer_class = VehicleDataSerializer
#     throttle_classes = [throttling.UserRateThrottle]
#     def get_queryset(self):
#         vehicles = cache.get('vehicle_data_list')
#         if not vehicles:
#             vehicles = super().get_queryset()
#         cache.set('vehicle_data_list', vehicles, timeout=60*15)
#         return vehicles

class VehicleDataDetailView(generics.RetrieveAPIView):
    queryset = VehicleData.objects.all()
    serializer_class = VehicleDataSerializer
    throttle_classes = [throttling.UserRateThrottle]