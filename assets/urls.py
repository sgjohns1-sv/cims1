from django.urls import path
from assets.views import AssetAddView, AssetListView, AssetDetailView, AssetUpdateView, AssetDeleteView, AssetSearchView

urlpatterns=[
    path("", AssetListView.as_view(), name="asset_assets"),
    path("<int:pk>/", AssetDetailView.as_view(), name="asset_view"),
    path("add/", AssetAddView.as_view(), name="asset_add"),
    path("<int:pk>/update/", AssetUpdateView.as_view(), name="asset_update"),
    path("<int:pk>/delete/", AssetDeleteView.as_view(), name="asset_delete"),
    path("search/", AssetListView.as_view(), name="asset_search"),
]