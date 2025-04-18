from django.urls import path
from assets.views import AssetListView

urlpatterns=[
    path("", AssetListView.as_view(), name="home_assets"),
]