import random as r

from django.http import (
    HttpRequest,
    HttpResponse,
    HttpResponsePermanentRedirect,
    HttpResponseRedirect,
)
from django.shortcuts import redirect, render
from django.utils import timezone


def index(request: HttpRequest) -> HttpResponse:
    context: dict[str, list[dict[str, int | str | timezone.datetime]]] = {
        "articles": [
            {
                "id": 1,
                "title": "Post 01",
                "body": (
                    "test post.\n"
                    "Lorem ipsum dolor sit amet, \n"
                    "consectetur adipiscing elit, \n"
                    "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.\n"
                ),
                "posted_at": timezone.now(),
            },
        ],
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
