from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.api_root),
    path('snippets/', views.snippet_list.as_view(), name = 'snippet-list'),
    path('snippets/<int:pk>/', views.snippet_detail.as_view(), name = 'snippet-detail'),
    path('snippets/<int:pk>/highlight/', views.SnippetHighLight.as_view(), name = 'snippet-highlight'),
    path('users/', views.UserList.as_view(), name = 'user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name = 'user-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
