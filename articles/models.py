from django.db import models
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

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
    title = models.CharField(max_length=200)
    short_description = models.CharField(max_length=500)
    content = RichTextUploadingField(config_name="default")
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, blank=True)
    thumbnail = models.FileField(blank=True, null=True)

    def __str__(self):
        return self.title


class Article_Images(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    image = models.FileField(upload_to="static/images/")

    def __str__(self):
        return self.article.title


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return self.content
