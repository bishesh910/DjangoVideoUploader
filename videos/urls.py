
from django.contrib import admin
from django.urls import path
from .views import CreateVideo, DeleteVideo, DetailVideo, UpdateVideo

urlpatterns = [
    path('create/', CreateVideo.as_view() , name='video-create'),
    path('<int:pk>/', DetailVideo.as_view(), name='video-detail'),
    path('<int:pk>/update', UpdateVideo.as_view(), name='video-update'),
    path('<int:pk>/delete', DeleteVideo.as_view(), name='video-delete'),
]