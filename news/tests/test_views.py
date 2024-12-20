from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils.timezone import now
from news.models import Newspaper

User = get_user_model()


class LoginRequiredViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="testuser",
            password="secret"
        )
        self.newspaper = Newspaper.objects.create(
            title="Test Paper",
            content="Test content", published_date=now()
        )
        self.create_url = reverse("news:newspaper-create")
        self.list_url = reverse("news:newspaper-list")
        self.detail_url = reverse(
            "news:newspaper-detail",
            args=[self.newspaper.pk]
        )

    def login(self):
        self.client.login(username="testuser", password="secret")

    def assert_redirects_to_login(self, url):
        response = self.client.get(url)
        self.assertRedirects(response, f"{reverse('login')}?next={url}")

    def login_and_get(self, url):
        self.login()
        return self.client.get(url)

    def test_list_view_requires_login(self):
        # Without login
        self.assert_redirects_to_login(self.list_url)

        # After login
        response = self.login_and_get(self.list_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "news/newspaper_list.html")

    def test_detail_view_requires_login(self):
        self.assert_redirects_to_login(self.detail_url)

        response = self.login_and_get(self.detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "news/newspaper_detail.html")

    def test_create_view_requires_login(self):
        self.assert_redirects_to_login(self.create_url)

        response = self.login_and_get(self.create_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "news/newspaper_form.html")

        data = {
            "title": "New Title",
            "content": "New content",
            "published_date": "2024-12-19",
        }
        response = self.client.post(self.create_url, data=data)
        self.assertRedirects(response, reverse("news:newspaper-list"))
        self.assertTrue(Newspaper.objects.filter(title="New Title").exists())
