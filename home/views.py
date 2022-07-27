from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render
from news.models import News, Comment
from .tasks import send_mail_func


def news(request):
    new = News.objects.all().filter(status='POSTED').order_by('-id')
    random_news = News.objects.filter(status='POSTED').order_by('?')[:5]
    latest_news = News.objects.filter(status='POSTED').order_by('-id')[:3]

    paginator = Paginator(new, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'latest_news': latest_news,
    }

    return render(request, 'pages/news.html', context)


def news_detail(request, id, slug):
    news = News.objects.get(pk=id)
    comments = Comment.objects.filter(news_id=id)
    random_news = News.objects.filter(status='POSTED').order_by('?')[:5]
    total_comments = 0

    for comment in comments:
        total_comments += 1

    context = {
        'news': news,
        'random_news': random_news,
        'comments': comments,
        'total_comments': total_comments
    }

    return render(request, 'pages/news_detail.html', context)


def send_email(request):
    url = request.META.get('HTTP_REFERER')
    send_mail_func.delay()
    return HttpResponseRedirect(url)
