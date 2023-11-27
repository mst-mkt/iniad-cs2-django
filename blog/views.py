from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "blog/index.html")


def update(request: HttpRequest, article_id: int) -> HttpResponse:
    return HttpResponse(f"article_id: {article_id}")


def hello(request: HttpRequest) -> HttpResponse:
    data = {
        "name": "Alice",
        "weather": "CLOUDY",
        "fortune": "Great Fortune!",
    }
    return render(request, "blog/hello.html", data)
