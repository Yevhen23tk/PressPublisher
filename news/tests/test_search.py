from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from news.models import Newspaper, Topic, Redactor

User = get_user_model()


class NewspaperSearchTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="secret"
        )
        self.client.login(username="testuser", password="secret")

        self.paper1 = Newspaper.objects.create(
            title="Breaking News", content="Some breaking news content."
        )
        self.paper2 = Newspaper.objects.create(
            title="Global Update", content="Global news content."
        )
        self.url = reverse("news:newspaper-list")

    def test_search_by_title(self):
        response = self.client.get(self.url, {"title": "Breaking"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.paper1, response.context["newspaper_list"])
        self.assertNotIn(self.paper2, response.context["newspaper_list"])

    def test_search_no_results(self):
        response = self.client.get(self.url, {"title": "NonExistent"})
        self.assertEqual(response.status_code, 200)
        self.assertQuerySetEqual(response.context["newspaper_list"], [])


class TopicSearchTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="secret"
        )
        self.client.login(username="testuser", password="secret")

        self.topic1 = Topic.objects.create(name="Technology")
        self.topic2 = Topic.objects.create(name="Health")
        self.url = reverse("news:topic-list")

    def test_search_by_topic_name(self):
        response = self.client.get(self.url, {"topic": "Tech"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.topic1, response.context["topic_list"])
        self.assertNotIn(self.topic2, response.context["topic_list"])

    def test_search_no_results(self):
        response = self.client.get(self.url, {"topic": "NonExistent"})
        self.assertEqual(response.status_code, 200)
        self.assertQuerySetEqual(response.context["topic_list"], [])


class RedactorSearchTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="secret"
        )
        self.client.login(
            username="testuser",
            password="secret"
        )

        self.redactor1 = Redactor.objects.create(
            username="jdoe",
            first_name="John",
            last_name="Doe",
            email="jdoe@example.com",
        )
        self.redactor2 = Redactor.objects.create(
            username="asmith",
            first_name="Alice",
            last_name="Smith",
            email="asmith@example.com",
        )
        self.url = reverse("news:redactor-list")

    def test_search_by_first_name(self):
        response = self.client.get(self.url, {"first_name": "John"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.redactor1, response.context["redactor_list"])
        self.assertNotIn(self.redactor2, response.context["redactor_list"])

    def test_search_by_last_name(self):
        response = self.client.get(self.url, {"first_name": "Smith"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.redactor2, response.context["redactor_list"])
        self.assertNotIn(self.redactor1, response.context["redactor_list"])

    def test_search_by_username(self):
        response = self.client.get(self.url, {"first_name": "jdoe"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.redactor1, response.context["redactor_list"])
        self.assertNotIn(self.redactor2, response.context["redactor_list"])

    def test_search_no_results(self):
        response = self.client.get(self.url, {"first_name": "NonExistent"})
        self.assertEqual(response.status_code, 200)
        self.assertQuerySetEqual(response.context["redactor_list"], [])
