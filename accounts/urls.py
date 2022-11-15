from django.urls import path
from .views import SignUpPageView
from articles.views import add_to_favourite_view

urlpatterns = [
    path('fav/<int:article_id>', add_to_favourite_view ,name='favourite_add'),
    path("signup/", SignUpPageView.as_view(), name="signup"),
]
