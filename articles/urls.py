from django.urls import path
from .views import HomePageView, ArticleDetailView

urlpatterns = [
    path("", HomePageView.as_view(), name="homepage"),
    path("<uuid:pk>", ArticleDetailView.as_view(), name="article_detail"),
]
