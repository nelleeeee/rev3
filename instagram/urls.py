from django.urls import include, path
from rest_framework import DefaultRouter
from . import views

router = DefaultRouter()
router.register("post", views.PostViewSet)
# router.urls <- url pattern list

urlpatterns = [
    path("", include(router.urls)),
]
