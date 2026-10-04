from rest_framework import generics
from .models import Category
from .serializers import CategorySerializer


class MenuListView(generics.ListAPIView):
    queryset = Category.objects.filter(is_available=True).prefetch_related("items")
    serializer_class = CategorySerializer