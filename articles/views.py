from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView

from .models import Article, Comment, Tag
from .forms import ArticleForm


class HomePageView(ListView):
    model = Article
    template_name = "home.html"
    paginate_by = 5


class TagsListView(ListView):
    model = Tag
    template_name = "tags.html"
    paginate_by = 5


def article_detail_view(request, pk):
    context = {}
    article = Article.objects.get(pk=pk)
    context["article"] = article
    if request.POST:
        comment_content = request.POST["comment-content"]
        comment = Comment.objects.create(
            article=article, author=request.user, content=comment_content
        )
        comment.save()
        return HttpResponseRedirect(reverse_lazy("article_detail", kwargs={"pk": pk}))

    return render(request, "detail.html", context)

def new_homepage_view(request):
    context = {}
    articles = Article.objects.all()[:5]
    recent_tags = Tag.objects.all()[:5]
    context['articles'] = articles
    context['recent_tags'] = recent_tags
    return render(request, 'homepage.html', context)

@login_required
def my_articles_view(request):
    context = {}
    articles = Article.objects.filter(author=request.user)
    context['articles'] = articles
    return render(request, 'myarticles.html', context)
    
class ArticleCreateView(CreateView):
    form_class = ArticleForm
    model = Article
    template_name = 'create_article.html'

    def get_success_url(self):
        return reverse('homepage')