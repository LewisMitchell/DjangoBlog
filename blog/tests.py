from django.test import TestCase
from django.urls import reverse
from .models import Post
from bs4 import BeautifulSoup
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

    def test_layout_page(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        soup = BeautifulSoup(response.content, 'html.parser')
        self.assertEqual(soup.find(class_ = 'navbar-brand').contents[0], 'DjangoBlog')
        self.assertEqual(soup.find(class_ = 'nav-link').contents[0], 'Home')