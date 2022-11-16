from django.urls import path
from .views import article_detail_view, new_homepage_view, my_articles_view, ArticleCreateView, NoteListView, NoteCreateView
from articles.views import FavouriteListView

urlpatterns = [
    path('', new_homepage_view, name='homepage'),
    path('create-new-article/', ArticleCreateView.as_view(), name='create_article'),
    path('create-new-note/', NoteCreateView.as_view(), name='create_note'),
    path("@<str:author>/<slug:slug>", article_detail_view, name="article_detail"),
    path('my-articles', my_articles_view, name='my_articles'),
    path('my-notes', NoteListView.as_view(), name='my_notes'),
    path('my-favourites', FavouriteListView.as_view() ,name='my_favourites')
]
