from django.urls import path
from .views import CafeSettingsView, MenuListView

urlpatterns = [
    path("menu/", MenuListView.as_view(), name="menu-list"),
    path("settings/", CafeSettingsView.as_view(), name="cafe-settings"),
]