from django.test import TestCase
from news.models import Newspaper, Topic, Redactor
from news.forms import (
    NewspaperCreationForm,
    NewspaperUpdateForm,
    NewspaperSearchForm,
    TopicCreateForm,
    TopicUpdateForm,
    TopicSearchForm,
    RedactorCreateForm,
    RedactorUpdateForm,
    RedactorSearchForm,
)


class NewspaperCreationFormTest(TestCase):
    def setUp(self):
        self.topic = Topic.objects.create(name="Technology")
        self.redactor = Redactor.objects.create(
            first_name="John",
            last_name="Doe",
            username="johndoe",
            email="johndoe@example.com"
        )

    def test_valid_form(self):
        data = {
            "title": "Breaking News",
            "content": "This is some breaking news content.",
            "published_date": "2024-12-19",
            "topics": [self.topic.id],
            "publishers": [self.redactor.id],
        }
        form = NewspaperCreationForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        data = {
            "title": "",  # Missing required title
            "content": "",
        }
        form = NewspaperCreationForm(data=data)
        self.assertFalse(form.is_valid())


class NewspaperUpdateFormTest(TestCase):
    def setUp(self):
        self.topic = Topic.objects.create(name="Science")
        self.newspaper = Newspaper.objects.create(
            title="Old News",
            content="This is old news content.",
            published_date="2024-12-18",
        )
        self.newspaper.topics.add(self.topic)

    def test_valid_update_form(self):
        data = {
            "title": "Updated News",
            "content": "Updated news content.",
            "topics": [self.topic.id],
        }
        form = NewspaperUpdateForm(instance=self.newspaper, data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_update_form(self):
        data = {
            "title": "",  # Title is required
        }
        form = NewspaperUpdateForm(instance=self.newspaper, data=data)
        self.assertFalse(form.is_valid())


class NewspaperSearchFormTest(TestCase):
    def test_valid_search_form(self):
        data = {"title": "Breaking"}
        form = NewspaperSearchForm(data=data)
        self.assertTrue(form.is_valid())

    def test_empty_search_form(self):
        data = {}
        form = NewspaperSearchForm(data=data)
        self.assertTrue(form.is_valid())  # Empty search forms should still be valid


class TopicCreateFormTest(TestCase):
    def test_valid_topic_form(self):
        data = {"name": "New Topic"}
        form = TopicCreateForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_topic_form(self):
        data = {"name": ""}  # Name is required
        form = TopicCreateForm(data=data)
        self.assertFalse(form.is_valid())


class RedactorCreateFormTest(TestCase):
    def test_valid_redactor_form(self):
        data = {
            "first_name": "Alice",
            "last_name": "Smith",
            "username": "alicesmith",
            "email": "alice@example.com",
        }
        form = RedactorCreateForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_redactor_form(self):
        data = {
            "first_name": "",  # Missing required fields
            "last_name": "",
            "username": "",
            "email": "",
        }
        form = RedactorCreateForm(data=data)
        self.assertFalse(form.is_valid())


class RedactorSearchFormTest(TestCase):
    def test_valid_search_form(self):
        data = {"first_name": "John"}
        form = RedactorSearchForm(data=data)
        self.assertTrue(form.is_valid())

    def test_empty_search_form(self):
        data = {}
        form = RedactorSearchForm(data=data)
        self.assertTrue(form.is_valid())
