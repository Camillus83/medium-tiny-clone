from django.db import models
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse
import uuid


User = get_user_model()


class Tag(models.Model):
    tag_name = models.CharField(max_length=50)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tag_name

    class Meta:
        ordering = [
            "-date_posted",
        ]


class Article(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    short_description = models.CharField(max_length=500)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, blank=True)
    content = RichTextUploadingField(config_name="default")
    thumbnail = models.FileField(blank=True, null=True, default="default_thumbnail.png")

    class Meta:
        ordering = [
            "-date_posted",
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article_detail", args=[str(self.id)])


class Comment(models.Model):
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name="comments"
    )
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return self.content
