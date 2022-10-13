from django.contrib import admin
from .models import Author, Article, Tag, Comment


# class Article_ImagesInline(admin.TabularInline):
#     model = Article_Images
#     extra = 3


class ArticleAdmin(admin.ModelAdmin):
    # inlines = [Article_ImagesInline]
    list_display = ("title", "short_description", "author", "date_posted")
    filter_horizontal = ("tags",)


class CommentAdmin(admin.ModelAdmin):
    list_display = ("article", "author", "date_posted", "content")


admin.site.register(Author)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag)
admin.site.register(Comment, CommentAdmin)
