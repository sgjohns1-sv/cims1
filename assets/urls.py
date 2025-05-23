from django.urls import path
from assets.views import AssetAddView, AssetListView, AssetDetailView, AssetUpdateView, AssetDeleteView

#Url patterns used to direct requests from users to pages such as adding an asset, updating, an asset, and deleting an asset.
urlpatterns=[
    path("", AssetListView.as_view(), name="asset_assets"),
    path("<int:pk>/", AssetDetailView.as_view(), name="asset_view"),
    path("add/", AssetAddView.as_view(), name="asset_add"),
    path("<int:pk>/update/", AssetUpdateView.as_view(), name="asset_update"),
    path("<int:pk>/delete/", AssetDeleteView.as_view(), name="asset_delete"),
]