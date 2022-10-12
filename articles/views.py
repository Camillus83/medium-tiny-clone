from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Author, Article, Tag, Article_Images, Comment


class HomePageView(ListView):
    model = Article
    template_name = "home.html"
