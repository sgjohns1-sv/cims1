from django.urls import path

from . import views

urlpatterns=[
    path("", views.index, name="assets"),
    path("<int:asset_id>", views.view, name="view"),
    path("add/", views.add, name="add")
]