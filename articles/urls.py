from django.urls import path
from .views import HomePageView, article_detail_view, new_homepage_view, my_articles_view, ArticleCreateView

urlpatterns = [
    path('', new_homepage_view, name='homepage'),
    path('create-new-article/', ArticleCreateView.as_view(), name='create_article'),
    # path("article/<slug:slug>", article_detail_view, name="article_detail"),
    path("@<str:author>/<slug:slug>", article_detail_view, name="article_detail"),
    path('my_articles', my_articles_view, name='my_articles'),
    # path("tags", TagsListView.as_view(), name="tags_page"),
]
