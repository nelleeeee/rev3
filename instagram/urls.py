from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register("post", views.PostViewSet)
# router.urls <- url pattern list

urlpatterns = [
    path("public/", views.public_post_list),
    path("", include(router.urls)),
]
