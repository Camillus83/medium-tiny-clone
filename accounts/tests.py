from django.test import TestCase
from django.contrib.auth import get_user_model


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
