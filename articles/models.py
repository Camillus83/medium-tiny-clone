from django.db import models
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse
import uuid


User = get_user_model()


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Tag(models.Model):
    tag_name = models.CharField(max_length=50)

    def __str__(self):
        return self.tag_name


class Article(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    short_description = models.CharField(max_length=500)
    content = RichTextUploadingField(config_name="default")
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, blank=True)
    thumbnail = models.FileField(blank=True, null=True, default="default_thumbnail.png")

    class Meta:
        ordering = [
            "-date_posted",
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article_detail", args=[str(self.id)])


# class Article_Images(models.Model):
#     article = models.ForeignKey(Article, on_delete=models.CASCADE)
#     image = models.FileField(upload_to="static/images/")

#     def __str__(self):
#         return self.article.title


class Comment(models.Model):
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name="comments"
    )
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return self.content
