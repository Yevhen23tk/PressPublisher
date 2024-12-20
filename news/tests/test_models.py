from django.test import TestCase
from django.utils.timezone import localdate
from django.db import IntegrityError
from news.models import Redactor, Topic, Newspaper


class RedactorModelTest(TestCase):
    def test_redactor_str(self):
        redactor = Redactor.objects.create(
            username="jdoe",
            first_name="John",
            last_name="Doe",
            email="jdoe@example.com"
        )
        self.assertEqual(str(redactor), "John Doe")


class TopicModelTest(TestCase):
    def test_topic_str(self):
        topic = Topic.objects.create(name="Technology")
        self.assertEqual(str(topic), "Technology")

    def test_unique_topic_name(self):
        Topic.objects.create(name="Health")
        with self.assertRaises(IntegrityError):
            # Attempt to create another topic with the same name
            Topic.objects.create(name="Health")


class NewspaperModelTest(TestCase):
    def setUp(self):
        self.topic_science = Topic.objects.create(name="Science")
        self.topic_politics = Topic.objects.create(name="Politics")

        self.redactor_jane = Redactor.objects.create(
            username="jane_smith",
            first_name="Jane",
            last_name="Smith",
            email="janesmith@example.com"
        )
        self.redactor_bob = Redactor.objects.create(
            username="bob_brown",
            first_name="Bob",
            last_name="Brown",
            email="bobbrown@example.com"
        )

    def test_newspaper_str(self):
        newspaper = Newspaper.objects.create(
            title="Global News",
            content="A brief content about global events."
        )
        self.assertEqual(str(newspaper), "Global News")

    def test_default_published_date(self):
        newspaper = Newspaper.objects.create(
            title="Daily Tech Update",
            content="All the latest in tech."
        )
        # The default is `now`, which is a datetime with timezone. We only check the date.
        self.assertEqual(newspaper.published_date, localdate())

    def test_newspaper_topics(self):
        newspaper = Newspaper.objects.create(
            title="Science Weekly",
            content="Focus on recent scientific discoveries."
        )
        newspaper.topics.set([self.topic_science, self.topic_politics])
        self.assertEqual(newspaper.topics.count(), 2)
        self.assertIn(self.topic_science, newspaper.topics.all())
        self.assertIn(self.topic_politics, newspaper.topics.all())

    def test_newspaper_publishers(self):
        newspaper = Newspaper.objects.create(
            title="Political Daily",
            content="Today's political headlines."
        )
        newspaper.publishers.set([self.redactor_jane, self.redactor_bob])
        self.assertEqual(newspaper.publishers.count(), 2)
        self.assertIn(self.redactor_jane, newspaper.publishers.all())
        self.assertIn(self.redactor_bob, newspaper.publishers.all())
