from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Author, Article, Tag, Article_Images, Comment


class HomePageView(TemplateView):
    template_name = "home.html"
