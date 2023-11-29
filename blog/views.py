import random as r

from django.http import (
    Http404,
    HttpRequest,
    HttpResponse,
    HttpResponsePermanentRedirect,
    HttpResponseRedirect,
)
from django.shortcuts import redirect, render

from blog.models import Article, Comment


def index(
    request: HttpRequest,
) -> HttpResponse | HttpResponseRedirect | HttpResponsePermanentRedirect:
    if request.method == "POST":
        article = Article(
            title=request.POST.get("title", ""),
            body=request.POST.get("text", ""),
        )
        article.save()
        return redirect(detail, article.id)

    context = {
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
    try:
        article = Article.objects.get(pk=article_id)
    except Article.DoesNotExist:
        msg = "Article does not exist"
        raise Http404(msg) from None

    if request.method == "POST":
        comment = Comment(
            article=article,
            text=request.POST.get("text", ""),
        )
        comment.save()

    content = {
        "article": article,
        "comments": article.comments.order_by("-posted_at"),
    }
    return render(request, "blog/detail.html", content)


def update(request: HttpRequest, article_id: int) -> HttpResponse:
    try:
        article = Article.objects.get(pk=article_id)
    except Article.DoesNotExist:
        msg = "Article does not exist"
        raise Http404(msg) from None
    if request.method == "POST":
        article.title = request.POST.get("title", "")
        article.body = request.POST.get("text", "")
        article.save()
        return redirect(detail, article_id)
    content = {
        "article": article,
    }
    return render(request, "blog/edit.html", content)


def delete(_: HttpRequest, article_id: int) -> HttpResponseRedirect | HttpResponsePermanentRedirect:
    try:
        article = Article.objects.get(pk=article_id)
    except Article.DoesNotExist:
        msg = "Article does not exist"
        raise Http404(msg) from None

    article.delete()
    return redirect(index)


def like(_: HttpRequest, article_id: int) -> HttpResponseRedirect | HttpResponsePermanentRedirect:
    try:
        article = Article.objects.get(pk=article_id)
        article.like += 1
        article.save()
    except Article.DoesNotExist:
        msg = "Article does not exist"
        raise Http404(msg) from None

    return redirect(detail, article_id)
