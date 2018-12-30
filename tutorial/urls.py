from django.contrib import admin
from django.urls import re_path, include, path
from snippets import views

urlpatterns = [
    path('', include('snippets.urls')),
    re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
