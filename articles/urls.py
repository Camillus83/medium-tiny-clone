from django.urls import path
from .views import delete_article, article_detail_view, new_homepage_view, my_articles_view, ArticleCreateView, NoteListView, NoteCreateView
from articles.views import FavouriteListView, ReadlistListView, HomePageListView, ArticleEditView

urlpatterns = [
    # path('', new_homepage_view, name='homepage'),
    path('',  HomePageListView.as_view(), name='homepage'),
    path('create-new-article/', ArticleCreateView.as_view(), name='create_article'),
    path('create-new-note/', NoteCreateView.as_view(), name='create_note'),
    path("@<str:author>/<slug:slug>", article_detail_view, name="article_detail"),
    path('my-articles', my_articles_view, name='my_articles'),
    path('my-notes', NoteListView.as_view(), name='my_notes'),
    path('my-favourites', FavouriteListView.as_view() ,name='my_favourites'),
    path('my-readlist', ReadlistListView.as_view(), name='my_readlist'),
    path('delete/article/<int:article_id>', delete_article, name='delete_article'),
    path('edit/article/<slug:slug>', ArticleEditView.as_view(), name='edit_article'),

]
