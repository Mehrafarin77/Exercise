from django.test import SimpleTestCase, TestCase
from django.urls import reverse
from . import models


# Create your tests here.
class PostTests(TestCase):
    @classmethod
    def setUpTestData(self):
        self.post = models.Post.objects.create(text='This is a test!')

    def test_model_content(self):
        self.assertEqual(self.post.text, 'This is a test!')

    def test_url_exists_at_correct_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_homepage(self):                    # combined tests
        response = self.client.get(reverse('pages:home'))
        self.assertEqual(response.status_code, 200)                 # response status code
        self.assertTemplateUsed(response, 'pages/home.html')        # template name
        self.assertContains(response, 'This is a test!')            # response contains


