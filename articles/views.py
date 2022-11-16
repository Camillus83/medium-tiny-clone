from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Article, Comment, Note
from .forms import ArticleForm, NoteForm


class NoteListView(ListView, LoginRequiredMixin):
    model = Note
    template_name = 'notelist.html'
    paginate_by = 5
    login_url = "account_login"
    context_object_name = 'notes'
    
    def get_queryset(self):
        user = self.request.user
        queryset = Note.objects.filter(author=user)
        return queryset

class FavouriteListView(ListView, LoginRequiredMixin):
    model = Article
    template_name = 'favourite_list.html'
    paginate_by = 5
    login_url = "account_login"
    context_object_name = 'articles'
    
    def get_queryset(self):
        user = self.request.user
        queryset = Article.objects.filter(favourite=user)
        return queryset


def article_detail_view(request, slug, author):
    context = {}
    article = Article.objects.get(slug=slug)
    context["article"] = article
    if request.POST:
        comment_content = request.POST["comment-content"]
        comment = Comment.objects.create(
            article=article, author=request.user, content=comment_content
        )
        comment.save()
        return HttpResponseRedirect(reverse_lazy("article_detail", kwargs={"slug": slug, "author":request.user.username}))

    return render(request, "detail.html", context)

def new_homepage_view(request):
    context = {}
   
    articles = Article.objects.all()[:5]
    # recent_tags = Tag.objects.all()[:5]
    context['articles'] = articles
    # context['recent_tags'] = recent_tags

    return render(request, 'homepage.html', context)

@login_required
def my_articles_view(request):
    context = {}
    articles = Article.objects.filter(author=request.user)
    context['articles'] = articles
    return render(request, 'myarticles.html', context)
    
class ArticleCreateView(CreateView, LoginRequiredMixin):
    form_class = ArticleForm
    model = Article
    template_name = 'create_article.html'
    login_url = "account_login"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        form.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('homepage')

class NoteCreateView(CreateView, LoginRequiredMixin):
    form_class = NoteForm
    model = Note
    template_name = 'create_note.html'
    login_url = "account_login"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        form.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('homepage')

@login_required
def add_to_favourite_view(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    if article.favourite.filter(pk=request.user.id).exists():
        article.favourite.remove(request.user)
    else:
        article.favourite.add(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

@login_required
def like_article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    if article.liked.filter(pk=request.user.id).exists():
        article.liked.remove(request.user)
    else:
        article.liked.add(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

@login_required
def add_to_readlist(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    if article.readlist.filter(pk=request.user.id).exists():
        article.readlist.remove(request.user)
    else:
        article.readlist.add(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])