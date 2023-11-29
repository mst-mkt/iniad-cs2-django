from typing import TYPE_CHECKING

from django.db import models
from django.utils import timezone

if TYPE_CHECKING:
    from django.db.models.manager import RelatedManager


class Article(models.Model):
    id = models.AutoField(primary_key=True)  # noqa: A003
    title = models.CharField(max_length=200)
    body = models.TextField()
    posted_at = models.DateTimeField(default=timezone.now)
    published_at = models.DateTimeField(null=True, blank=True)
    like = models.IntegerField(default=0)

    if TYPE_CHECKING:
        comments: "RelatedManager[Comment]"

    def __str__(self: "Article") -> str:
        return self.title

    def publish(self: "Article") -> None:
        self.published_at = timezone.now()
        self.save()


class Comment(models.Model):
    text = models.TextField()
    posted_at = models.DateTimeField(default=timezone.now)
    article = models.ForeignKey(Article, related_name="comments", on_delete=models.CASCADE)

    def __str__(self: "Comment") -> str:
        return self.text
