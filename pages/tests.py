from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Post

class PostCRUDTests(TestCase):

    def setUp(self):
        # Create test user
        self.user = User.objects.create_user(username='testuser', password='password')
        # Create a test post
        self.post = Post.objects.create(
            title='Test Title',
            author=self.user,
            text='Test Content'
        )

    def test_post_list_view(self):
        response = self.client.get(reverse('pages:posts'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Title')

    def test_post_detail_view(self):
        response = self.client.get(reverse('pages:post_detail', args=[self.post.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Content')

    def test_post_create_view(self):
        self.client.login(username='testuser', password='password')
        response = self.client.post(reverse('pages:post_new'), {
            'title': 'New Post',
            'author': self.user.id,
            'text': 'New Content'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Post.objects.filter(title='New Post').exists())

    def test_post_update_view(self):
        self.client.login(username='testuser', password='password')
        response = self.client.post(reverse('pages:post_edit', args=[self.post.pk]), {
            'title': 'edited Title',
            'author': self.user.id,
            'text': 'edited Content'
        })
        self.assertEqual(response.status_code, 302)
        self.post.refresh_from_db()
        self.assertEqual(self.post.title, 'edited Title')

    def test_post_delete_view(self):
        self.client.login(username='testuser', password='password')
        response = self.client.post(reverse('pages:post_delete', args=[self.post.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Post.objects.filter(pk=self.post.pk).exists())
