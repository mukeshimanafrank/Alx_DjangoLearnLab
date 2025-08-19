from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, FeedView

# Create router and register viewsets
router = DefaultRouter()
router.register(r"posts", PostViewSet, basename="post")
router.register(r"comments", CommentViewSet, basename="comment")

urlpatterns = [
    # Include router URLs
    path("", include(router.urls)),

    # Feed endpoint
    path("feed/", FeedView.as_view(), name="feed"),
]
