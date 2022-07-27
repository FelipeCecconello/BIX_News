from django.urls import path
from . import views

urlpatterns = [
    path('', views.news, name='index'),
    path('news/<int:id>/<slug:slug>', views.news_detail, name='news_detail'),
    path('send/', views.send_email, name='send_email'),
]