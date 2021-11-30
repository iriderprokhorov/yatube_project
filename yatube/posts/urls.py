from django.urls import path

from . import views

urlpatterns = [
    # Главная страница
    path('', views.index),
    # Отдельная страница с информацией о group
    path('group/<slug:slug>/', views.group_posts),
]