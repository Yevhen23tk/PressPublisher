from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import now


class Redactor(AbstractUser):

    class Meta:
        verbose_name_plural = 'Redactors'
        verbose_name = 'Redactor'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Topic(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Newspaper(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    published_date = models.DateField(default=now)
    # published_date = models.DateField(auto_now_add=True)
    topics = models.ManyToManyField(Topic, related_name="newspapers")
    publishers = models.ManyToManyField(Redactor, related_name="newspapers")

    def __str__(self):
        return self.title
