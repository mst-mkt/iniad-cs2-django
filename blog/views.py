import random as r
from typing import TYPE_CHECKING

from django.http import (
    HttpRequest,
    HttpResponse,
    HttpResponsePermanentRedirect,
    HttpResponseRedirect,
)
from django.shortcuts import redirect, render

from blog.models import Article

if TYPE_CHECKING:
    from django.db.models import BaseManager


def index(request: HttpRequest) -> HttpResponse:
    context: dict[str, BaseManager[Article]] = {
        "articles": Article.objects.all(),
    }
    return render(request, "blog/index.html", context)


def hello(request: HttpRequest) -> HttpResponse:
    fortune = r.randint(0, 2)
    fortune_message = [
        "Great Fortune!",
        "Small Fortune",
        "Bad Fortune...",
    ][fortune]

    data = {
        "name": "Alice",
        "weather": "CLOUDY",
        "weather_details": [
            "Temperature: 23℃",
            "Humidity: 40%",
            "Wind: 5m/s",
        ],
        "is_great_fortune": fortune == 0,
        "fortune": fortune_message,
    }

    return render(request, "blog/hello.html", data)


def redirect_test() -> HttpResponseRedirect | HttpResponsePermanentRedirect:
    return redirect(hello)


def detail(request: HttpRequest, article_id: int) -> HttpResponse:
    content = {
        "article_id": article_id,
    }
    return render(request, "blog/tbd.html", content)


def update(request: HttpRequest, article_id: int) -> HttpResponse:
    content = {
        "article_id": article_id,
    }
    return render(request, "blog/tbd.html", content)


def delete() -> HttpResponseRedirect | HttpResponsePermanentRedirect:
    return redirect(index)
