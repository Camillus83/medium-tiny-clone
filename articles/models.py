from django.db import models
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse
from django.template.defaultfilters import slugify
from taggit.managers import TaggableManager
from django_extensions.db.fields import AutoSlugField


User = get_user_model()


# class Tag(models.Model):
#     tag_name = models.CharField(max_length=50)
#     date_posted = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.tag_name

#     class Meta:
#         ordering = [
#             "-date_posted",
#         ]


class Article(models.Model):
    article_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=60)
    short_description = models.CharField(max_length=180)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    date_posted = models.DateTimeField(auto_now_add=True)
    tags = TaggableManager()
    content = RichTextUploadingField(config_name="default")
    thumbnail = models.FileField(blank=True, null=True, default="default_thumbnail.png")
    liked = models.ManyToManyField(User, default=None, blank=True, related_name='liked')
    favourite = models.ManyToManyField(User, default=None, blank=True, related_name='favourite')
    readlist = models.ManyToManyField(User, default=None, blank=True, related_name='readlist')
    slug = AutoSlugField(unique=True, populate_from='title')

    class Meta:
        ordering = [
            "-date_posted",
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article_detail", kwargs={'slug': self.slug, 'author': self.author.username,})
    
  


class Comment(models.Model):
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name="comments"
    )
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return self.content

class Note(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=60)
    content = models.TextField()
    note_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

    class Meta:
        ordering = [
            "-note_created",
        ]