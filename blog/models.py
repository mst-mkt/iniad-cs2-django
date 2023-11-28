from django.db import models
from django.utils import timezone


class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    body = models.TextField()
    posted_at = models.DateTimeField(default=timezone.now)
    published_at = models.DateTimeField(null=True, blank=True)
    like = models.IntegerField(default=0)

    def __str__(self: "Article") -> str:
        return self.title

    def publish(self: "Article") -> None:
        self.published_at = timezone.now()
        self.save()
