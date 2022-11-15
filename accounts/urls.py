from django.urls import path
from .views import SignUpPageView
from articles.views import add_to_favourite_view, like_article, add_to_readlist

urlpatterns = [
    path('readlist/<int:article_id>', add_to_readlist ,name='readlist_add'),
    path('like/<int:article_id>', like_article ,name='like_article'),
    path('fav/<int:article_id>', add_to_favourite_view ,name='favourite_add'),
    path("signup/", SignUpPageView.as_view(), name="signup"),
]
