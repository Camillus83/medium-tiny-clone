from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve
from django.contrib.auth.forms import AuthenticationForm
from accounts.forms import CustomUserCreationForm
from .views import SignUpPageView
from django.contrib.auth.views import LoginView


class CustomUserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username="testuser",
            first_name="test",
            last_name="user",
            email="testuser@email.com",
            password="testpass123",
        )
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.first_name, "test")
        self.assertEqual(user.last_name, "user")
        self.assertEqual(user.email, "testuser@email.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_user(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username="admin",
            first_name="article",
            last_name="admin",
            email="admin@email.com",
            password="testpass123",
        )
        self.assertEqual(admin_user.username, "admin")
        self.assertEqual(admin_user.first_name, "article")
        self.assertEqual(admin_user.last_name, "admin")
        self.assertEqual(admin_user.email, "admin@email.com")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)


class LoginPageTests(TestCase):
    def setUp(self):
        url = reverse("login")
        self.response = self.client.get(url)

    def test_login_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, "registration/login.html")

    def test_login_form(self):
        form = self.response.context.get("form")
        self.assertIsInstance(form, AuthenticationForm)
        self.assertTemplateUsed(self.response, "registration/login.html")

    def test_login_view(self):
        view = resolve("/accounts/login/")
        self.assertEqual(view.func.__name__, LoginView.as_view().__name__)


class SignUpPageTests(TestCase):
    def setUp(self):
        url = reverse("signup")
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, "registration/signup.html")

    def test_signup_form(self):
        form = self.response.context.get("form")
        self.assertIsInstance(form, CustomUserCreationForm)
        self.assertContains(self.response, "csrfmiddlewaretoken")

    def test_signup_view(self):
        view = resolve("/accounts/signup/")
        self.assertEqual(view.func.__name__, SignUpPageView.as_view().__name__)
