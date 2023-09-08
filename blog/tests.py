from django.test import TestCase
from django.urls import reverse
from .models import Post
import datetime

# Create your tests here.
class UnitTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.post = Post.objects.create(
            title='A good title',
            body='Nice body content',
            created_at= "2023-09-08 13:18:19.000000",
        )

    def test_index_page(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'A good title')
        self.assertContains(response, 'Nice body content')
        self.assertTemplateUsed(response, "blog/index.html")