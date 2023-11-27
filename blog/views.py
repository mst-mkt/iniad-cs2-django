from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "blog/index.html")


def update(_: HttpRequest, article_id: int) -> HttpResponse:
    return HttpResponse(f"article_id: {article_id}")


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
