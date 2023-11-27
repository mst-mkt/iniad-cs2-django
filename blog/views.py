from datetime import datetime

from django.http import (
    HttpRequest,
    HttpResponse,
    HttpResponsePermanentRedirect,
    HttpResponseRedirect,
)
from django.shortcuts import redirect, render
from django.utils import timezone


def index(request: HttpRequest) -> HttpResponse:
    context: dict[str, list[dict[str, int | str | datetime]]] = {
        "articles": [
            {
                "id": 1,
                "title": "Post 01",
                "body": "test post.\nLorem ipsum dolor sit amet, \nconsectetur adipiscing elit,\n sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.\n",
                "posted_at": timezone.now(),
            },
        ],
    }
    return render(request, "blog/index.html", context)


def hello(request: HttpRequest) -> HttpResponse:
    data = {
        "name": "Alice",
        "weather": "CLOUDY",
        "weather_details": [
            "Temperature: 23℃",
            "Humidity: 40%",
            "Wind: 5m/s",
        ],
        "is_great_fortune": True,
        "fortune": "Great Fortune!",
    }
    return render(request, "blog/hello.html", data)


def redirect_test(request: HttpRequest) -> HttpResponseRedirect | HttpResponsePermanentRedirect:
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
