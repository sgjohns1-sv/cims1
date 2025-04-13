from django.urls import path
from assets.views import AssetAddView, AssetListView, AssetDetailView, AssetUpdateView

from . import views

urlpatterns=[
    path("", AssetListView.as_view(), name="asset_assets"),
    path("<int:pk>/", AssetDetailView.as_view(), name="asset_view"),
    path("add/", AssetAddView.as_view(), name="asset_add"),
    path("update/<int:pk>/", AssetUpdateView.as_view(), name="asset_update")
]