from django.test import SimpleTestCase, TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from . import models


# Create your tests here.
class PostTests(TestCase):
    @classmethod
    def setUpTestData(self):
        self.user = get_user_model().objects.create_user(
        username="testuser", email="test@email.com", password="password"
        )
        self.post = models.Post.objects.create(
        title="A good title",
        text="Nice body content",
        author=self.user,
    )

    def test_post_model(self):
        self.assertEqual(self.post.title, "A good title")
        self.assertEqual(self.post.text, "Nice body content")
        self.assertEqual(self.post.author.username, "testuser")
        self.assertEqual(str(self.post), "A good title")
        self.assertEqual(self.post.get_absolute_url(), "/post/1/")

