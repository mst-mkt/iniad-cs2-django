from django.contrib import admin
from django.urls import path

from blog import views as blog_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("blog/", blog_views.index),
]
