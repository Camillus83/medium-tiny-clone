from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Article, Tag
from django.urls import reverse


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

        cls.tag_1 = Tag.objects.create(tag_name="FirstTag")

        cls.tag_2 = Tag.objects.create(tag_name="SecondTag")

        # cls.author = Author.objects.create(user=cls.user)

        cls.article = Article.objects.create(
            title="Dogs Article",
            short_description="Article about dogs",
            content="lorem ipsum lorem ipsum",
            author=cls.author,
            # tags=cls.tag_1,
        )

    def test_article_creation(self):
        self.assertEqual(f"{self.article.title}", "Dogs Article")
        self.assertEqual(f"{self.article.short_description}", "Article about dogs")
        self.assertEqual(f"{self.article.content}", "lorem ipsum lorem ipsum")
        self.assertEqual(self.article.author, self.author)
        # self.assertEqual(f"{self.article.tags.tag_name}", "FirstTag")

    def test_homepage_view(self):
        response = self.client.get(reverse("homepage"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("templates/login.html")

    def test_detail_view(self):
        pass
