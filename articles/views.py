from django.shortcuts import render
from django.views.generic import ListView
from .models import Article, Tag, Comment
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect


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
    if request.GET:
        comment_content = request.GET["comment-content"]
        comment = Comment.objects.create(
            article=article, author=request.user, content=comment_content
        )
        comment.save()
        return HttpResponseRedirect(reverse_lazy("article_detail", kwargs={"pk": pk}))

    return render(request, "detail.html", context)
