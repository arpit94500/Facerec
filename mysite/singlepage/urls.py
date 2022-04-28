from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("sections/<int:num>", views.section, name='section'),
path("video_feed1/", views.video_feed1,  name='video_feed1'),
]