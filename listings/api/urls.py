from django.urls import include, path
from rest_framework.routers import SimpleRouter

from . import views

# TODO: Create your routers and urls here
router = SimpleRouter()
router.register(r'houses', views.HouseViewSet, basename='house')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework'))
]
