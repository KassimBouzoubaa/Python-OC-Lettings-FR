from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("lettings/", include("lettings.urls")),
    path("profiles/", include("profiles.urls")),
    path("", views.index, name="index"),
]
