from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Article, Tag, Comment
from django.urls import reverse, resolve
from .views import HomePageView, TagsListView


class ArticleTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="TestUser",
            first_name="Test",
            last_name="User",
            email="testuser@email.com",
            password="testpass123",
        )
        cls.commenter = get_user_model().objects.create_user(
            username="Commentator",
            first_name="Comment",
            last_name="Maker",
            email="commentator@email.com",
            password="testpass123",
        )

        cls.tag_1 = Tag.objects.create(tag_name="FirstTag")
        cls.tag_2 = Tag.objects.create(tag_name="SecondTag")
        cls.tag_3 = Tag.objects.create(tag_name="ThirdTag")

        cls.article = Article.objects.create(
            title="Dogs Article",
            short_description="Article about dogs",
            content="lorem ipsum lorem ipsum",
            author=cls.user,
        )
        cls.article.save()
        cls.article.tags.add(cls.tag_1)
        cls.article.tags.add(cls.tag_2)
        cls.article.save()

    def test_article_creation(self):
        self.assertEqual(f"{self.article.title}", "Dogs Article")
        self.assertEqual(f"{self.article.short_description}", "Article about dogs")
        self.assertEqual(f"{self.article.content}", "lorem ipsum lorem ipsum")
        self.assertEqual(self.article.author, self.user)
        self.assertEqual(self.article.tags.all().count(), 2)
        self.assertEqual(self.article.tags.all()[1], self.tag_1)
        self.assertEqual(self.article.tags.all()[0], self.tag_2)

    def test_adding_comment(self):
        comment = Comment.objects.create(
            article=self.article,
            author=self.commenter,
            content="NICE ARTICLE",
        )
        self.assertEqual(comment.author, self.commenter)
        self.assertEqual(comment.article, self.article)
        self.assertEqual(f"{comment.content}", "NICE ARTICLE")


class HomePageTests(TestCase):
    def setUp(self):
        url = reverse("homepage")
        self.response = self.client.get(url)

    def test_homepage_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, "home.html")

    def test_homepage_view(self):
        view = resolve("/")
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)


class ArticleDetailTests(TestCase):
    def setUp(self):
        ArticleTest.setUpTestData()
        url = reverse("article_detail", args=[ArticleTest.article.pk])
        self.response = self.client.get(url)

    def test_detail_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed("templates/detail.html")


class TagsPageTests(TestCase):
    def setUp(self):
        url = reverse("tags_page")
        self.response = self.client.get(url)

    def test_tags_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed("tags.html")

    def test_tags_view(self):
        view = resolve("/tags")
        self.assertEqual(view.func.__name__, TagsListView.as_view().__name__)
