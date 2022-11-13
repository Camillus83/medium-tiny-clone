from django.urls import path
from .views import HomePageView, article_detail_view, TagsListView, new_homepage_view

urlpatterns = [
    path("", HomePageView.as_view(), name="homepage"),
    path("article/<uuid:pk>", article_detail_view, name="article_detail"),
    path("tags", TagsListView.as_view(), name="tags_page"),
    path('newhomepage/', new_homepage_view, name='newhomepage')
]
