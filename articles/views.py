from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Author, Article, Tag, Comment


class HomePageView(ListView):
    model = Article
    template_name = "home.html"
    paginate_by = 5


class ArticleDetailView(DetailView):
    model = Article
    template_name = "detail.html"
