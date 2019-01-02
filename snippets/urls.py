from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# First Step:
#############-Create an instance of the router
router = DefaultRouter()

#############-Register our viewsets with it
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

#Last Step:
#The API URLs are now determined automatically by the router
###########- include the router into the urlpattern list
urlpatterns = [
    path('', include(router.urls)),
]
