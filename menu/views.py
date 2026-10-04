from rest_framework import generics
from .models import Category, CafeSettings
from .serializers import CategorySerializer, CafeSettingsSerializer


class MenuListView(generics.ListAPIView):
    queryset = Category.objects.filter(is_available=True).prefetch_related("items")
    serializer_class = CategorySerializer

class CafeSettingsView(generics.RetrieveAPIView):
    serializer_class = CafeSettingsSerializer

    def get_object(self):
        return CafeSettings.objects.get(pk=1)